"""Chat completions resource.

Delegates to the official ``openai`` Python SDK so customers get full
feature parity (tool use, structured outputs, streaming, multi-modal
inputs) without us having to reimplement OpenAI semantics. The OpenAI
client is configured against the Graphn inference host with the
workspace API key and ``X-Workspace-Id`` as a default header so the
model gateway can route the request to the right workspace.

In addition to plain delegation we add a thin ``Completions`` /
``AsyncCompletions`` wrapper with two features the upstream client
cannot know about:

1. **Bare custom-model id acceptance.** Customers pass
   ``model=model.id`` (e.g. ``"cm_abc123"``) and the wrapper
   prepends the gateway's ``"custom:"`` routing namespace before
   delegating. First-party model ids (``meta-llama/...``) and
   already-prefixed strings (``"custom:cm_..."``) are passed through
   unchanged. The gateway protocol still uses the prefixed form on
   the wire — this just keeps customer code from having to know
   about the prefix.

2. **Auto-wake on cold start.** Custom models default to
   ``min_replicas=0`` and scale to zero after a cooldown. The first
   chat request after a scale-to-zero returns ``503`` with a body
   like::

       {"error": {"message": "Model is scaled to zero and is now
       warming up. Try again in 1-2 minutes.", ...}}

   When the request targets a custom model we recognize that error,
   call ``POST /custom-models/{cm_id}/wake`` once, and then retry
   the chat call with exponential backoff until the gateway starts
   serving or the warm-up budget is exhausted. On by default;
   customers who want raw behavior can pass ``auto_wake=False`` or
   use ``client.chat.openai_client.chat.completions.create``
   directly.
"""

from __future__ import annotations

import asyncio
import contextlib
import re
import time
from typing import TYPE_CHECKING, Any

from graphn._transport import AsyncTransport, SyncTransport

if TYPE_CHECKING:  # pragma: no cover
    from openai import AsyncOpenAI, OpenAI

DEFAULT_WAKE_TIMEOUT_SECONDS = 180.0
_INITIAL_BACKOFF_SECONDS = 2.0
_MAX_BACKOFF_SECONDS = 15.0

_CUSTOM_MODEL_PREFIX = "custom:"
_CUSTOM_ID_RE = re.compile(r"^cm_[a-f0-9]+$")
_COLD_START_PATTERNS = (
    "scaled to zero",
    "warming up",
    "not ready",
    "no available replicas",
)


def _build_sync_openai(transport: SyncTransport) -> OpenAI:
    from openai import OpenAI

    cfg = transport.cfg
    return OpenAI(
        api_key=cfg.api_key,
        base_url=f"{cfg.inference_url}/v1",
        default_headers={"X-Workspace-Id": cfg.workspace_id, **cfg.default_headers},
        timeout=cfg.timeout,
        max_retries=cfg.max_retries,
    )


def _build_async_openai(transport: AsyncTransport) -> AsyncOpenAI:
    from openai import AsyncOpenAI

    cfg = transport.cfg
    return AsyncOpenAI(
        api_key=cfg.api_key,
        base_url=f"{cfg.inference_url}/v1",
        default_headers={"X-Workspace-Id": cfg.workspace_id, **cfg.default_headers},
        timeout=cfg.timeout,
        max_retries=cfg.max_retries,
    )


def _normalize_model_param(model: Any) -> Any:
    """Add the ``"custom:"`` routing prefix to bare custom-model ids.

    The Graphn model gateway routes inference under two namespaces —
    first-party catalog (``meta-llama/Llama-3.1-8B-Instruct`` etc.)
    and per-workspace custom (``custom:cm_...``). The prefix is a
    wire-level routing detail customers shouldn't have to type, so
    accept any of:

    * Bare custom id: ``"cm_abc123"`` -> ``"custom:cm_abc123"``.
    * Pre-prefixed: ``"custom:cm_abc123"`` -> unchanged.
    * First-party id: ``"meta-llama/Llama-3.1-8B-Instruct"`` -> unchanged.
    * Anything that isn't a string (None, an int, etc.): unchanged
      — the OpenAI delegate will produce the same TypeError it
      would produce without us.

    Intentionally permissive: any string that doesn't match the
    bare-cm shape is passed through, so old code that already types
    the prefixed form keeps working without change.
    """

    if not isinstance(model, str):
        return model
    if _CUSTOM_ID_RE.match(model):
        return _CUSTOM_MODEL_PREFIX + model
    return model


def _extract_custom_model_id(model: Any) -> str | None:
    """Return the ``cm_...`` id if ``model`` targets a custom model.

    Used by the auto-wake path to find the right control-plane
    resource to wake. Callers pass the post-normalization value, so
    by the time we see it the bare ``"cm_..."`` case is already
    prefixed. Returns ``None`` for built-in / imported models or any
    other shape, which short-circuits the auto-wake logic.
    """

    if not isinstance(model, str):
        return None
    if not model.startswith(_CUSTOM_MODEL_PREFIX):
        return None
    rest = model[len(_CUSTOM_MODEL_PREFIX) :]
    if not _CUSTOM_ID_RE.match(rest):
        return None
    return rest


def _is_cold_start_error(exc: BaseException) -> bool:
    """Return True if ``exc`` looks like a graphn cold-start 503."""

    status_code = getattr(exc, "status_code", None)
    if status_code not in (502, 503, 504):
        return False
    haystack = str(exc).lower()
    return any(p in haystack for p in _COLD_START_PATTERNS)


def _next_backoff(prev: float) -> float:
    return min(_MAX_BACKOFF_SECONDS, max(_INITIAL_BACKOFF_SECONDS, prev * 1.5))


