"""Workspace agents: CRUD, publish, archive, dry-run, run."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params


class Agent(BaseModel):
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


def _create_body(
    *,
    name: str,
    spec: Mapping[str, Any] | None,
    workflow_id: str | None,
    extra: Mapping[str, Any] | None,
) -> dict[str, Any]:
    return merge_extra(compact({"name": name, "spec": spec, "workflow_id": workflow_id}), extra)


class Agents:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        spec: Mapping[str, Any] | None = None,
        workflow_id: str | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Agent:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("agents"),
            json=_create_body(name=name, spec=spec, workflow_id=workflow_id, extra=extra),
            idempotency_key=idempotency_key,
        )
        return Agent.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> SyncPage[Agent]:
        def fetch(token: str | None) -> RawPage[Agent]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("agents"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, Agent.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, agent_id: str) -> Agent:
        data = self._transport.request("GET", self._transport.cp_path("agents", agent_id))
        return Agent.model_validate(data)

    def get_by_name(self, name: str) -> Agent:
        data = self._transport.request("GET", self._transport.cp_path("agents", "by-name", name))
        return Agent.model_validate(data)

    def update(
        self,
        agent_id: str,
        *,
        name: str | None = None,
        spec: Mapping[str, Any] | None = None,
        workflow_id: str | None = None,
        extra: Mapping[str, Any] | None = None,
    ) -> Agent:
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("agents", agent_id),
            json=merge_extra(
                compact({"name": name, "spec": spec, "workflow_id": workflow_id}), extra
            ),
        )
        return Agent.model_validate(data)

    def delete(self, agent_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("agents", agent_id))

    def publish(self, agent_id: str) -> Agent:
        data = self._transport.request(
            "POST", self._transport.cp_path("agents", agent_id, "publish")
        )
        return Agent.model_validate(data)

    def archive(self, agent_id: str) -> Agent:
        data = self._transport.request(
            "POST", self._transport.cp_path("agents", agent_id, "archive")
        )
        return Agent.model_validate(data)

    def dry_run(self, *, spec: Mapping[str, Any], input: str) -> dict[str, Any]:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("agents", "dry-run"),
            json={"spec": spec, "input": input},
        )
        return data or {}

    def run(self, agent_id: str, *, input: str) -> dict[str, Any]:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("agents", agent_id, "run"),
            json={"input": input},
        )
        return data or {}


class AsyncAgents:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        spec: Mapping[str, Any] | None = None,
        workflow_id: str | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Agent:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("agents"),
            json=_create_body(name=name, spec=spec, workflow_id=workflow_id, extra=extra),
            idempotency_key=idempotency_key,
        )
        return Agent.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
        workflow_id: str | None = None,
    ) -> AsyncPage[Agent]:
        async def fetch(token: str | None) -> RawPage[Agent]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("agents"),
                params=page_params(limit, token, workflow_id=workflow_id),
            )
            return RawPage.from_response(data or {}, Agent.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, agent_id: str) -> Agent:
        data = await self._transport.request("GET", self._transport.cp_path("agents", agent_id))
        return Agent.model_validate(data)

    async def get_by_name(self, name: str) -> Agent:
        data = await self._transport.request(
            "GET", self._transport.cp_path("agents", "by-name", name)
        )
        return Agent.model_validate(data)

    async def update(
        self,
        agent_id: str,
        *,
        name: str | None = None,
        spec: Mapping[str, Any] | None = None,
        workflow_id: str | None = None,
        extra: Mapping[str, Any] | None = None,
    ) -> Agent:
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("agents", agent_id),
            json=merge_extra(
                compact({"name": name, "spec": spec, "workflow_id": workflow_id}), extra
            ),
        )
        return Agent.model_validate(data)

    async def delete(self, agent_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("agents", agent_id))

    async def publish(self, agent_id: str) -> Agent:
        data = await self._transport.request(
            "POST", self._transport.cp_path("agents", agent_id, "publish")
        )
        return Agent.model_validate(data)

    async def archive(self, agent_id: str) -> Agent:
        data = await self._transport.request(
            "POST", self._transport.cp_path("agents", agent_id, "archive")
        )
        return Agent.model_validate(data)

    async def dry_run(self, *, spec: Mapping[str, Any], input: str) -> dict[str, Any]:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("agents", "dry-run"),
            json={"spec": spec, "input": input},
        )
        return data or {}

    async def run(self, agent_id: str, *, input: str) -> dict[str, Any]:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("agents", agent_id, "run"),
            json={"input": input},
        )
        return data or {}
