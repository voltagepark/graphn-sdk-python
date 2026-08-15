"""Gateway batch jobs over a published workflow."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params


class Batch(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    status: str
    created_at: str
    completed_at: str | None = None
    request_counts: dict[str, Any] | None = None


class Batches:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(self, workflow_id: str, **fields: Any) -> Batch:
        extra = fields.pop("extra", None)
        data = self._transport.request(
            "POST",
            self._transport.gw_url(workflow_id, "batch"),
            json=merge_extra(compact(fields), extra if isinstance(extra, Mapping) else None),
        )
        return Batch.model_validate(data)

    def list(
        self,
        workflow_id: str,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        status: str | None = None,
    ) -> SyncPage[Batch]:
        def fetch(token: str | None) -> RawPage[Batch]:
            data = self._transport.request(
                "GET",
                self._transport.gw_url(workflow_id, "batch"),
                params=page_params(limit, token, status=status),
            )
            return RawPage.from_response(data or {}, Batch.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, workflow_id: str, batch_id: str) -> Batch:
        data = self._transport.request(
            "GET", self._transport.gw_url(workflow_id, "batch", batch_id)
        )
        return Batch.model_validate(data)

    def items(self, workflow_id: str, batch_id: str, **params: Any) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET",
                self._transport.gw_url(workflow_id, "batch", batch_id, "items"),
                params=compact(params),
            )
            or {}
        )

    def output(self, workflow_id: str, batch_id: str) -> bytes:
        body = self._transport.request(
            "GET", self._transport.gw_url(workflow_id, "batch", batch_id, "output.jsonl")
        )
        if isinstance(body, bytes):
            return body
        return b"" if body is None else str(body).encode()

    def cancel(self, workflow_id: str, batch_id: str) -> Batch:
        data = self._transport.request(
            "POST", self._transport.gw_url(workflow_id, "batch", batch_id, "cancel")
        )
        return Batch.model_validate(data)


class AsyncBatches:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(self, workflow_id: str, **fields: Any) -> Batch:
        extra = fields.pop("extra", None)
        data = await self._transport.request(
            "POST",
            self._transport.gw_url(workflow_id, "batch"),
            json=merge_extra(compact(fields), extra if isinstance(extra, Mapping) else None),
        )
        return Batch.model_validate(data)

    async def list(
        self,
        workflow_id: str,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        status: str | None = None,
    ) -> AsyncPage[Batch]:
        async def fetch(token: str | None) -> RawPage[Batch]:
            data = await self._transport.request(
                "GET",
                self._transport.gw_url(workflow_id, "batch"),
                params=page_params(limit, token, status=status),
            )
            return RawPage.from_response(data or {}, Batch.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, workflow_id: str, batch_id: str) -> Batch:
        data = await self._transport.request(
            "GET", self._transport.gw_url(workflow_id, "batch", batch_id)
        )
        return Batch.model_validate(data)

    async def items(self, workflow_id: str, batch_id: str, **params: Any) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET",
                self._transport.gw_url(workflow_id, "batch", batch_id, "items"),
                params=compact(params),
            )
            or {}
        )

    async def output(self, workflow_id: str, batch_id: str) -> bytes:
        body = await self._transport.request(
            "GET", self._transport.gw_url(workflow_id, "batch", batch_id, "output.jsonl")
        )
        if isinstance(body, bytes):
            return body
        return b"" if body is None else str(body).encode()

    async def cancel(self, workflow_id: str, batch_id: str) -> Batch:
        data = await self._transport.request(
            "POST", self._transport.gw_url(workflow_id, "batch", batch_id, "cancel")
        )
        return Batch.model_validate(data)
