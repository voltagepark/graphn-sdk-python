"""Workspace-scoped API keys (`gn_...`). The raw key is returned only on create."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, page_params


class ApiKey(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    key_id: str
    workspace_id: str
    description: str
    created_at: datetime
    expires_at: datetime | None = None
    key: str | None = None


class ApiKeys:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(self, *, description: str, expires_at: str | None = None) -> ApiKey:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("api-keys"),
            json=compact({"description": description, "expires_at": expires_at}),
        )
        return ApiKey.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[ApiKey]:
        def fetch(token: str | None) -> RawPage[ApiKey]:
            data = (
                self._transport.request(
                    "GET",
                    self._transport.cp_path("api-keys"),
                    params=page_params(limit, token),
                )
                or {}
            )
            items = data.get("api_keys") or data.get("items") or []
            return RawPage(
                items=[ApiKey.model_validate(item) for item in items],
                count=len(items),
                continue_token=data.get("continue_token"),
            )

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def delete(self, key_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("api-keys", key_id))


class AsyncApiKeys:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(self, *, description: str, expires_at: str | None = None) -> ApiKey:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("api-keys"),
            json=compact({"description": description, "expires_at": expires_at}),
        )
        return ApiKey.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[ApiKey]:
        async def fetch(token: str | None) -> RawPage[ApiKey]:
            data = (
                await self._transport.request(
                    "GET",
                    self._transport.cp_path("api-keys"),
                    params=page_params(limit, token),
                )
                or {}
            )
            items = data.get("api_keys") or data.get("items") or []
            return RawPage(
                items=[ApiKey.model_validate(item) for item in items],
                count=len(items),
                continue_token=data.get("continue_token"),
            )

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def delete(self, key_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("api-keys", key_id))
