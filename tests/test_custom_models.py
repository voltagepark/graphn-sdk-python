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
    """S3 imports must include huggingface_model_id (the canonical model id).

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


def test_create_s3_lora_passes_base_model_id(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """`base_model_id` is the only way to classify an S3 bundle as LoRA at create."""

    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(
            201,
            json=_model_payload(
                weight_source="s3_presigned",
                huggingface_model_id="org/qwen3-finetune",
                artifact_type="lora",
                base_model_id="Qwen/Qwen3-4B",
            ),
        )
    )

    model = client.custom_models.create(
        name="my-lora",
        weight_source="s3_presigned",
        huggingface_model_id="org/qwen3-finetune",
        s3_url="https://example.com/lora.tar.gz",
        base_model_id="Qwen/Qwen3-4B",
    )

    assert route.called
    sent = json.loads(route.calls.last.request.content)
    assert sent["base_model_id"] == "Qwen/Qwen3-4B"
    assert model.artifact_type == "lora"
    assert model.base_model_id == "Qwen/Qwen3-4B"


def test_create_huggingface_lora_override_passes_base_model_id(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """On HF imports `base_model_id` overrides `adapter_config.json::base_model_name_or_path`."""

    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(201, json=_model_payload())
    )

    client.custom_models.create(
        name="my-lora",
        huggingface_model_id="org/some-lora",
        base_model_id="meta-llama/Llama-3-8B",
    )

    sent = json.loads(route.calls.last.request.content)
    assert sent["base_model_id"] == "meta-llama/Llama-3-8B"


def test_get_returns_typed_lora_fields(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("custom-models/cm_lora")).mock(
        return_value=httpx.Response(
            200,
            json=_model_payload(
                id="cm_lora",
                artifact_type="lora",
                base_model_id="Qwen/Qwen3-4B",
                lora_adapter_name="my-lora",
                lora_rank=16,
            ),
        )
    )

    model = client.custom_models.get("cm_lora")
    assert model.artifact_type == "lora"
    assert model.base_model_id == "Qwen/Qwen3-4B"
    assert model.lora_adapter_name == "my-lora"
    assert model.lora_rank == 16


def test_get_legacy_response_treats_artifact_type_as_none(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """Older control planes don't return `artifact_type`; SDK must tolerate it."""

    respx_mock.get(cp_url("custom-models/cm_legacy")).mock(
        return_value=httpx.Response(200, json=_model_payload(id="cm_legacy"))
    )

    model = client.custom_models.get("cm_legacy")
    assert model.artifact_type is None
    assert model.base_model_id is None
    assert model.lora_adapter_name is None
    assert model.lora_rank is None


def test_validate_returns_lora_fields(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.post(cp_url("custom-models/validate")).mock(
        return_value=httpx.Response(
            200,
            json={
                "valid": True,
                "artifact_type": "lora",
                "detected_base_model_id": "Qwen/Qwen3-4B",
                "lora_rank": 16,
                "architectures": ["Qwen3ForCausalLM"],
                "num_params": 7_500_000_000,
            },
        )
    )

    resp = client.custom_models.validate(huggingface_model_id="org/some-lora")
    assert resp.valid is True
    assert resp.artifact_type == "lora"
    assert resp.detected_base_model_id == "Qwen/Qwen3-4B"
    assert resp.lora_rank == 16


def test_validate_forwards_model_size_gb(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.post(cp_url("custom-models/validate")).mock(
        return_value=httpx.Response(200, json={"valid": True})
    )

    client.custom_models.validate(
        huggingface_model_id="meta-llama/Llama-3-405B",
        model_size_gb=812,
    )
    sent = json.loads(route.calls.last.request.content)
    assert sent["model_size_gb"] == 812


def test_update_sends_patch_with_body(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.patch(cp_url("custom-models/cm_01")).mock(
        return_value=httpx.Response(
            200,
            json=_model_payload(
                status="ready",
                min_replicas=1,
                max_replicas=4,
                cooldown_seconds=300,
                display_name="renamed",
            ),
        )
    )

    model = client.custom_models.update(
        "cm_01",
        name="renamed",
        min_replicas=1,
        max_replicas=4,
        cooldown_seconds=300,
    )

    assert route.called
    assert route.calls.last.request.method == "PATCH"
    sent = json.loads(route.calls.last.request.content)
    assert sent == {
        "name": "renamed",
        "min_replicas": 1,
        "max_replicas": 4,
        "cooldown_seconds": 300,
    }
    assert model.min_replicas == 1
    assert model.max_replicas == 4
    assert model.cooldown_seconds == 300


def test_update_rejects_empty_body(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """An empty PATCH must fail client-side, never hitting the wire."""

    with pytest.raises(ValidationError) as exc_info:
        client.custom_models.update("cm_01")
    assert exc_info.value.code == "empty_update"
    assert respx_mock.calls.call_count == 0


def test_update_404_maps_to_not_found(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.patch(cp_url("custom-models/missing")).mock(
        return_value=httpx.Response(
            404, json={"code": "not_found", "message": "no such model"}
        )
    )

    with pytest.raises(NotFoundError):
        client.custom_models.update("missing", min_replicas=1)


def test_update_extra_passes_through(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """`extra` lets callers PATCH future fields without an SDK release."""

    route = respx_mock.patch(cp_url("custom-models/cm_01")).mock(
        return_value=httpx.Response(200, json=_model_payload())
    )

    client.custom_models.update("cm_01", extra={"future_field": "value"})
    sent = json.loads(route.calls.last.request.content)
    assert sent == {"future_field": "value"}


def test_supported_architectures_returns_typed(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("custom-models/supported-architectures")).mock(
        return_value=httpx.Response(
            200,
            json={
                "architectures": [
                    {
                        "name": "LlamaForCausalLM",
                        "capabilities": ["tool_calling", "streaming"],
                    },
                    {
                        "name": "Qwen3VLMoeForConditionalGeneration",
                        "capabilities": ["vision", "image_input", "streaming"],
                    },
                ],
            },
        )
    )

    catalog = client.custom_models.supported_architectures()
    assert [a.name for a in catalog.architectures] == [
        "LlamaForCausalLM",
        "Qwen3VLMoeForConditionalGeneration",
    ]
    assert catalog.architectures[1].capabilities == ["vision", "image_input", "streaming"]


@pytest.mark.asyncio
async def test_async_update_sends_patch_with_body(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.patch(cp_url("custom-models/cm_01")).mock(
        return_value=httpx.Response(
            200, json=_model_payload(min_replicas=2, max_replicas=6)
        )
    )

    model = await async_client.custom_models.update(
        "cm_01", min_replicas=2, max_replicas=6
    )

    assert route.called
    sent = json.loads(route.calls.last.request.content)
    assert sent == {"min_replicas": 2, "max_replicas": 6}
    assert model.min_replicas == 2
    assert model.max_replicas == 6


@pytest.mark.asyncio
async def test_async_update_rejects_empty_body(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    with pytest.raises(ValidationError):
        await async_client.custom_models.update("cm_01")
    assert respx_mock.calls.call_count == 0


@pytest.mark.asyncio
async def test_async_supported_architectures(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(cp_url("custom-models/supported-architectures")).mock(
        return_value=httpx.Response(
            200,
            json={
                "architectures": [
                    {"name": "LlamaForCausalLM", "capabilities": ["tool_calling"]},
                ],
            },
        )
    )

    catalog = await async_client.custom_models.supported_architectures()
    assert catalog.architectures[0].name == "LlamaForCausalLM"
