"""Imported (BYO) model discovery + connectivity checks.

Both endpoints live on the inference host and are used by the dashboard
to validate user-provided OpenAI-compatible endpoints before importing
them into a workspace.
"""

from __future__ import annotations

from typing import Any

import httpx
from pydantic import BaseModel, ConfigDict

from graphn._transport import (
    AsyncTransport,
    SyncTransport,
    _build_error,
    _TransportConfig,
)

_DISCOVER_PATH = "/v1/imported-models/discover-models"
_TEST_PATH = "/v1/imported-models/test-connection"


class DiscoveredImportedModel(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    name: str


class DiscoverImportedModelsResponse(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    models: list[DiscoveredImportedModel]


class TestConnectionResponse(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    response: str
    model: str
    usage: dict[str, Any] | None = None


def _discover_body(*, endpoint: str, api_key_secret_id: str) -> dict[str, Any]:
    return {"endpoint": endpoint, "api_key_secret_id": api_key_secret_id}


def _test_body(
    *,
    endpoint: str,
    model_id: str,
    api_key_secret_id: str | None,
    message: str | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"endpoint": endpoint, "model_id": model_id}
    if api_key_secret_id is not None:
        body["api_key_secret_id"] = api_key_secret_id
    if message is not None:
        body["message"] = message
    return body


def _inference_headers(cfg: _TransportConfig) -> dict[str, str]:
    headers = cfg.auth_headers()
    headers["Accept"] = "application/json"
    return headers


class ImportedModels:
    """Synchronous imported-models resource."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self._client: httpx.Client | None = None

    def _http(self) -> httpx.Client:
        if self._client is None:
            cfg = self._transport.cfg
            self._client = httpx.Client(base_url=cfg.inference_url, timeout=cfg.timeout)
        return self._client

    def discover(self, *, endpoint: str, api_key_secret_id: str) -> DiscoverImportedModelsResponse:
        cfg = self._transport.cfg
        response = self._http().post(
            _DISCOVER_PATH,
            json=_discover_body(endpoint=endpoint, api_key_secret_id=api_key_secret_id),
            headers=_inference_headers(cfg),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return DiscoverImportedModelsResponse.model_validate(response.json())

    def test_connection(
        self,
        *,
        endpoint: str,
        model_id: str,
        api_key_secret_id: str | None = None,
        message: str | None = None,
    ) -> TestConnectionResponse:
        cfg = self._transport.cfg
        response = self._http().post(
            _TEST_PATH,
            json=_test_body(
                endpoint=endpoint,
                model_id=model_id,
                api_key_secret_id=api_key_secret_id,
                message=message,
            ),
            headers=_inference_headers(cfg),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return TestConnectionResponse.model_validate(response.json())

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
            self._client = None


class AsyncImportedModels:
    """Asynchronous imported-models resource."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self._client: httpx.AsyncClient | None = None

    def _http(self) -> httpx.AsyncClient:
        if self._client is None:
            cfg = self._transport.cfg
            self._client = httpx.AsyncClient(base_url=cfg.inference_url, timeout=cfg.timeout)
        return self._client

    async def discover(
        self, *, endpoint: str, api_key_secret_id: str
    ) -> DiscoverImportedModelsResponse:
        cfg = self._transport.cfg
        response = await self._http().post(
            _DISCOVER_PATH,
            json=_discover_body(endpoint=endpoint, api_key_secret_id=api_key_secret_id),
            headers=_inference_headers(cfg),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return DiscoverImportedModelsResponse.model_validate(response.json())

    async def test_connection(
        self,
        *,
        endpoint: str,
        model_id: str,
        api_key_secret_id: str | None = None,
        message: str | None = None,
    ) -> TestConnectionResponse:
        cfg = self._transport.cfg
        response = await self._http().post(
            _TEST_PATH,
            json=_test_body(
                endpoint=endpoint,
                model_id=model_id,
                api_key_secret_id=api_key_secret_id,
                message=message,
            ),
            headers=_inference_headers(cfg),
        )
        if response.status_code >= 400:
            raise _build_error(response, request_id=None)
        return TestConnectionResponse.model_validate(response.json())

    async def aclose(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None
