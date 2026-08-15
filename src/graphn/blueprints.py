"""Public workflow blueprint catalog and one-shot deploy."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from urllib.parse import quote

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra


class BlueprintSummary(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    name: str
    description: str | None = None
    category: str | None = None


class Blueprint(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    name: str
    dsl: str
    description: str | None = None


class Blueprints:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(self) -> SyncPage[BlueprintSummary]:
        def fetch(_token: str | None) -> RawPage[BlueprintSummary]:
            data = self._transport.request("GET", "/v1/blueprints")
            return RawPage.from_response(data or {}, BlueprintSummary.model_validate)

        return SyncPage(first=fetch(None), fetch_next=fetch)

    def get(self, blueprint_id: str) -> Blueprint:
        data = self._transport.request("GET", f"/v1/blueprints/{quote(blueprint_id, safe='')}")
        return Blueprint.model_validate(data)

    def deploy(self, blueprint_id: str, **fields: Any) -> dict[str, Any]:
        extra = fields.pop("extra", None)
        return (
            self._transport.request(
                "POST",
                self._transport.cp_path("blueprints", blueprint_id, "deploy"),
                json=merge_extra(compact(fields), extra if isinstance(extra, Mapping) else None),
            )
            or {}
        )


class AsyncBlueprints:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(self) -> AsyncPage[BlueprintSummary]:
        async def fetch(_token: str | None) -> RawPage[BlueprintSummary]:
            data = await self._transport.request("GET", "/v1/blueprints")
            return RawPage.from_response(data or {}, BlueprintSummary.model_validate)

        return AsyncPage(first=await fetch(None), fetch_next=fetch)

    async def get(self, blueprint_id: str) -> Blueprint:
        data = await self._transport.request(
            "GET", f"/v1/blueprints/{quote(blueprint_id, safe='')}"
        )
        return Blueprint.model_validate(data)

    async def deploy(self, blueprint_id: str, **fields: Any) -> dict[str, Any]:
        extra = fields.pop("extra", None)
        return (
            await self._transport.request(
                "POST",
                self._transport.cp_path("blueprints", blueprint_id, "deploy"),
                json=merge_extra(compact(fields), extra if isinstance(extra, Mapping) else None),
            )
            or {}
        )
