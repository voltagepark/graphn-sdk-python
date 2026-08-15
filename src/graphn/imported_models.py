"""Imported (BYO) models: workspace CRUD plus inference-host probes."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

import httpx
from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import (
    AsyncTransport,
    SyncTransport,
    _build_error,
    _TransportConfig,
)
from graphn._util import compact, merge_extra, page_params

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


class ImportedModel(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    name: str
    display_name: str
    workspace_id: str
    endpoint: str
    model_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    owner_id: str | None = None
    api_key_secret_id: str | None = None
    type: str | None = None
    description: str | None = None


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

    def create(
        self,
        *,
        name: str,
        display_name: str,
        endpoint: str,
        model_id: str,
        extra: Mapping[str, Any] | None = None,
        **fields: Any,
    ) -> ImportedModel:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("imported-models"),
            json=merge_extra(
                compact(
                    {
                        "name": name,
                        "display_name": display_name,
                        "endpoint": endpoint,
                        "model_id": model_id,
                        **fields,
                    }
                ),
                extra,
            ),
        )
        return ImportedModel.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[ImportedModel]:
        def fetch(token: str | None) -> RawPage[ImportedModel]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("imported-models"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, ImportedModel.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, imported_model_id: str) -> ImportedModel:
        data = self._transport.request(
            "GET", self._transport.cp_path("imported-models", imported_model_id)
        )
        return ImportedModel.model_validate(data)

    def update(self, imported_model_id: str, **fields: Any) -> ImportedModel:
        extra = fields.pop("extra", None)
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("imported-models", imported_model_id),
            json=merge_extra(compact(fields), extra),
        )
        return ImportedModel.model_validate(data)

    def delete(self, imported_model_id: str) -> None:
        self._transport.request(
            "DELETE", self._transport.cp_path("imported-models", imported_model_id)
        )

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

    async def create(
        self,
        *,
        name: str,
        display_name: str,
        endpoint: str,
        model_id: str,
        extra: Mapping[str, Any] | None = None,
        **fields: Any,
    ) -> ImportedModel:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("imported-models"),
            json=merge_extra(
                compact(
                    {
                        "name": name,
                        "display_name": display_name,
                        "endpoint": endpoint,
                        "model_id": model_id,
                        **fields,
                    }
                ),
                extra,
            ),
        )
        return ImportedModel.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[ImportedModel]:
        async def fetch(token: str | None) -> RawPage[ImportedModel]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("imported-models"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, ImportedModel.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, imported_model_id: str) -> ImportedModel:
        data = await self._transport.request(
            "GET", self._transport.cp_path("imported-models", imported_model_id)
        )
        return ImportedModel.model_validate(data)

    async def update(self, imported_model_id: str, **fields: Any) -> ImportedModel:
        extra = fields.pop("extra", None)
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("imported-models", imported_model_id),
            json=merge_extra(compact(fields), extra),
        )
        return ImportedModel.model_validate(data)

    async def delete(self, imported_model_id: str) -> None:
        await self._transport.request(
            "DELETE", self._transport.cp_path("imported-models", imported_model_id)
        )

    async def aclose(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None
