"""Chat completions resource.

Delegates to the official ``openai`` Python SDK so customers get full
feature parity (tool use, structured outputs, streaming, multi-modal
inputs) without us having to reimplement OpenAI semantics. The OpenAI
client is configured against the Graphn inference host with the
workspace API key and ``X-Workspace-Id`` as a default header so the
model gateway can route the request to the right workspace.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from graphn._transport import AsyncTransport, SyncTransport

if TYPE_CHECKING:  # pragma: no cover
    from openai import AsyncOpenAI, OpenAI
    from openai.resources.chat.completions import (
        AsyncCompletions as _AsyncOpenAICompletions,
    )
    from openai.resources.chat.completions import (
        Completions as _OpenAICompletions,
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


class Chat:
    """Synchronous ``client.chat`` namespace.

    Mirrors ``openai.OpenAI.chat`` so ``client.chat.completions.create(...)``
    works identically. Customers can also reach the underlying OpenAI
    client via :attr:`openai_client` if they need a feature exposed by
    OpenAI but not surfaced here (for example, embeddings).
    """

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self._openai: OpenAI | None = None

    @property
    def openai_client(self) -> OpenAI:
        """Lazily-constructed underlying ``openai.OpenAI`` client."""

        if self._openai is None:
            self._openai = _build_sync_openai(self._transport)
        return self._openai

    @property
    def completions(self) -> _OpenAICompletions:
        return self.openai_client.chat.completions


class AsyncChat:
    """Asynchronous ``client.chat`` namespace."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self._openai: AsyncOpenAI | None = None

    @property
    def openai_client(self) -> AsyncOpenAI:
        if self._openai is None:
            self._openai = _build_async_openai(self._transport)
        return self._openai

    @property
    def completions(self) -> _AsyncOpenAICompletions:
        return self.openai_client.chat.completions


def _build_chat_create_kwargs(**kwargs: Any) -> dict[str, Any]:
    """Internal helper kept for symmetry with other resource modules."""

    return {k: v for k, v in kwargs.items() if v is not None}
