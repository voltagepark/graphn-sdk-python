"""HTTP transport shared by :mod:`graphn._client`.

Wraps ``httpx.Client`` / ``httpx.AsyncClient`` with:

* ``Authorization: Bearer <api_key>`` injection
* ``X-Workspace-Id`` default header (the inference path also derives the
  workspace from this header; the control plane uses both the path
  parameter and the header)
* ``X-Request-Id`` round-tripping (we generate one if the caller
  doesn't supply one)
* JSON decoding + structured error mapping into
  :class:`graphn._exceptions.APIError` subclasses
* Bounded retries on connect failures, 429, and 5xx responses with
  exponential backoff

The control-plane URL construction utility :func:`cp_path` lives here
too so resource modules can call ``self._transport.cp_path("custom-models")``
and stay agnostic of the workspace id wiring.
"""

from __future__ import annotations

import asyncio
import json as _json
import time
import uuid
from collections.abc import Mapping
from typing import Any
from urllib.parse import quote

import httpx

from graphn._exceptions import APIConnectionError, APIError, from_response
from graphn._version import __version__

_DEFAULT_RETRY_STATUSES = frozenset({408, 425, 429, 500, 502, 503, 504})


def _user_agent() -> str:
    return f"graphn-python/{__version__} httpx/{httpx.__version__}"


def _normalize_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    return {str(k): str(v) for k, v in (headers or {}).items()}


def _sleep_for_retry(attempt: int, retry_after: str | None) -> float:
    """Compute backoff for retry attempt ``attempt`` (0-indexed)."""

    if retry_after is not None:
        try:
            return max(0.0, float(retry_after))
        except ValueError:
            pass
    # Exponential backoff: 0.5s, 1s, 2s, 4s, capped at 8s.
    return min(8.0, 0.5 * (2**attempt))


def _build_error(
    response: httpx.Response, *, request_id: str | None
) -> APIError:
    body: Any
    try:
        body = response.json()
    except (ValueError, _json.JSONDecodeError):
        body = None

    code: str | None = None
    message: str = response.reason_phrase or f"HTTP {response.status_code}"
    details: dict[str, Any] | None = None
    if isinstance(body, dict):
        code = body.get("code") if isinstance(body.get("code"), str) else None
        if isinstance(body.get("message"), str):
            message = body["message"]
        if isinstance(body.get("details"), dict):
            details = body["details"]

    return from_response(
        status_code=response.status_code,
        code=code,
        message=message,
        details=details,
        request_id=request_id or response.headers.get("X-Request-Id"),
    )


class _TransportConfig:
    """Configuration shared by sync and async transports."""

    __slots__ = (
        "api_key",
        "base_url",
        "default_headers",
        "inference_url",
        "max_retries",
        "timeout",
        "workspace_id",
    )

    def __init__(
        self,
        *,
        api_key: str,
        workspace_id: str,
        base_url: str,
        inference_url: str,
        timeout: float,
        max_retries: int,
        default_headers: Mapping[str, str] | None = None,
    ) -> None:
        self.api_key = api_key
        self.workspace_id = workspace_id
        self.base_url = base_url.rstrip("/")
        self.inference_url = inference_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.default_headers = _normalize_headers(default_headers)

    def auth_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "X-Workspace-Id": self.workspace_id,
            "User-Agent": _user_agent(),
            "Accept": "application/json",
            **self.default_headers,
        }

    def cp_path(self, *parts: str) -> str:
        """Build a control-plane path with the workspace id injected."""

        encoded = "/".join(quote(p.strip("/"), safe="") for p in parts if p)
        ws = quote(self.workspace_id, safe="")
        return f"/v1/{ws}/{encoded}"


class SyncTransport:
    """Synchronous httpx-backed transport."""

    def __init__(self, cfg: _TransportConfig) -> None:
        self._cfg = cfg
        self._client = httpx.Client(
            base_url=cfg.base_url,
            timeout=cfg.timeout,
            headers=cfg.auth_headers(),
        )

    @property
    def cfg(self) -> _TransportConfig:
        return self._cfg

    def cp_path(self, *parts: str) -> str:
        return self._cfg.cp_path(*parts)

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        request_id = (
            (headers or {}).get("X-Request-Id") if headers else None
        ) or uuid.uuid4().hex
        merged_headers: dict[str, str] = {"X-Request-Id": request_id}
        if idempotency_key:
            merged_headers["Idempotency-Key"] = idempotency_key
        if headers:
            merged_headers.update(_normalize_headers(headers))

        last_exc: Exception | None = None
        for attempt in range(self._cfg.max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    path,
                    json=json,
                    params=params,
                    headers=merged_headers,
                )
            except httpx.HTTPError as exc:
                last_exc = exc
                if attempt >= self._cfg.max_retries:
                    raise APIConnectionError(str(exc)) from exc
                time.sleep(_sleep_for_retry(attempt, None))
                continue

            if (
                response.status_code in _DEFAULT_RETRY_STATUSES
                and attempt < self._cfg.max_retries
            ):
                time.sleep(
                    _sleep_for_retry(attempt, response.headers.get("Retry-After"))
                )
                continue

            return _decode(response, request_id)

        if last_exc is not None:
            raise APIConnectionError(str(last_exc)) from last_exc
        raise APIConnectionError("retries exhausted")

    def close(self) -> None:
        self._client.close()


class AsyncTransport:
    """Asynchronous httpx-backed transport."""

    def __init__(self, cfg: _TransportConfig) -> None:
        self._cfg = cfg
        self._client = httpx.AsyncClient(
            base_url=cfg.base_url,
            timeout=cfg.timeout,
            headers=cfg.auth_headers(),
        )

    @property
    def cfg(self) -> _TransportConfig:
        return self._cfg

    def cp_path(self, *parts: str) -> str:
        return self._cfg.cp_path(*parts)

    async def request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        request_id = (
            (headers or {}).get("X-Request-Id") if headers else None
        ) or uuid.uuid4().hex
        merged_headers: dict[str, str] = {"X-Request-Id": request_id}
        if idempotency_key:
            merged_headers["Idempotency-Key"] = idempotency_key
        if headers:
            merged_headers.update(_normalize_headers(headers))

        last_exc: Exception | None = None
        for attempt in range(self._cfg.max_retries + 1):
            try:
                response = await self._client.request(
                    method,
                    path,
                    json=json,
                    params=params,
                    headers=merged_headers,
                )
            except httpx.HTTPError as exc:
                last_exc = exc
                if attempt >= self._cfg.max_retries:
                    raise APIConnectionError(str(exc)) from exc
                await asyncio.sleep(_sleep_for_retry(attempt, None))
                continue

            if (
                response.status_code in _DEFAULT_RETRY_STATUSES
                and attempt < self._cfg.max_retries
            ):
                await asyncio.sleep(
                    _sleep_for_retry(attempt, response.headers.get("Retry-After"))
                )
                continue

            return _decode(response, request_id)

        if last_exc is not None:
            raise APIConnectionError(str(last_exc)) from last_exc
        raise APIConnectionError("retries exhausted")

    async def aclose(self) -> None:
        await self._client.aclose()


def _decode(response: httpx.Response, request_id: str) -> Any:
    if response.status_code >= 400:
        raise _build_error(response, request_id=request_id)
    if response.status_code == 204 or not response.content:
        return None
    try:
        return response.json()
    except (ValueError, _json.JSONDecodeError):
        # Non-JSON 2xx (e.g. audio/mpeg from /v1/tts) — return raw bytes
        # so the caller can handle the binary payload itself.
        return response.content
