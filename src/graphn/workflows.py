"""Workflow CRUD, bundle, publish, versions, run, and test."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._dsl import dsl_resource_refs, resource_id_from_ref
from graphn._exceptions import NotFoundError
from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact, merge_extra, page_params


class Workflow(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    workspace_id: str
    name: str
    created_at: datetime
    updated_at: datetime
    dsl: str | None = None
    owner_id: str | None = None
    description: str | None = None
    published_version_id: str | None = None
    has_unpublished_changes: bool | None = None
    status: str | None = None


class WorkflowVersionDetail(BaseModel):
    """POST /workflows/{id}/publish returns a version snapshot, not the workflow."""

    model_config = ConfigDict(extra="allow", frozen=True)

    version_id: str
    version_number: int
    created_at: datetime
    snapshot_id: str | None = None
    message: str | None = None
    dsl: str | None = None
    resource_pins: dict[str, Any] | None = None
    resource_snapshots: dict[str, Any] | None = None


class WorkflowRunResult(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    execution_id: str | None = None
    status: str | None = None
    output: Any = None
    error: str | None = None
    duration_ms: int | None = None


_BUNDLE_PATHS = {
    "agents": "agents",
    "functions": "functions",
    "mcp_servers": "mcp-servers",
}


def _bundle_entry(data: Mapping[str, Any], local_name: str) -> dict[str, Any]:
    entry: dict[str, Any] = {"id": data.get("id"), "name": local_name}
    if "spec" in data:
        entry["spec"] = data["spec"]
    return entry


def _extract_resource_list(bundle: Mapping[str, Any], key: str) -> list[dict[str, Any]]:
    items = bundle.get(key)
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def _merge_resource_specs(
    current: list[dict[str, Any]], changes: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Same name-keyed merge as CLI ``mergeBundleSave`` — keep unrelated bundle entries."""

    current_by_name = {
        name: row for row in current if isinstance((name := row.get("name")), str) and name
    }
    change_names: set[str] = set()
    result: list[dict[str, Any]] = []
    for change in changes:
        change_name = change.get("name")
        if not isinstance(change_name, str) or not change_name:
            result.append(dict(change))
            continue
        change_names.add(change_name)
        existing = current_by_name.get(change_name)
        if existing is None:
            result.append(dict(change))
            continue
        merged = {**existing, **{k: v for k, v in change.items() if k != "spec"}}
        existing_spec = existing.get("spec") if isinstance(existing.get("spec"), dict) else {}
        change_spec = change.get("spec") if isinstance(change.get("spec"), dict) else {}
        merged["spec"] = {
            **existing_spec,
            **{k: v for k, v in change_spec.items() if v is not None},
        }
        result.append(merged)
    for row in current:
        name = row.get("name")
        if isinstance(name, str) and name and name not in change_names:
            result.append(row)
    return result


def _merged_bundle_payload(current: Any, changes: Mapping[str, Any]) -> dict[str, Any]:
    payload = dict(changes)
    bundle = current if isinstance(current, dict) else {}
    for key in ("agents", "functions", "mcp_servers"):
        incoming = payload.get(key)
        if not isinstance(incoming, list):
            continue
        payload[key] = _merge_resource_specs(
            _extract_resource_list(bundle, key),
            [entry for entry in incoming if isinstance(entry, dict)],
        )
    return payload