class Completions:
    """Synchronous ``client.chat.completions`` namespace.

    Delegates to ``openai.OpenAI.chat.completions`` and adds
    auto-wake-on-cold-start for custom models.
    """

    def __init__(
        self,
        openai_client: OpenAI,
        cp_transport: SyncTransport,
    ) -> None:
        self._openai = openai_client
        self._cp = cp_transport

    def create(
        self,
        *args: Any,
        auto_wake: bool = True,
        wake_timeout: float = DEFAULT_WAKE_TIMEOUT_SECONDS,
        **kwargs: Any,
    ) -> Any:
        if "model" in kwargs:
            kwargs["model"] = _normalize_model_param(kwargs["model"])
        try:
            return self._openai.chat.completions.create(*args, **kwargs)
        except Exception as exc:
            if not auto_wake or not _is_cold_start_error(exc):
                raise
            cm_id = _extract_custom_model_id(kwargs.get("model"))
            if cm_id is None:
                raise
            self._wake_and_retry(cm_id, exc, wake_timeout)
            return self._retry_create(args, kwargs, exc, wake_timeout)

    def _wake_and_retry(
        self,
        cm_id: str,
        first_error: BaseException,
        wake_timeout: float,
    ) -> None:
        # POST /custom-models/{cm_id}/wake is idempotent; firing once
        # is enough to nudge KServe to scale up. We do not raise from
        # this call: even if it 4xxs (e.g. someone deleted the model
        # between the two requests) the gateway's response on retry
        # will surface a clearer error to the caller.
        with contextlib.suppress(Exception):
            self._cp.request(
                "POST",
                self._cp.cp_path("custom-models", cm_id, "wake"),
            )

    def _retry_create(
        self,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
        first_error: BaseException,
        wake_timeout: float,
    ) -> Any:
        deadline = time.monotonic() + wake_timeout
        backoff = _INITIAL_BACKOFF_SECONDS
        last_error: BaseException = first_error
        while True:
            sleep_for = min(backoff, max(0.0, deadline - time.monotonic()))
            if sleep_for <= 0:
                raise last_error
            time.sleep(sleep_for)
            try:
                return self._openai.chat.completions.create(*args, **kwargs)
            except Exception as exc:
                if not _is_cold_start_error(exc):
                    raise
                last_error = exc
                if time.monotonic() >= deadline:
                    raise last_error from None
                backoff = _next_backoff(backoff)


class AsyncCompletions:
    """Asynchronous ``client.chat.completions`` namespace."""

    def __init__(
        self,
        openai_client: AsyncOpenAI,
        cp_transport: AsyncTransport,
    ) -> None:
        self._openai = openai_client
        self._cp = cp_transport

    async def create(
        self,
        *args: Any,
        auto_wake: bool = True,
        wake_timeout: float = DEFAULT_WAKE_TIMEOUT_SECONDS,
        **kwargs: Any,
    ) -> Any:
        if "model" in kwargs:
            kwargs["model"] = _normalize_model_param(kwargs["model"])
        try:
            return await self._openai.chat.completions.create(*args, **kwargs)
        except Exception as exc:
            if not auto_wake or not _is_cold_start_error(exc):
                raise
            cm_id = _extract_custom_model_id(kwargs.get("model"))
            if cm_id is None:
                raise
            await self._wake(cm_id)
            return await self._retry_create(args, kwargs, exc, wake_timeout)

    async def _wake(self, cm_id: str) -> None:
        with contextlib.suppress(Exception):
            await self._cp.request(
                "POST",
                self._cp.cp_path("custom-models", cm_id, "wake"),
            )

    async def _retry_create(
        self,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
        first_error: BaseException,
        wake_timeout: float,
    ) -> Any:
        deadline = time.monotonic() + wake_timeout
        backoff = _INITIAL_BACKOFF_SECONDS
        last_error: BaseException = first_error
        while True:
            sleep_for = min(backoff, max(0.0, deadline - time.monotonic()))
            if sleep_for <= 0:
                raise last_error
            await asyncio.sleep(sleep_for)
            try:
                return await self._openai.chat.completions.create(*args, **kwargs)
            except Exception as exc:
                if not _is_cold_start_error(exc):
                    raise
                last_error = exc
                if time.monotonic() >= deadline:
                    raise last_error from None
                backoff = _next_backoff(backoff)


class Chat:
    """Synchronous ``client.chat`` namespace.

    Mirrors ``openai.OpenAI.chat`` so ``client.chat.completions.create(...)``
    works identically. For custom models (``model="cm_..."``) we
    transparently route to the gateway's custom-model namespace and
    wake the model on cold-start 503s. Customers can also reach the
    underlying OpenAI client via :attr:`openai_client` if they need a
    feature exposed by OpenAI but not surfaced here (for example,
    embeddings).
    """

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self._openai: OpenAI | None = None
        self._completions: Completions | None = None

    @property
    def openai_client(self) -> OpenAI:
        """Lazily-constructed underlying ``openai.OpenAI`` client."""

        if self._openai is None:
            self._openai = _build_sync_openai(self._transport)
        return self._openai

    @property
    def completions(self) -> Completions:
        if self._completions is None:
            self._completions = Completions(self.openai_client, self._transport)
        return self._completions


class AsyncChat:
    """Asynchronous ``client.chat`` namespace."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self._openai: AsyncOpenAI | None = None
        self._completions: AsyncCompletions | None = None

    @property
    def openai_client(self) -> AsyncOpenAI:
        if self._openai is None:
            self._openai = _build_async_openai(self._transport)
        return self._openai

    @property
    def completions(self) -> AsyncCompletions:
        if self._completions is None:
            self._completions = AsyncCompletions(self.openai_client, self._transport)
        return self._completions
