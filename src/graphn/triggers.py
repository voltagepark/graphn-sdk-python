"""Cron and webhook triggers that invoke a published workflow."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params


class Trigger(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    workspace_id: str
    workflow_id: str
    name: str
    enabled: bool
    created_at: datetime
    updated_at: datetime
    cron_schedule: str | None = None
    input: dict[str, Any] | None = None
    last_error: str | None = None


class Triggers:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        workflow_id: str,
        cron_schedule: str,
        extra: Mapping[str, Any] | None = None,
        **fields: Any,
    ) -> Trigger:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("triggers"),
            json=merge_extra(
                compact(
                    {
                        "name": name,
                        "workflow_id": workflow_id,
                        "cron_schedule": cron_schedule,
                        **fields,
                    }
                ),
                extra,
            ),
        )
        return Trigger.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> SyncPage[Trigger]:
        def fetch(token: str | None) -> RawPage[Trigger]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("triggers"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, Trigger.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, trigger_id: str) -> Trigger:
        data = self._transport.request("GET", self._transport.cp_path("triggers", trigger_id))
        return Trigger.model_validate(data)

    def update(self, trigger_id: str, **fields: Any) -> Trigger:
        extra = fields.pop("extra", None)
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("triggers", trigger_id),
            json=merge_extra(compact(fields), extra),
        )
        return Trigger.model_validate(data)

    def delete(self, trigger_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("triggers", trigger_id))


class AsyncTriggers:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        workflow_id: str,
        cron_schedule: str,
        extra: Mapping[str, Any] | None = None,
        **fields: Any,
    ) -> Trigger:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("triggers"),
            json=merge_extra(
                compact(
                    {
                        "name": name,
                        "workflow_id": workflow_id,
                        "cron_schedule": cron_schedule,
                        **fields,
                    }
                ),
                extra,
            ),
        )
        return Trigger.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> AsyncPage[Trigger]:
        async def fetch(token: str | None) -> RawPage[Trigger]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("triggers"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, Trigger.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, trigger_id: str) -> Trigger:
        data = await self._transport.request("GET", self._transport.cp_path("triggers", trigger_id))
        return Trigger.model_validate(data)

    async def update(self, trigger_id: str, **fields: Any) -> Trigger:
        extra = fields.pop("extra", None)
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("triggers", trigger_id),
            json=merge_extra(compact(fields), extra),
        )
        return Trigger.model_validate(data)

    async def delete(self, trigger_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("triggers", trigger_id))
