"""Tests for the custom-models resource (sync + async)."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from graphn import (
    APIError,
    AsyncClient,
    Client,
    NotFoundError,
    ValidationError,
)
from tests.conftest import cp_url


def _model_payload(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "cm_01",
        "name": "my-llama",
        "workspace_id": "ws_test",
        "status": "pending",
        "weight_source": "huggingface",
        "huggingface_model_id": "meta-llama/Llama-3-8B",
        "gpu_count": 1,
        "capabilities": ["tool_calling"],
        "min_replicas": 0,
        "max_replicas": 1,
        "cooldown_seconds": 600,
        "gpu_memory_utilization": 0.9,
        "created_at": "2026-04-24T00:00:00Z",
        "updated_at": "2026-04-24T00:00:00Z",
    }
    base.update(overrides)
    return base


def test_create_sends_workspace_path_and_body(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(201, json=_model_payload())
    )

    model = client.custom_models.create(
        name="my-llama",
        huggingface_model_id="meta-llama/Llama-3-8B",
        hf_token_secret_id="sec_1",
        capabilities=["tool_calling"],
    )

    assert route.called
    sent = json.loads(route.calls.last.request.content)
    assert sent == {
        "name": "my-llama",
        "weight_source": "huggingface",
        "huggingface_model_id": "meta-llama/Llama-3-8B",
        "hf_token_secret_id": "sec_1",
        "capabilities": ["tool_calling"],
    }
    headers = route.calls.last.request.headers
    assert headers["Authorization"] == "Bearer gn_test_token"
    assert headers["X-Workspace-Id"] == "ws_test"
    assert "X-Request-Id" in headers
    assert model.id == "cm_01"
    assert model.status == "pending"


def test_create_attaches_idempotency_key(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(201, json=_model_payload())
    )

    client.custom_models.create(
        name="my-llama",
        huggingface_model_id="meta-llama/Llama-3-8B",
        idempotency_key="abc-123",
    )

    assert route.calls.last.request.headers["Idempotency-Key"] == "abc-123"


def test_get_returns_typed_model(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("custom-models/cm_01")).mock(
        return_value=httpx.Response(200, json=_model_payload(status="ready"))
    )

    model = client.custom_models.get("cm_01")
    assert model.status == "ready"


def test_get_404_maps_to_not_found(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("custom-models/missing")).mock(
        return_value=httpx.Response(
            404,
            json={"code": "not_found", "message": "no such model"},
        )
    )

    with pytest.raises(NotFoundError) as exc_info:
        client.custom_models.get("missing")
    assert exc_info.value.code == "not_found"
    assert exc_info.value.message == "no such model"


def test_validate_400_raises_validation_error(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.post(cp_url("custom-models/validate")).mock(
        return_value=httpx.Response(
            422,
            json={"code": "validation_error", "message": "bad request"},
        )
    )

    with pytest.raises(ValidationError):
        client.custom_models.validate(huggingface_model_id="meta-llama/Llama-3-8B")


def test_wait_until_ready_polls_until_ready(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    sleeps: list[float] = []
    monkeypatch.setattr("graphn.custom_models.resource.time.sleep", sleeps.append)

    route = respx_mock.post(cp_url("custom-models/cm_01/refresh"))
    route.mock(
        side_effect=[
            httpx.Response(200, json=_model_payload(status="pending")),
            httpx.Response(200, json=_model_payload(status="deploying")),
            httpx.Response(200, json=_model_payload(status="ready")),
        ]
    )

    model = client.custom_models.wait_until_ready(
        "cm_01", timeout=60, poll_interval=0.1
    )

    assert model.status == "ready"
    assert route.call_count == 3
    assert len(sleeps) == 2  # one sleep between each non-terminal poll


def test_wait_until_ready_failed_raises(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("graphn.custom_models.resource.time.sleep", lambda _: None)
    respx_mock.post(cp_url("custom-models/cm_01/refresh")).mock(
        return_value=httpx.Response(
            200,
            json=_model_payload(status="failed", error_message="OOM during load"),
        )
    )

    with pytest.raises(APIError) as exc_info:
        client.custom_models.wait_until_ready("cm_01", timeout=10, poll_interval=0.1)
    assert "OOM during load" in str(exc_info.value)
    assert exc_info.value.code == "custom_model_deployment_failed"


def test_wait_until_ready_times_out(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("graphn.custom_models.resource.time.sleep", lambda _: None)
    times = iter([0.0, 0.0, 100.0])
    monkeypatch.setattr(
        "graphn.custom_models.resource.time.monotonic", lambda: next(times)
    )
    respx_mock.post(cp_url("custom-models/cm_01/refresh")).mock(
        return_value=httpx.Response(200, json=_model_payload(status="deploying"))
    )

    with pytest.raises(TimeoutError):
        client.custom_models.wait_until_ready("cm_01", timeout=1, poll_interval=0.1)


def test_list_auto_paginates(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("custom-models")).mock(
        side_effect=[
            httpx.Response(
                200,
                json={
                    "items": [_model_payload(id="cm_1")],
                    "total": 1,
                    "continue_token": "next",
                },
            ),
            httpx.Response(
                200,
                json={
                    "items": [_model_payload(id="cm_2"), _model_payload(id="cm_3")],
                    "total": 2,
                },
            ),
        ]
    )

    page = client.custom_models.list()
    assert page.has_more is True
    ids = [model.id for model in page]
    assert ids == ["cm_1", "cm_2", "cm_3"]


@pytest.mark.asyncio
async def test_async_create_and_list(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(201, json=_model_payload())
    )
    respx_mock.get(cp_url("custom-models")).mock(
        return_value=httpx.Response(
            200,
            json={"items": [_model_payload(id="cm_a")], "total": 1},
        )
    )

    model = await async_client.custom_models.create(
        name="my-llama", huggingface_model_id="meta-llama/Llama-3-8B"
    )
    assert model.id == "cm_01"

    page = await async_client.custom_models.list()
    collected: list[str] = []
    async for m in page:
        collected.append(m.id)
    assert collected == ["cm_a"]


@pytest.mark.parametrize("weight_source", ["s3_presigned", "s3_assume_role"])
def test_create_s3_requires_huggingface_model_id(
    client: Client, respx_mock: respx.MockRouter, weight_source: str
) -> None:
    """S3 imports must include huggingface_model_id (used as served-model-name).

    The validation is client-side and must happen before any HTTP request, so
    no route is registered.
    """
    with pytest.raises(ValidationError) as exc_info:
        client.custom_models.create(
            name="my-s3-model",
            weight_source=weight_source,  # type: ignore[arg-type]
            s3_url="https://example.com/model.tar.gz",
        )
    assert exc_info.value.code == "missing_huggingface_model_id"
    assert "huggingface_model_id is required" in exc_info.value.message
    assert exc_info.value.details == {"weight_source": weight_source}
    assert respx_mock.calls.call_count == 0


def test_create_s3_with_blank_huggingface_model_id_is_rejected(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    with pytest.raises(ValidationError):
        client.custom_models.create(
            name="my-s3-model",
            weight_source="s3_presigned",
            huggingface_model_id="   ",
            s3_url="https://example.com/model.tar.gz",
        )
    assert respx_mock.calls.call_count == 0


def test_create_s3_with_huggingface_model_id_is_accepted(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(
            201,
            json=_model_payload(
                weight_source="s3_presigned",
                huggingface_model_id="Qwen/Qwen3-0.6B",
            ),
        )
    )

    model = client.custom_models.create(
        name="my-s3-model",
        weight_source="s3_presigned",
        huggingface_model_id="Qwen/Qwen3-0.6B",
        s3_url="https://example.com/model.tar.gz",
    )
    assert route.called
    sent = json.loads(route.calls.last.request.content)
    assert sent["weight_source"] == "s3_presigned"
    assert sent["huggingface_model_id"] == "Qwen/Qwen3-0.6B"
    assert sent["s3_url"] == "https://example.com/model.tar.gz"
    assert model.id == "cm_01"


def test_create_huggingface_does_not_require_huggingface_model_id_client_side(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """HuggingFace imports without huggingface_model_id should still hit the
    server (which will return its own 422); the client must not pre-empt it.
    """
    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(
            422,
            json={"code": "validation_error", "message": "missing field"},
        )
    )

    with pytest.raises(ValidationError) as exc_info:
        client.custom_models.create(
            name="my-hf-model", weight_source="huggingface"
        )
    assert route.called
    assert exc_info.value.code == "validation_error"


@pytest.mark.asyncio
async def test_async_create_s3_requires_huggingface_model_id(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    with pytest.raises(ValidationError) as exc_info:
        await async_client.custom_models.create(
            name="my-s3-model",
            weight_source="s3_assume_role",
            s3_role_arn="arn:aws:iam::123:role/example",
        )
    assert exc_info.value.code == "missing_huggingface_model_id"
    assert respx_mock.calls.call_count == 0
