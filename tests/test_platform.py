"""Tests for workflow / execution / knowledge-base wrappers."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from graphn import APIError, Client
from tests.conftest import GATEWAY_URL, cp_url, gw_url


def _workflow_payload(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "wf_01",
        "workspace_id": "ws_test",
        "name": "qa",
        "dsl": "name: qa\nsteps: []",
        "created_at": "2026-08-15T00:00:00Z",
        "updated_at": "2026-08-15T00:00:00Z",
    }
    base.update(overrides)
    return base


def test_workflow_create_publish_run(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("workflows")).mock(
        return_value=httpx.Response(201, json=_workflow_payload())
    )
    respx_mock.post(cp_url("workflows/wf_01/publish")).mock(
        return_value=httpx.Response(
            200,
            json={
                "version_id": "wfv_01",
                "version_number": 1,
                "created_at": "2026-08-15T00:00:00Z",
            },
        )
    )
    route = respx_mock.post(cp_url("workflows/wf_01/run")).mock(
        return_value=httpx.Response(
            200,
            json={"execution_id": "exec_01", "status": "completed", "output": {"ok": True}},
        )
    )

    wf = client.workflows.create(name="qa", dsl="name: qa\nsteps: []")
    published = client.workflows.publish(wf.id)
    run = client.workflows.run(wf.id, input={"q": "hello"})

    assert published.version_id == "wfv_01"

    assert json.loads(route.calls.last.request.content) == {"input": {"q": "hello"}}
    assert run.execution_id == "exec_01"
    assert run.status == "completed"


def test_workflow_create_auto_links_dsl_functions(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    dsl = 'name: qa\nfunctions:\n  echo: "res://functions/fn_01"\n'
    respx_mock.post(cp_url("workflows")).mock(
        return_value=httpx.Response(201, json=_workflow_payload(dsl=dsl))
    )
    respx_mock.get(cp_url("functions/fn_01")).mock(
        return_value=httpx.Response(
            200,
            json={
                "id": "fn_01",
                "name": "echo",
                "workspace_id": "ws_test",
                "spec": {"source": "print(1)"},
                "created_at": "2026-08-15T00:00:00Z",
                "updated_at": "2026-08-15T00:00:00Z",
            },
        )
    )
    respx_mock.get(cp_url("workflows/wf_01/bundle")).mock(
        return_value=httpx.Response(404, json={"code": "NOT_FOUND", "message": "missing"})
    )
    save = respx_mock.put(cp_url("workflows/wf_01/bundle")).mock(
        return_value=httpx.Response(200, json={"validation": {"valid": True}})
    )

    wf = client.workflows.create(name="qa", dsl=dsl)

    assert wf.id == "wf_01"
    assert save.called
    body = json.loads(save.calls.last.request.content)
    assert body["workflow"]["dsl"] == dsl
    assert body["functions"] == [{"id": "fn_01", "name": "echo", "spec": {"source": "print(1)"}}]


def test_workflow_create_skips_missing_resources(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    dsl = "name: qa\nfunctions:\n  missing:\n"
    respx_mock.post(cp_url("workflows")).mock(
        return_value=httpx.Response(201, json=_workflow_payload(dsl=dsl))
    )
    respx_mock.get(cp_url("functions/by-name/missing")).mock(
        return_value=httpx.Response(404, json={"code": "NOT_FOUND", "message": "gone"})
    )
    save = respx_mock.put(cp_url("workflows/wf_01/bundle")).mock(
        return_value=httpx.Response(200, json={})
    )

    client.workflows.create(name="qa", dsl=dsl)
    assert not save.called


def test_execution_wait_polls_until_completed(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.get(cp_url("executions/exec_01")).mock(
        side_effect=[
            httpx.Response(200, json={"id": "exec_01", "status": "running"}),
            httpx.Response(
                200,
                json={"id": "exec_01", "status": "completed", "output": {"n": 1}},
            ),
        ]
    )

    result = client.executions.wait("exec_01", timeout=5, poll_interval=0)
    assert result.status == "completed"
    assert result.output == {"n": 1}


def test_execution_wait_raises_on_failed(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.get(cp_url("executions/exec_01")).mock(
        return_value=httpx.Response(
            200, json={"id": "exec_01", "status": "failed", "error": "boom"}
        )
    )

    with pytest.raises(APIError, match="boom"):
        client.executions.wait("exec_01", timeout=5, poll_interval=0)


def test_execution_submit_hits_gateway(client: Client, respx_mock: respx.MockRouter) -> None:
    op_id = "019d4c84-b174-75c2-b42f-2f902dc39c95"
    route = respx_mock.post(gw_url("wf_01/async")).mock(
        return_value=httpx.Response(
            202,
            json={"id": op_id, "status": "admitted", "created_at": "2026-08-15T00:00:00Z"},
        )
    )
    run = client.executions.submit("wf_01", input={"text": "ping"})
    assert route.called
    assert run.id == op_id
    assert str(route.calls.last.request.url).startswith(GATEWAY_URL)


def test_execution_uuid_hits_gateway(client: Client, respx_mock: respx.MockRouter) -> None:
    op_id = "019d4c84-b174-75c2-b42f-2f902dc39c95"
    route = respx_mock.get(f"{GATEWAY_URL}/v1/ws_test/executions/{op_id}").mock(
        return_value=httpx.Response(200, json={"id": op_id, "status": "succeeded"})
    )

    execution = client.executions.get(op_id)
    assert route.called
    assert execution.status == "succeeded"


def test_knowledgebase_list_accepts_bare_array(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("knowledgebases")).mock(
        return_value=httpx.Response(
            200,
            json=[
                {
                    "id": "kb_01",
                    "name": "docs",
                    "workspace_id": "ws_test",
                    "status": "ready",
                    "created_at": "2026-08-15T00:00:00Z",
                    "updated_at": "2026-08-15T00:00:00Z",
                }
            ],
        )
    )
    page = client.knowledgebases.list()
    assert [kb.id for kb in page] == ["kb_01"]


def test_knowledgebase_search(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("knowledgebases/kb_01/search")).mock(
        return_value=httpx.Response(
            200,
            json={
                "query": "hello",
                "total": 1,
                "results": [
                    {
                        "id": "chunk_1",
                        "text": "hello world",
                        "score": 0.9,
                        "document_id": "doc_1",
                        "source": "notes.txt",
                    }
                ],
            },
        )
    )

    hits = client.knowledgebases.search("kb_01", query="hello")
    assert hits.total == 1
    assert hits.results[0].text == "hello world"


def test_imported_model_create(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("imported-models")).mock(
        return_value=httpx.Response(
            201,
            json={
                "id": "im_01",
                "name": "my-gpt",
                "display_name": "My GPT",
                "workspace_id": "ws_test",
                "endpoint": "https://api.example.com/v1",
                "model_id": "gpt-4o",
                "status": "ready",
                "created_at": "2026-08-15T00:00:00Z",
                "updated_at": "2026-08-15T00:00:00Z",
            },
        )
    )

    model = client.imported_models.create(
        name="my-gpt",
        display_name="My GPT",
        endpoint="https://api.example.com/v1",
        model_id="gpt-4o",
    )
    assert model.id == "im_01"


def test_ingest_wait(client: Client, respx_mock: respx.MockRouter) -> None:
    summary = {
        "total": 1,
        "pending": 0,
        "running": 0,
        "succeeded": 1,
        "failed": 0,
        "skipped": 0,
    }
    respx_mock.get(cp_url("knowledgebases/kb_01/ingest/job_01")).mock(
        side_effect=[
            httpx.Response(
                200,
                json={
                    "id": "job_01",
                    "kb_id": "kb_01",
                    "status": "running",
                    "summary": {**summary, "running": 1, "succeeded": 0},
                    "created_at": "2026-08-15T00:00:00Z",
                },
            ),
            httpx.Response(
                200,
                json={
                    "id": "job_01",
                    "kb_id": "kb_01",
                    "status": "succeeded",
                    "summary": summary,
                    "created_at": "2026-08-15T00:00:00Z",
                },
            ),
        ]
    )

    job = client.knowledgebases.wait_ingest("kb_01", "job_01", timeout=5, poll_interval=0)
    assert job.status == "succeeded"