class Workflows:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        dsl: str | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        link_resources: bool = True,
        **fields: Any,
    ) -> Workflow:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("workflows"),
            json=merge_extra(compact({"name": name, "dsl": dsl, **fields}), extra),
            idempotency_key=idempotency_key,
        )
        workflow = Workflow.model_validate(data)
        if link_resources and dsl:
            self._link_dsl(workflow.id, dsl, name=workflow.name)
        return workflow

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[Workflow]:
        def fetch(token: str | None) -> RawPage[Workflow]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("workflows"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, Workflow.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, workflow_id: str) -> Workflow:
        data = self._transport.request("GET", self._transport.cp_path("workflows", workflow_id))
        return Workflow.model_validate(data)

    def get_by_name(self, name: str) -> Workflow:
        data = self._transport.request("GET", self._transport.cp_path("workflows", "by-name", name))
        return Workflow.model_validate(data)

    def update(self, workflow_id: str, **fields: Any) -> Workflow:
        extra = fields.pop("extra", None)
        link_resources = fields.pop("link_resources", True)
        dsl = fields.get("dsl")
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("workflows", workflow_id),
            json=merge_extra(compact(fields), extra),
        )
        workflow = Workflow.model_validate(data)
        if link_resources and isinstance(dsl, str) and dsl:
            self._link_dsl(workflow.id, dsl, name=workflow.name)
        return workflow

    def delete(self, workflow_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("workflows", workflow_id))

    def publish(self, workflow_id: str, *, message: str | None = None) -> WorkflowVersionDetail:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "publish"),
            json=compact({"message": message}),
        )
        return WorkflowVersionDetail.model_validate(data)

    def bundle(self, workflow_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("workflows", workflow_id, "bundle")
            )
            or {}
        )

    def save_bundle(self, workflow_id: str, **fields: Any) -> dict[str, Any]:
        return (
            self._transport.request(
                "PUT",
                self._transport.cp_path("workflows", workflow_id, "bundle"),
                json=compact(fields),
            )
            or {}
        )

    def _link_dsl(self, workflow_id: str, dsl: str, *, name: str | None) -> None:
        refs = dsl_resource_refs(dsl)
        if not any(refs.values()):
            return
        bundle: dict[str, Any] = {"workflow": compact({"name": name, "dsl": dsl})}
        for section, path in _BUNDLE_PATHS.items():
            entries: list[dict[str, Any]] = []
            for local_name, ref in refs[section].items():  # type: ignore[literal-required]
                resource_id = resource_id_from_ref(ref)
                try:
                    if resource_id:
                        data = self._transport.request(
                            "GET", self._transport.cp_path(path, resource_id)
                        )
                    else:
                        data = self._transport.request(
                            "GET", self._transport.cp_path(path, "by-name", local_name)
                        )
                except NotFoundError:
                    continue
                if isinstance(data, dict) and data.get("id"):
                    entries.append(_bundle_entry(data, local_name))
            if entries:
                bundle[section] = entries
        if len(bundle) == 1:
            return
        try:
            current = self.bundle(workflow_id)
        except NotFoundError:
            current = {}
        self.save_bundle(workflow_id, **_merged_bundle_payload(current, bundle))

    def versions(self, workflow_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("workflows", workflow_id, "versions")
            )
            or {}
        )

    def get_version(self, workflow_id: str, version_id: str) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET", self._transport.cp_path("workflows", workflow_id, "versions", version_id)
            )
            or {}
        )

    def restore(self, workflow_id: str, *, version_id: str) -> Workflow:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "restore"),
            json={"version_id": version_id},
        )
        return Workflow.model_validate(data)

    def run(
        self,
        workflow_id: str,
        *,
        input: Mapping[str, Any] | None = None,
        async_execution: bool | None = None,
    ) -> WorkflowRunResult:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "run"),
            json=compact({"input": input, "async_execution": async_execution}),
        )
        return WorkflowRunResult.model_validate(data or {})

    def test(
        self,
        workflow_id: str,
        *,
        input: Mapping[str, Any] | None = None,
    ) -> WorkflowRunResult:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "test"),
            json=compact({"input": input}),
        )
        return WorkflowRunResult.model_validate(data or {})

    def dry_run(self, *, dsl: str, input: Mapping[str, Any] | None = None) -> WorkflowRunResult:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("workflows", "dry-run"),
            json=compact({"dsl": dsl, "input": input}),
        )
        return WorkflowRunResult.model_validate(data or {})


