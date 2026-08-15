"""Organizations the caller belongs to."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport


class Organization(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    name: str
    slug: str
    type: str
    owner_id: str
    created_at: datetime
    updated_at: datetime


class Organizations:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(self, *, name: str, type: str) -> Organization:
        data = self._transport.request(
            "POST", "/v1/organizations", json={"name": name, "type": type}
        )
        return Organization.model_validate(data)

    def list(self) -> SyncPage[Organization]:
        def fetch(_token: str | None) -> RawPage[Organization]:
            data = self._transport.request("GET", "/v1/organizations")
            return RawPage.from_response(data or {}, Organization.model_validate)

        return SyncPage(first=fetch(None), fetch_next=fetch)

    def get(self, org_id: str) -> Organization:
        data = self._transport.request("GET", self._transport.org_path(org_id))
        return Organization.model_validate(data)

    def update(self, org_id: str, *, name: str) -> Organization:
        data = self._transport.request(
            "PATCH", self._transport.org_path(org_id), json={"name": name}
        )
        return Organization.model_validate(data)

    def delete(self, org_id: str) -> None:
        self._transport.request("DELETE", self._transport.org_path(org_id))


class AsyncOrganizations:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(self, *, name: str, type: str) -> Organization:
        data = await self._transport.request(
            "POST", "/v1/organizations", json={"name": name, "type": type}
        )
        return Organization.model_validate(data)

    async def list(self) -> AsyncPage[Organization]:
        async def fetch(_token: str | None) -> RawPage[Organization]:
            data = await self._transport.request("GET", "/v1/organizations")
            return RawPage.from_response(data or {}, Organization.model_validate)

        return AsyncPage(first=await fetch(None), fetch_next=fetch)

    async def get(self, org_id: str) -> Organization:
        data = await self._transport.request("GET", self._transport.org_path(org_id))
        return Organization.model_validate(data)

    async def update(self, org_id: str, *, name: str) -> Organization:
        data = await self._transport.request(
            "PATCH", self._transport.org_path(org_id), json={"name": name}
        )
        return Organization.model_validate(data)

    async def delete(self, org_id: str) -> None:
        await self._transport.request("DELETE", self._transport.org_path(org_id))
