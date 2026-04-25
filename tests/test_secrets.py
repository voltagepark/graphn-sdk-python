"""Tests for the secrets resource."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from graphn import AsyncClient, Client
from tests.conftest import cp_url


def _secret_payload(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "sec_01",
        "workspace_id": "ws_test",
        "name": "hf-token",
        "value_preview": "hf_xx",
        "created_at": "2026-04-24T00:00:00Z",
        "updated_at": "2026-04-24T00:00:00Z",
    }
    base.update(overrides)
    return base


def test_create_sends_value(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(cp_url("secrets")).mock(
        return_value=httpx.Response(201, json=_secret_payload())
    )

    secret = client.secrets.create(name="hf-token", value="hf_supersecret")

    assert json.loads(route.calls.last.request.content) == {
        "name": "hf-token",
        "value": "hf_supersecret",
    }
    assert secret.id == "sec_01"
    assert secret.value_preview == "hf_xx"


def test_list_uses_count_field(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.get(cp_url("secrets")).mock(
        return_value=httpx.Response(
            200,
            json={"items": [_secret_payload()], "count": 1},
        )
    )

    page = client.secrets.list()
    assert [s.id for s in page] == ["sec_01"]
    assert page.has_more is False


def test_update_only_sends_value(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.put(cp_url("secrets/sec_01")).mock(
        return_value=httpx.Response(200, json=_secret_payload(value_preview="ne"))
    )

    secret = client.secrets.update("sec_01", value="new-value")

    assert json.loads(route.calls.last.request.content) == {"value": "new-value"}
    assert secret.value_preview == "ne"


def test_delete_returns_none(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.delete(cp_url("secrets/sec_01")).mock(return_value=httpx.Response(204))

    assert client.secrets.delete("sec_01") is None
    assert route.called


@pytest.mark.asyncio
async def test_async_secret_crud(async_client: AsyncClient, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("secrets")).mock(
        return_value=httpx.Response(201, json=_secret_payload())
    )
    respx_mock.delete(cp_url("secrets/sec_01")).mock(return_value=httpx.Response(204))

    secret = await async_client.secrets.create(name="hf-token", value="hf_xx")
    assert secret.id == "sec_01"
    await async_client.secrets.delete("sec_01")