class AsyncWorkflows:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        dsl: str | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        link_resources: bool = True,
        **fields: Any,
    ) -> Workflow:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("workflows"),
            json=merge_extra(compact({"name": name, "dsl": dsl, **fields}), extra),
            idempotency_key=idempotency_key,
        )
        workflow = Workflow.model_validate(data)
        if link_resources and dsl:
            await self._link_dsl(workflow.id, dsl, name=workflow.name)
        return workflow

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[Workflow]:
        async def fetch(token: str | None) -> RawPage[Workflow]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("workflows"),
                params=page_params(limit, token),
            )
            return RawPage.from_response(data or {}, Workflow.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, workflow_id: str) -> Workflow:
        data = await self._transport.request(
            "GET", self._transport.cp_path("workflows", workflow_id)
        )
        return Workflow.model_validate(data)

    async def get_by_name(self, name: str) -> Workflow:
        data = await self._transport.request(
            "GET", self._transport.cp_path("workflows", "by-name", name)
        )
        return Workflow.model_validate(data)

    async def update(self, workflow_id: str, **fields: Any) -> Workflow:
        extra = fields.pop("extra", None)
        link_resources = fields.pop("link_resources", True)
        dsl = fields.get("dsl")
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("workflows", workflow_id),
            json=merge_extra(compact(fields), extra),
        )
        workflow = Workflow.model_validate(data)
        if link_resources and isinstance(dsl, str) and dsl:
            await self._link_dsl(workflow.id, dsl, name=workflow.name)
        return workflow

    async def delete(self, workflow_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("workflows", workflow_id))

    async def publish(
        self, workflow_id: str, *, message: str | None = None
    ) -> WorkflowVersionDetail:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "publish"),
            json=compact({"message": message}),
        )
        return WorkflowVersionDetail.model_validate(data)

    async def bundle(self, workflow_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("workflows", workflow_id, "bundle")
            )
            or {}
        )

    async def save_bundle(self, workflow_id: str, **fields: Any) -> dict[str, Any]:
        return (
            await self._transport.request(
                "PUT",
                self._transport.cp_path("workflows", workflow_id, "bundle"),
                json=compact(fields),
            )
            or {}
        )

    async def _link_dsl(self, workflow_id: str, dsl: str, *, name: str | None) -> None:
        refs = dsl_resource_refs(dsl)
        if not any(refs.values()):
            return
        bundle: dict[str, Any] = {"workflow": compact({"name": name, "dsl": dsl})}
        for section, path in _BUNDLE_PATHS.items():
            entries: list[dict[str, Any]] = []
            for local_name, ref in refs[section].items():  # type: ignore[literal-required]
                resource_id = resource_id_from_ref(ref)
                try:
                    if resource_id:
                        data = await self._transport.request(
                            "GET", self._transport.cp_path(path, resource_id)
                        )
                    else:
                        data = await self._transport.request(
                            "GET", self._transport.cp_path(path, "by-name", local_name)
                        )
                except NotFoundError:
                    continue
                if isinstance(data, dict) and data.get("id"):
                    entries.append(_bundle_entry(data, local_name))
            if entries:
                bundle[section] = entries
        if len(bundle) == 1:
            return
        try:
            current = await self.bundle(workflow_id)
        except NotFoundError:
            current = {}
        await self.save_bundle(workflow_id, **_merged_bundle_payload(current, bundle))

    async def versions(self, workflow_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("workflows", workflow_id, "versions")
            )
            or {}
        )

    async def get_version(self, workflow_id: str, version_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET", self._transport.cp_path("workflows", workflow_id, "versions", version_id)
            )
            or {}
        )

    async def restore(self, workflow_id: str, *, version_id: str) -> Workflow:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "restore"),
            json={"version_id": version_id},
        )
        return Workflow.model_validate(data)

    async def run(
        self,
        workflow_id: str,
        *,
        input: Mapping[str, Any] | None = None,
        async_execution: bool | None = None,
    ) -> WorkflowRunResult:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "run"),
            json=compact({"input": input, "async_execution": async_execution}),
        )
        return WorkflowRunResult.model_validate(data or {})

    async def test(
        self,
        workflow_id: str,
        *,
        input: Mapping[str, Any] | None = None,
    ) -> WorkflowRunResult:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("workflows", workflow_id, "test"),
            json=compact({"input": input}),
        )
        return WorkflowRunResult.model_validate(data or {})

    async def dry_run(
        self, *, dsl: str, input: Mapping[str, Any] | None = None
    ) -> WorkflowRunResult:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("workflows", "dry-run"),
            json=compact({"dsl": dsl, "input": input}),
        )
        return WorkflowRunResult.model_validate(data or {})
