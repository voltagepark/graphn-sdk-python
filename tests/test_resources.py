"""GA coverage for every first-party resource wrapper.

These tests pin HTTP method, host, and path so a generated-client
routing mistake (control plane vs gateway vs storage) cannot ship.
"""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from graphn import AsyncClient, Client
from tests.conftest import GATEWAY_URL, STORAGE_URL, cp_url, gw_url, inference_url_for


def _ts() -> str:
    return "2026-08-15T00:00:00Z"


def _agent(**overrides: object) -> dict[str, object]:
    body: dict[str, object] = {
        "id": "ag_01",
        "workspace_id": "ws_test",
        "name": "bot",
        "spec": {"instructions": "hi", "model": "qwen3-80b", "mcp_tools": []},
        "created_at": _ts(),
        "updated_at": _ts(),
    }
    body.update(overrides)
    return body


def test_client_exposes_platform_resources(client: Client) -> None:
    for name in (
        "agents",
        "functions",
        "mcp_servers",
        "workflows",
        "executions",
        "triggers",
        "knowledgebases",
        "imported_models",
        "organizations",
        "workspaces",
        "api_keys",
        "blueprints",
        "storages",
        "batch",
        "custom_models",
        "secrets",
        "chat",
        "models",
        "tts",
    ):
        assert hasattr(client, name), name


def test_agent_create_list_publish(client: Client, respx_mock: respx.MockRouter) -> None:
    create = respx_mock.post(cp_url("agents")).mock(return_value=httpx.Response(201, json=_agent()))
    respx_mock.get(cp_url("agents")).mock(
        return_value=httpx.Response(200, json={"items": [_agent()], "count": 1})
    )
    respx_mock.post(cp_url("agents/ag_01/publish")).mock(
        return_value=httpx.Response(200, json=_agent())
    )

    created = client.agents.create(name="bot", spec={"instructions": "hi", "model": "qwen3-80b"})
    page = client.agents.list()
    client.agents.publish(created.id)

    assert json.loads(create.calls.last.request.content)["name"] == "bot"
    assert [a.id for a in page] == ["ag_01"]


def test_function_create_and_test(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("functions")).mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "fn_01",
                "workspace_id": "ws_test",
                "name": "double",
                "spec": {"type": "custom"},
                "created_at": _ts(),
                "updated_at": _ts(),
            },
        )
    )
    respx_mock.post(cp_url("functions/fn_01/test")).mock(
        return_value=httpx.Response(200, json={"success": True, "output": 4})
    )

    fn = client.functions.create(name="double", files={"main.py": "def main(x): return x*2"})
    result = client.functions.test(fn.id, input={"x": 2})
    assert result.success is True
    assert result.output == 4


def test_mcp_server_create(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("mcp-servers")).mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "mcp_01",
                "workspace_id": "ws_test",
                "name": "github",
                "spec": {"type": "remote"},
                "created_at": _ts(),
                "updated_at": _ts(),
            },
        )
    )
    server = client.mcp_servers.create(name="github", type="remote")
    assert server.id == "mcp_01"


def test_trigger_create(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("triggers")).mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "trg_01",
                "workspace_id": "ws_test",
                "workflow_id": "wf_01",
                "name": "hourly",
                "enabled": True,
                "cron_schedule": "0 * * * *",
                "created_at": _ts(),
                "updated_at": _ts(),
            },
        )
    )
    trigger = client.triggers.create(name="hourly", workflow_id="wf_01", cron_schedule="0 * * * *")
    assert trigger.id == "trg_01"


def test_organizations_list_is_unscoped(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.get("https://api.graphn.test/v1/organizations").mock(
        return_value=httpx.Response(
            200,
            json={
                "items": [
                    {
                        "id": "org_01",
                        "name": "Acme",
                        "slug": "acme",
                        "type": "team",
                        "owner_id": "user_01",
                        "created_at": _ts(),
                        "updated_at": _ts(),
                    }
                ],
                "count": 1,
            },
        )
    )
    page = client.organizations.list()
    assert route.called
    assert [o.id for o in page] == ["org_01"]


def test_workspaces_create_uses_org_path(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post("https://api.graphn.test/v1/org_01/workspaces").mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "ws_new",
                "organization_id": "org_01",
                "name": "prod",
                "owner_id": "user_01",
                "created_at": _ts(),
                "updated_at": _ts(),
            },
        )
    )
    ws = client.workspaces.create("org_01", name="prod")
    assert route.called
    assert ws.id == "ws_new"


