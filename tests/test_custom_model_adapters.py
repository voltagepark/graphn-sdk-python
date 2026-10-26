"""Tests for shared LoRA bases and their adapters (sync + async)."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from graphn import APIError, AsyncClient, Client, ConflictError, ValidationError
from tests.conftest import cp_url
from tests.test_custom_models import _model_payload


def _adapter_payload(**overrides: object) -> dict[str, object]:
    payload = _model_payload(
        id="cm_ad1",
        name="support-v3",
        huggingface_model_id="acme/support-v3",
        parent_model_id="cm_base",
        is_lora_adapter=True,
    )
    payload.update(overrides)
    return payload


def test_create_shared_base_sends_lora_fields(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(
            201,
            json=_model_payload(id="cm_base", lora_enabled=True, max_lora_rank=64, max_adapters=8),
        )
    )

    model = client.custom_models.create(
        name="base",
        huggingface_model_id="meta-llama/Llama-3-8B",
        lora_enabled=True,
        max_lora_rank=64,
    )

    sent = json.loads(route.calls.last.request.content)
    assert sent["lora_enabled"] is True
    assert sent["max_lora_rank"] == 64
    assert model.lora_enabled is True
    assert model.max_adapters == 8


def test_create_shared_base_requires_rank(client: Client, respx_mock: respx.MockRouter) -> None:
    with pytest.raises(ValidationError) as exc_info:
        client.custom_models.create(
            name="base", huggingface_model_id="meta-llama/Llama-3-8B", lora_enabled=True
        )
    assert exc_info.value.code == "missing_max_lora_rank"
    assert not respx_mock.calls


def test_create_without_lora_omits_fields(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(cp_url("custom-models")).mock(
        return_value=httpx.Response(201, json=_model_payload())
    )

    client.custom_models.create(name="m", huggingface_model_id="meta-llama/Llama-3-8B")

    sent = json.loads(route.calls.last.request.content)
    assert "lora_enabled" not in sent
    assert "max_lora_rank" not in sent


def test_list_include_adapters(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.get(cp_url("custom-models")).mock(
        return_value=httpx.Response(
            200, json={"items": [_model_payload(id="cm_base"), _adapter_payload()]}
        )
    )

    ids = [m.id for m in client.custom_models.list(include_adapters=True)]

    assert route.calls.last.request.url.params["include"] == "adapters"
    assert ids == ["cm_base", "cm_ad1"]


def test_list_default_has_no_include(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.get(cp_url("custom-models")).mock(
        return_value=httpx.Response(200, json={"items": []})
    )

    list(client.custom_models.list())

    assert "include" not in route.calls.last.request.url.params


def test_attach_huggingface(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(201, json=_adapter_payload())
    )

    adapter = client.custom_models.adapters.attach(
        "cm_base",
        huggingface_model_id="acme/support-v3",
        hf_token_secret_id="sec_1",
        idempotency_key="attach-1",
    )

    request = route.calls.last.request
    assert json.loads(request.content) == {
        "weight_source": "huggingface",
        "huggingface_model_id": "acme/support-v3",
        "hf_token_secret_id": "sec_1",
    }
    assert request.headers["Idempotency-Key"] == "attach-1"
    assert adapter.parent_model_id == "cm_base"


def test_attach_s3_presigned(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(201, json=_adapter_payload(weight_source="s3_presigned"))
    )

    client.custom_models.adapters.attach(
        "cm_base", s3_url="https://bucket.s3.amazonaws.com/a.tar.gz?X-Amz-Signature=x", name="a"
    )

    sent = json.loads(route.calls.last.request.content)
    assert sent["weight_source"] == "s3_presigned"
    assert sent["name"] == "a"
    assert "s3_role_arn" not in sent


def test_attach_s3_assume_role(client: Client, respx_mock: respx.MockRouter) -> None:
    route = respx_mock.post(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(201, json=_adapter_payload(weight_source="s3_assume_role"))
    )

    client.custom_models.adapters.attach(
        "cm_base",
        s3_url="s3://acme-models/adapters/v3/",
        s3_role_arn="arn:aws:iam::123456789012:role/graphn-byom-acme",
        s3_external_id="ext-1",
        acknowledge_base_mismatch=True,
    )

    sent = json.loads(route.calls.last.request.content)
    assert sent == {
        "weight_source": "s3_assume_role",
        "s3_url": "s3://acme-models/adapters/v3/",
        "s3_role_arn": "arn:aws:iam::123456789012:role/graphn-byom-acme",
        "s3_external_id": "ext-1",
        "base_mismatch_acknowledged": True,
    }


@pytest.mark.parametrize(
    "kwargs",
    [{}, {"huggingface_model_id": "acme/a", "s3_url": "s3://b/a/"}],
)
def test_attach_needs_exactly_one_source(
    client: Client, respx_mock: respx.MockRouter, kwargs: dict[str, str]
) -> None:
    with pytest.raises(ValidationError) as exc_info:
        client.custom_models.adapters.attach("cm_base", **kwargs)
    assert exc_info.value.code == "adapter_source_required"
    assert not respx_mock.calls


def test_attach_conflict_surfaces_code(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(
            409, json={"code": "NOT_LORA_ENABLED", "message": "base is not a shared LoRA base"}
        )
    )

    with pytest.raises(ConflictError) as exc_info:
        client.custom_models.adapters.attach("cm_base", huggingface_model_id="acme/a")
    assert exc_info.value.code == "NOT_LORA_ENABLED"


def test_list_adapters(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.get(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(
            200, json={"items": [_adapter_payload(), _adapter_payload(id="cm_ad2")]}
        )
    )

    adapters = client.custom_models.adapters.list("cm_base")

    assert [a.id for a in adapters] == ["cm_ad1", "cm_ad2"]


def test_adapter_wait_until_ready(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("graphn.custom_models.adapters.time.sleep", lambda _: None)
    route = respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        side_effect=[
            httpx.Response(200, json=_adapter_payload(status="pending")),
            httpx.Response(200, json=_adapter_payload(status="ready", adapter_digest="sha256:a")),
        ]
    )

    adapter = client.custom_models.adapters.wait_until_ready("cm_ad1", poll_interval=0)

    assert adapter.status == "ready"
    assert adapter.adapter_digest == "sha256:a"
    assert route.call_count == 2


def test_adapter_wait_until_ready_failed(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("graphn.custom_models.adapters.time.sleep", lambda _: None)
    respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        return_value=httpx.Response(
            200,
            json=_adapter_payload(
                status="failed", error_message="ADAPTER_RANK_EXCEEDS_BASE: rank 128 > 64"
            ),
        )
    )

    with pytest.raises(APIError) as exc_info:
        client.custom_models.adapters.wait_until_ready("cm_ad1", poll_interval=0)
    assert exc_info.value.code == "custom_model_adapter_failed"
    assert str(exc_info.value).startswith("ADAPTER_RANK_EXCEEDS_BASE")


def test_adapter_delete_and_wait(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("graphn.custom_models.adapters.time.sleep", lambda _: None)
    delete = respx_mock.delete(cp_url("custom-models/cm_ad1")).mock(
        return_value=httpx.Response(204)
    )
    get = respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        side_effect=[
            httpx.Response(200, json=_adapter_payload(status="deleting")),
            httpx.Response(404, json={"code": "NOT_FOUND", "message": "gone"}),
        ]
    )

    client.custom_models.adapters.delete("cm_ad1")
    client.custom_models.adapters.wait_until_deleted("cm_ad1", poll_interval=0)

    assert delete.called
    assert get.call_count == 2


def test_base_delete_with_adapters_conflicts(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.delete(cp_url("custom-models/cm_base")).mock(
        return_value=httpx.Response(
            409, json={"code": "HAS_ADAPTERS", "message": "delete its adapters first"}
        )
    )

    with pytest.raises(ConflictError) as exc_info:
        client.custom_models.delete("cm_base")
    assert exc_info.value.code == "HAS_ADAPTERS"


def test_wait_until_ready_falls_back_to_get_for_adapters(
    client: Client, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("graphn.custom_models.resource.time.sleep", lambda _: None)
    refresh = respx_mock.post(cp_url("custom-models/cm_ad1/refresh")).mock(
        return_value=httpx.Response(
            422, json={"code": "ADAPTER_REFRESH_UNSUPPORTED", "message": "adapters can't refresh"}
        )
    )
    get = respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        side_effect=[
            httpx.Response(200, json=_adapter_payload(status="pending")),
            httpx.Response(200, json=_adapter_payload(status="ready")),
        ]
    )

    model = client.custom_models.wait_until_ready("cm_ad1", poll_interval=0)

    assert model.status == "ready"
    assert refresh.call_count == 1
    assert get.call_count == 2


def test_wait_until_ready_reraises_other_422(client: Client, respx_mock: respx.MockRouter) -> None:
    respx_mock.post(cp_url("custom-models/cm_01/refresh")).mock(
        return_value=httpx.Response(422, json={"code": "validation_error", "message": "bad"})
    )

    with pytest.raises(ValidationError):
        client.custom_models.wait_until_ready("cm_01", poll_interval=0)


async def test_async_attach_and_wait(
    async_client: AsyncClient, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def _no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr("graphn.custom_models.adapters.asyncio.sleep", _no_sleep)
    attach = respx_mock.post(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(201, json=_adapter_payload())
    )
    respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        side_effect=[
            httpx.Response(200, json=_adapter_payload(status="pending")),
            httpx.Response(200, json=_adapter_payload(status="ready")),
        ]
    )

    adapter = await async_client.custom_models.adapters.attach(
        "cm_base", huggingface_model_id="acme/support-v3"
    )
    ready = await async_client.custom_models.adapters.wait_until_ready(adapter.id, poll_interval=0)

    assert json.loads(attach.calls.last.request.content)["weight_source"] == "huggingface"
    assert ready.status == "ready"


async def test_async_list_and_delete_adapters(
    async_client: AsyncClient, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def _no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr("graphn.custom_models.adapters.asyncio.sleep", _no_sleep)
    respx_mock.get(cp_url("custom-models/cm_base/adapters")).mock(
        return_value=httpx.Response(200, json={"items": [_adapter_payload()]})
    )
    respx_mock.delete(cp_url("custom-models/cm_ad1")).mock(return_value=httpx.Response(204))
    respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        return_value=httpx.Response(404, json={"code": "NOT_FOUND", "message": "gone"})
    )

    adapters = await async_client.custom_models.adapters.list("cm_base")
    await async_client.custom_models.adapters.delete(adapters[0].id)
    await async_client.custom_models.adapters.wait_until_deleted(adapters[0].id, poll_interval=0)

    assert [a.id for a in adapters] == ["cm_ad1"]


async def test_async_wait_until_ready_falls_back_to_get(
    async_client: AsyncClient, respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    async def _no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr("graphn.custom_models.resource.asyncio.sleep", _no_sleep)
    respx_mock.post(cp_url("custom-models/cm_ad1/refresh")).mock(
        return_value=httpx.Response(
            422, json={"code": "ADAPTER_REFRESH_UNSUPPORTED", "message": "adapters can't refresh"}
        )
    )
    respx_mock.get(cp_url("custom-models/cm_ad1")).mock(
        return_value=httpx.Response(200, json=_adapter_payload(status="ready"))
    )

    model = await async_client.custom_models.wait_until_ready("cm_ad1", poll_interval=0)

    assert model.status == "ready"
