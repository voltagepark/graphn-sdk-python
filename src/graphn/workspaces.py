"""Workspaces inside an organization."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import page_params


class Workspace(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    organization_id: str
    name: str
    owner_id: str
    created_at: datetime
    updated_at: datetime


class Workspaces:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(self, org_id: str, *, name: str) -> Workspace:
        data = self._transport.request(
            "POST",
            self._transport.org_path(org_id, "workspaces"),
            json={"name": name},
        )
        return Workspace.model_validate(data)

    def list(
        self,
        org_id: str,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[Workspace]:
        def fetch(token: str | None) -> RawPage[Workspace]:
            data = self._transport.request(
                "GET",
                self._transport.org_path(org_id, "workspaces"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, Workspace.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, org_id: str, workspace_id: str) -> Workspace:
        data = self._transport.request("GET", self._transport.org_path(org_id, workspace_id))
        return Workspace.model_validate(data)

    def update(self, org_id: str, workspace_id: str, *, name: str) -> Workspace:
        data = self._transport.request(
            "PATCH",
            self._transport.org_path(org_id, workspace_id),
            json={"name": name},
        )
        return Workspace.model_validate(data)

    def delete(self, org_id: str, workspace_id: str) -> None:
        self._transport.request("DELETE", self._transport.org_path(org_id, workspace_id))


class AsyncWorkspaces:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(self, org_id: str, *, name: str) -> Workspace:
        data = await self._transport.request(
            "POST",
            self._transport.org_path(org_id, "workspaces"),
            json={"name": name},
        )
        return Workspace.model_validate(data)

    async def list(
        self,
        org_id: str,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[Workspace]:
        async def fetch(token: str | None) -> RawPage[Workspace]:
            data = await self._transport.request(
                "GET",
                self._transport.org_path(org_id, "workspaces"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, Workspace.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, org_id: str, workspace_id: str) -> Workspace:
        data = await self._transport.request("GET", self._transport.org_path(org_id, workspace_id))
        return Workspace.model_validate(data)

    async def update(self, org_id: str, workspace_id: str, *, name: str) -> Workspace:
        data = await self._transport.request(
            "PATCH",
            self._transport.org_path(org_id, workspace_id),
            json={"name": name},
        )
        return Workspace.model_validate(data)

    async def delete(self, org_id: str, workspace_id: str) -> None:
        await self._transport.request("DELETE", self._transport.org_path(org_id, workspace_id))
