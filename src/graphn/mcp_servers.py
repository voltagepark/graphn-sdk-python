"""Hosted and remote MCP servers, tools, and runtime control."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params


class McpServer(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    workspace_id: str
    name: str
    spec: dict[str, Any]
    created_at: datetime
    updated_at: datetime
    owner_id: str | None = None
    tools: list[dict[str, Any]] | None = None
    workflow_id: str | None = None
    published_version_id: str | None = None
    has_unpublished_changes: bool | None = None
    status: str | None = None
    runtime_status: str | None = None
    runtime_error: str | None = None


class McpServers:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> McpServer:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("mcp-servers"),
            json=merge_extra(compact({"name": name, **fields}), extra),
            idempotency_key=idempotency_key,
        )
        return McpServer.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> SyncPage[McpServer]:
        def fetch(token: str | None) -> RawPage[McpServer]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("mcp-servers"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, McpServer.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, server_id: str) -> McpServer:
        data = self._transport.request("GET", self._transport.cp_path("mcp-servers", server_id))
        return McpServer.model_validate(data)

    def get_by_name(self, name: str) -> McpServer:
        data = self._transport.request(
            "GET", self._transport.cp_path("mcp-servers", "by-name", name)
        )
        return McpServer.model_validate(data)

    def update(self, server_id: str, **fields: Any) -> McpServer:
        extra = fields.pop("extra", None)
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("mcp-servers", server_id),
            json=merge_extra(compact(fields), extra),
        )
        return McpServer.model_validate(data)

    def delete(self, server_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("mcp-servers", server_id))

    def publish(self, server_id: str) -> McpServer:
        data = self._transport.request(
            "POST", self._transport.cp_path("mcp-servers", server_id, "publish")
        )
        return McpServer.model_validate(data)

    def start(self, server_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", server_id, "start")
            )
            or {}
        )

    def stop(self, server_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", server_id, "stop")
            )
            or {}
        )

    def status(self, server_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("mcp-servers", server_id, "status")
            )
            or {}
        )

    def tools(self, server_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("mcp-servers", server_id, "tools")
            )
            or {}
        )

    def refresh_tools(self, server_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", server_id, "refresh-tools")
            )
            or {}
        )

    def test_tool(
        self, server_id: str, *, tool_name: str, arguments: Mapping[str, Any] | None = None
    ) -> dict[str, Any]:
        return (
            self._transport.request(
                "POST",
                self._transport.cp_path("mcp-servers", server_id, "tools", tool_name, "test"),
                json=compact({"arguments": arguments}),
            )
            or {}
        )

    def versions(self, server_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("mcp-servers", server_id, "versions")
            )
            or {}
        )

    def discover_tools(self, **fields: Any) -> dict[str, Any]:
        return (
            self._transport.request(
                "POST",
                self._transport.cp_path("mcp-servers", "discover-tools"),
                json=compact(fields),
            )
            or {}
        )

    def dry_run(self, **fields: Any) -> dict[str, Any]:
        return (
            self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", "dry-run"), json=compact(fields)
            )
            or {}
        )


class AsyncMcpServers:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> McpServer:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("mcp-servers"),
            json=merge_extra(compact({"name": name, **fields}), extra),
            idempotency_key=idempotency_key,
        )
        return McpServer.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> AsyncPage[McpServer]:
        async def fetch(token: str | None) -> RawPage[McpServer]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("mcp-servers"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, McpServer.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, server_id: str) -> McpServer:
        data = await self._transport.request(
            "GET", self._transport.cp_path("mcp-servers", server_id)
        )
        return McpServer.model_validate(data)

    async def get_by_name(self, name: str) -> McpServer:
        data = await self._transport.request(
            "GET", self._transport.cp_path("mcp-servers", "by-name", name)
        )
        return McpServer.model_validate(data)

    async def update(self, server_id: str, **fields: Any) -> McpServer:
        extra = fields.pop("extra", None)
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("mcp-servers", server_id),
            json=merge_extra(compact(fields), extra),
        )
        return McpServer.model_validate(data)

    async def delete(self, server_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("mcp-servers", server_id))

    async def publish(self, server_id: str) -> McpServer:
        data = await self._transport.request(
            "POST", self._transport.cp_path("mcp-servers", server_id, "publish")
        )
        return McpServer.model_validate(data)

    async def start(self, server_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", server_id, "start")
            )
            or {}
        )

    async def stop(self, server_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", server_id, "stop")
            )
            or {}
        )

    async def status(self, server_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("mcp-servers", server_id, "status")
            )
            or {}
        )

    async def tools(self, server_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("mcp-servers", server_id, "tools")
            )
            or {}
        )

    async def refresh_tools(self, server_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", server_id, "refresh-tools")
            )
            or {}
        )

    async def test_tool(
        self, server_id: str, *, tool_name: str, arguments: Mapping[str, Any] | None = None
    ) -> dict[str, Any]:
        return (
            await self._transport.request(
                "POST",
                self._transport.cp_path("mcp-servers", server_id, "tools", tool_name, "test"),
                json=compact({"arguments": arguments}),
            )
            or {}
        )

    async def versions(self, server_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("mcp-servers", server_id, "versions")
            )
            or {}
        )

    async def discover_tools(self, **fields: Any) -> dict[str, Any]:
        return (
            await self._transport.request(
                "POST",
                self._transport.cp_path("mcp-servers", "discover-tools"),
                json=compact(fields),
            )
            or {}
        )

    async def dry_run(self, **fields: Any) -> dict[str, Any]:
        return (
            await self._transport.request(
                "POST", self._transport.cp_path("mcp-servers", "dry-run"), json=compact(fields)
            )
            or {}
        )
