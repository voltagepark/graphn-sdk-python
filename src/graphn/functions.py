"""Workspace Python functions (FES sandboxes) and builtins."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params


class Function(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    workspace_id: str
    name: str
    spec: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    owner_id: str | None = None
    workflow_id: str | None = None
    published_version_id: str | None = None
    has_unpublished_changes: bool | None = None
    status: str | None = None


class FunctionTestResponse(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    success: bool
    output: Any = None
    error: str | None = None
    stdout: str | None = None
    stderr: str | None = None
    duration_ms: int | None = None
    execution_id: str | None = None


def _create_body(
    *,
    name: str,
    extra: Mapping[str, Any] | None,
    **fields: Any,
) -> dict[str, Any]:
    return merge_extra(compact({"name": name, **fields}), extra)


class Functions:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        type: str | None = None,
        description: str | None = None,
        files: Mapping[str, str] | None = None,
        parameters_schema: Mapping[str, Any] | None = None,
        builtin_name: str | None = None,
        workflow_id: str | None = None,
        memory_mb: int | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Function:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("functions"),
            json=_create_body(
                name=name,
                extra=extra,
                type=type,
                description=description,
                files=files,
                parameters_schema=parameters_schema,
                builtin_name=builtin_name,
                workflow_id=workflow_id,
                memory_mb=memory_mb,
            ),
            idempotency_key=idempotency_key,
        )
        return Function.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> SyncPage[Function]:
        def fetch(token: str | None) -> RawPage[Function]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("functions"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, Function.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def builtins(self) -> dict[str, Any]:
        data = self._transport.request("GET", self._transport.cp_path("functions", "builtins"))
        return data or {}

    def get(self, function_id: str) -> Function:
        data = self._transport.request("GET", self._transport.cp_path("functions", function_id))
        return Function.model_validate(data)

    def get_by_name(self, name: str) -> Function:
        data = self._transport.request("GET", self._transport.cp_path("functions", "by-name", name))
        return Function.model_validate(data)

    def update(self, function_id: str, **fields: Any) -> Function:
        extra = fields.pop("extra", None)
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("functions", function_id),
            json=merge_extra(compact(fields), extra),
        )
        return Function.model_validate(data)

    def delete(self, function_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("functions", function_id))

    def publish(self, function_id: str) -> Function:
        data = self._transport.request(
            "POST", self._transport.cp_path("functions", function_id, "publish")
        )
        return Function.model_validate(data)

    def test(
        self, function_id: str, *, input: Mapping[str, Any] | None = None
    ) -> FunctionTestResponse:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("functions", function_id, "test"),
            json=compact({"input": input}),
        )
        return FunctionTestResponse.model_validate(data)

    def dry_run(self, **fields: Any) -> FunctionTestResponse:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("functions", "dry-run"),
            json=compact(fields),
        )
        return FunctionTestResponse.model_validate(data)


class AsyncFunctions:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        type: str | None = None,
        description: str | None = None,
        files: Mapping[str, str] | None = None,
        parameters_schema: Mapping[str, Any] | None = None,
        builtin_name: str | None = None,
        workflow_id: str | None = None,
        memory_mb: int | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Function:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("functions"),
            json=_create_body(
                name=name,
                extra=extra,
                type=type,
                description=description,
                files=files,
                parameters_schema=parameters_schema,
                builtin_name=builtin_name,
                workflow_id=workflow_id,
                memory_mb=memory_mb,
            ),
            idempotency_key=idempotency_key,
        )
        return Function.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> AsyncPage[Function]:
        async def fetch(token: str | None) -> RawPage[Function]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("functions"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, Function.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def builtins(self) -> dict[str, Any]:
        data = await self._transport.request(
            "GET", self._transport.cp_path("functions", "builtins")
        )
        return data or {}

    async def get(self, function_id: str) -> Function:
        data = await self._transport.request(
            "GET", self._transport.cp_path("functions", function_id)
        )
        return Function.model_validate(data)

    async def get_by_name(self, name: str) -> Function:
        data = await self._transport.request(
            "GET", self._transport.cp_path("functions", "by-name", name)
        )
        return Function.model_validate(data)

    async def update(self, function_id: str, **fields: Any) -> Function:
        extra = fields.pop("extra", None)
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("functions", function_id),
            json=merge_extra(compact(fields), extra),
        )
        return Function.model_validate(data)

    async def delete(self, function_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("functions", function_id))

    async def publish(self, function_id: str) -> Function:
        data = await self._transport.request(
            "POST", self._transport.cp_path("functions", function_id, "publish")
        )
        return Function.model_validate(data)

    async def test(
        self, function_id: str, *, input: Mapping[str, Any] | None = None
    ) -> FunctionTestResponse:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("functions", function_id, "test"),
            json=compact({"input": input}),
        )
        return FunctionTestResponse.model_validate(data)

    async def dry_run(self, **fields: Any) -> FunctionTestResponse:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("functions", "dry-run"),
            json=compact(fields),
        )
        return FunctionTestResponse.model_validate(data)
