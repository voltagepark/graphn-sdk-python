"""Ergonomic secrets resource.

Wraps the workspace-scoped ``/v1/{workspaceId}/secrets`` endpoints.
The plaintext ``value`` is write-only; responses only include the
``value_preview`` field.
"""

from __future__ import annotations

from typing import Any

from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn.secrets.types import Secret


def _list_params(limit: int | None, continue_token: str | None) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if continue_token is not None:
        params["continue_token"] = continue_token
    return params


def _build_create_body(
    *,
    name: str,
    value: str,
    provider_id: str | None,
    field_name: str | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"name": name, "value": value}
    if provider_id is not None:
        body["provider_id"] = provider_id
    if field_name is not None:
        body["field_name"] = field_name
    return body


class Secrets:
    """Synchronous secrets resource."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        value: str,
        provider_id: str | None = None,
        field_name: str | None = None,
        idempotency_key: str | None = None,
    ) -> Secret:
        data = self._transport.request(
            "POST",
            self._transport.cp_path("secrets"),
            json=_build_create_body(
                name=name,
                value=value,
                provider_id=provider_id,
                field_name=field_name,
            ),
            idempotency_key=idempotency_key,
        )
        return Secret.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[Secret]:
        def fetch(token: str | None) -> RawPage[Secret]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("secrets"),
                params=_list_params(limit, token),
            )
            return RawPage.from_response(data or {}, Secret.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def update(self, secret_id: str, *, value: str) -> Secret:
        data = self._transport.request(
            "PUT",
            self._transport.cp_path("secrets", secret_id),
            json={"value": value},
        )
        return Secret.model_validate(data)

    def delete(self, secret_id: str) -> None:
        self._transport.request("DELETE", self._transport.cp_path("secrets", secret_id))


class AsyncSecrets:
    """Asynchronous secrets resource."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        value: str,
        provider_id: str | None = None,
        field_name: str | None = None,
        idempotency_key: str | None = None,
    ) -> Secret:
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("secrets"),
            json=_build_create_body(
                name=name,
                value=value,
                provider_id=provider_id,
                field_name=field_name,
            ),
            idempotency_key=idempotency_key,
        )
        return Secret.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[Secret]:
        async def fetch(token: str | None) -> RawPage[Secret]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("secrets"),
                params=_list_params(limit, token),
            )
            return RawPage.from_response(data or {}, Secret.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def update(self, secret_id: str, *, value: str) -> Secret:
        data = await self._transport.request(
            "PUT",
            self._transport.cp_path("secrets", secret_id),
            json={"value": value},
        )
        return Secret.model_validate(data)

    async def delete(self, secret_id: str) -> None:
        await self._transport.request("DELETE", self._transport.cp_path("secrets", secret_id))
