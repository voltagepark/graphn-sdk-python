"""Poll workflow executions on the control plane or gateway.

``exec_`` / ``test_`` ids hit the control plane. UUID operation ids from
async/batch submit hit the gateway. :meth:`Executions.wait` polls until
a terminal status.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict

from graphn._exceptions import APIError
from graphn._poll import apoll_until, poll_until
from graphn._transport import AsyncTransport, SyncTransport
from graphn._util import compact

_TERMINAL_STATUSES = frozenset(
    {"completed", "succeeded", "failed", "cancelled", "canceled", "error"}
)
_FAILED_STATUSES = frozenset({"failed", "error"})
_DEFAULT_WAIT_TIMEOUT_SECONDS = 600.0
_DEFAULT_POLL_INTERVAL_SECONDS = 2.0


class Execution(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str | None = None
    execution_id: str | None = None
    status: str | None = None
    output: Any = None
    error: Any = None
    created_at: str | None = None
    completed_at: str | None = None
    workflow_id: str | None = None

    @property
    def resolved_id(self) -> str:
        return self.id or self.execution_id or ""


def _is_gateway_id(execution_id: str) -> bool:
    if execution_id.startswith(("exec_", "test_")):
        return False
    try:
        uuid.UUID(execution_id)
    except ValueError:
        return False
    return True


def _raise_if_failed(execution: Execution) -> Execution:
    if (execution.status or "") in _FAILED_STATUSES:
        message = execution.error
        if not isinstance(message, str):
            message = f"execution {execution.resolved_id} ended with status {execution.status!r}"
        raise APIError(
            str(message),
            status_code=0,
            code="execution_failed",
            details={"execution_id": execution.resolved_id, "status": execution.status},
        )
    return execution


class Executions:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def _get_path(self, execution_id: str) -> str:
        if _is_gateway_id(execution_id):
            return self._transport.gw_url("executions", execution_id)
        return self._transport.cp_path("executions", execution_id)

    def list(
        self,
        *,
        workflow_id: str,
        limit: int | None = None,
        page: int | None = None,
    ) -> dict[str, Any]:
        return (
            self._transport.request(
                "GET",
                self._transport.cp_path("executions"),
                params=compact({"workflow_id": workflow_id, "limit": limit, "page": page}),
            )
            or {}
        )

    def get(self, execution_id: str) -> Execution:
        data = self._transport.request("GET", self._get_path(execution_id))
        return Execution.model_validate(data or {})

    def submit(
        self,
        workflow_id: str,
        *,
        input: Mapping[str, Any] | None = None,
        extra: Mapping[str, Any] | None = None,
    ) -> Execution:
        """Submit an async run on the gateway (CLI ``wf run --mode async``)."""

        body: dict[str, Any] = compact({"input": input})
        if extra:
            body.update(dict(extra))
        data = self._transport.request(
            "POST",
            self._transport.gw_url(workflow_id, "async"),
            json=body,
        )
        return Execution.model_validate(data or {})

    def cancel(self, workflow_id: str, operation_id: str) -> dict[str, Any]:
        """Cancel a gateway async run (UUID operation id)."""

        return (
            self._transport.request(
                "DELETE",
                self._transport.gw_url(workflow_id, "async", operation_id),
            )
            or {}
        )

    def wait(
        self,
        execution_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> Execution:
        def fetch() -> Execution:
            return self.get(execution_id)

        execution = poll_until(
            fetch,
            done=lambda item: (item.status or "") in _TERMINAL_STATUSES,
            timeout=timeout,
            interval=poll_interval,
            timeout_message=lambda item: (
                f"execution {execution_id} did not finish within {timeout:.0f}s "
                f"(last status: {item.status!r})"
            ),
        )
        return _raise_if_failed(execution)


class AsyncExecutions:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    def _get_path(self, execution_id: str) -> str:
        if _is_gateway_id(execution_id):
            return self._transport.gw_url("executions", execution_id)
        return self._transport.cp_path("executions", execution_id)

    async def list(
        self,
        *,
        workflow_id: str,
        limit: int | None = None,
        page: int | None = None,
    ) -> dict[str, Any]:
        return (
            await self._transport.request(
                "GET",
                self._transport.cp_path("executions"),
                params=compact({"workflow_id": workflow_id, "limit": limit, "page": page}),
            )
            or {}
        )

    async def get(self, execution_id: str) -> Execution:
        data = await self._transport.request("GET", self._get_path(execution_id))
        return Execution.model_validate(data or {})

    async def submit(
        self,
        workflow_id: str,
        *,
        input: Mapping[str, Any] | None = None,
        extra: Mapping[str, Any] | None = None,
    ) -> Execution:
        body: dict[str, Any] = compact({"input": input})
        if extra:
            body.update(dict(extra))
        data = await self._transport.request(
            "POST",
            self._transport.gw_url(workflow_id, "async"),
            json=body,
        )
        return Execution.model_validate(data or {})

    async def cancel(self, workflow_id: str, operation_id: str) -> dict[str, Any]:
        return (
            await self._transport.request(
                "DELETE",
                self._transport.gw_url(workflow_id, "async", operation_id),
            )
            or {}
        )

    async def wait(
        self,
        execution_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> Execution:
        async def fetch() -> Execution:
            return await self.get(execution_id)

        execution = await apoll_until(
            fetch,
            done=lambda item: (item.status or "") in _TERMINAL_STATUSES,
            timeout=timeout,
            interval=poll_interval,
            timeout_message=lambda item: (
                f"execution {execution_id} did not finish within {timeout:.0f}s "
                f"(last status: {item.status!r})"
            ),
        )
        return _raise_if_failed(execution)