def test_api_keys_create_returns_raw_key(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("api-keys")).mock(
        return_value=httpx.Response(
            201,
            json={
                "key": "gn_secret",
                "key_id": "key_01",
                "workspace_id": "ws_test",
                "description": "ci",
                "created_at": _ts(),
            },
        )
    )
    created = client.api_keys.create(description="ci")
    assert created.key == "gn_secret"


def test_blueprints_list_is_unscoped(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.get("https://api.graphn.test/v1/blueprints").mock(
        return_value=httpx.Response(
            200, json={"items": [{"id": "bp_01", "name": "qa"}], "count": 1}
        )
    )
    page = client.blueprints.list()
    assert route.called
    assert [b.id for b in page] == ["bp_01"]


def test_storages_list_and_s3_put(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.get(cp_url("storages")).mock(
        return_value=httpx.Response(
            200, json={"items": [{"name": "artifacts", "status": "active"}], "total": 1}
        )
    )
    put = respx_mock.put(f"{STORAGE_URL}/artifacts/out.bin").mock(
        return_value=httpx.Response(200, content=b"")
    )

    page = client.storages.list()
    assert [s.name for s in page] == ["artifacts"]
    client.storages.put_object("artifacts", "out.bin", b"abc")
    assert put.called
    assert put.calls.last.request.content == b"abc"


def test_batch_create_hits_gateway(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(gw_url("wf_01/batch")).mock(
        return_value=httpx.Response(
            202,
            json={
                "id": "019d4c84-b174-75c2-b42f-2f902dc39c95",
                "status": "admitted",
                "created_at": _ts(),
                "request_counts": {"total": 1, "completed": 0, "failed": 0, "canceled": 0},
            },
        )
    )
    batch = client.batch.create("wf_01", inputs=[{"input": {"q": "a"}}])
    assert route.called
    assert batch.status == "admitted"
    assert not str(route.calls.last.request.url).startswith("https://api.graphn.test")


def test_execution_cancel_hits_gateway(client: Client, respx_mock: respx.MockRouter) -> None:
    op_id = "019d4c84-b174-75c2-b42f-2f902dc39c95"
    route = respx_mock.delete(gw_url(f"wf_01/async/{op_id}")).mock(
        return_value=httpx.Response(
            200, json={"id": op_id, "status": "canceled", "created_at": _ts()}
        )
    )
    client.executions.cancel("wf_01", op_id)
    assert route.called
    assert str(route.calls.last.request.url).startswith(GATEWAY_URL)


def test_knowledgebase_create(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("knowledgebases")).mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "kb_01",
                "name": "docs",
                "workspace_id": "ws_test",
                "status": "ready",
                "created_at": _ts(),
                "updated_at": _ts(),
            },
        )
    )
    kb = client.knowledgebases.create(name="docs")
    assert kb.id == "kb_01"


def test_exec_prefix_stays_on_control_plane(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.get(cp_url("executions/exec_01")).mock(
        return_value=httpx.Response(200, json={"id": "exec_01", "status": "running"})
    )
    client.executions.get("exec_01")
    assert route.called


def test_tts_synthesize_hits_inference_host(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(inference_url_for("v1/tts")).mock(
        return_value=httpx.Response(200, content=b"ID3fake")
    )
    audio = client.tts.synthesize(model="orpheus-tts", text="hi", speaker="tara")
    assert route.called
    assert audio == b"ID3fake"
    assert str(route.calls.last.request.url).startswith("https://inference.graphn.test")


@pytest.mark.asyncio
async def test_async_workflow_create(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    respx_mock.post(cp_url("workflows")).mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "wf_01",
                "workspace_id": "ws_test",
                "name": "qa",
                "created_at": _ts(),
                "updated_at": _ts(),
            },
        )
    )
    wf = await async_client.workflows.create(name="qa", dsl="name: qa\n")
    assert wf.id == "wf_01"
