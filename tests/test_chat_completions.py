"""Tests that the chat resource correctly delegates to the openai SDK."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from graphn import AsyncClient, Client
from tests.conftest import inference_url_for

_CHAT_RESPONSE = {
    "id": "chatcmpl-1",
    "object": "chat.completion",
    "created": 1_700_000_000,
    "model": "my-llama",
    "choices": [
        {
            "index": 0,
            "message": {"role": "assistant", "content": "hi back!"},
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 5, "completion_tokens": 3, "total_tokens": 8},
}


def test_chat_completions_create_routes_to_inference_host(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    route = respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        return_value=httpx.Response(200, json=_CHAT_RESPONSE)
    )

    resp = client.chat.completions.create(
        model="my-llama",
        messages=[{"role": "user", "content": "hello"}],
    )

    assert route.called
    sent = json.loads(route.calls.last.request.content)
    assert sent["model"] == "my-llama"
    assert sent["messages"] == [{"role": "user", "content": "hello"}]
    headers = route.calls.last.request.headers
    assert headers["Authorization"] == "Bearer gn_test_token"
    assert headers["X-Workspace-Id"] == "ws_test"
    assert resp.choices[0].message.content == "hi back!"


def test_chat_completions_propagates_error_responses(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    from openai import AuthenticationError as OpenAIAuthError

    respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        return_value=httpx.Response(
            401, json={"error": {"message": "bad key", "type": "auth_error"}}
        )
    )

    with pytest.raises(OpenAIAuthError):
        client.chat.completions.create(
            model="my-llama",
            messages=[{"role": "user", "content": "hello"}],
        )


def test_models_list_uses_inference_host(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    respx_mock.get(inference_url_for("v1/models")).mock(
        return_value=httpx.Response(
            200,
            json={
                "object": "list",
                "data": [
                    {
                        "id": "my-llama",
                        "object": "model",
                        "created": 1,
                        "owned_by": "graphn",
                    }
                ],
            },
        )
    )

    models = list(client.models.list())
    assert [m.id for m in models] == ["my-llama"]


@pytest.mark.asyncio
async def test_async_chat_completions(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        return_value=httpx.Response(200, json=_CHAT_RESPONSE)
    )

    resp = await async_client.chat.completions.create(
        model="my-llama",
        messages=[{"role": "user", "content": "hello"}],
    )
    assert resp.choices[0].message.content == "hi back!"


_COLD_START_BODY = {
    "error": {
        "message": (
            "Model is scaled to zero and is now warming up. "
            "Try again in 1-2 minutes."
        ),
        "type": "service_unavailable",
    }
}


def test_chat_auto_wakes_cold_custom_model_and_retries(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """First chat call hits a cold-start 503; SDK should call wake()
    on the control plane, then retry the chat call until it succeeds."""

    from tests.conftest import cp_url

    chat_route = respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        side_effect=[
            httpx.Response(503, json=_COLD_START_BODY),
            httpx.Response(200, json=_CHAT_RESPONSE),
        ]
    )
    wake_route = respx_mock.post(
        cp_url("custom-models/cm_deadbeef/wake")
    ).mock(
        return_value=httpx.Response(
            200,
            json={
                "id": "cm_deadbeef",
                "name": "my-cm",
                "workspace_id": "ws_test",
                "status": "ready",
                "weight_source": "huggingface",
                "gpu_count": 1,
                "capabilities": [],
                "min_replicas": 0,
                "max_replicas": 1,
                "cooldown_seconds": 600,
                "gpu_memory_utilization": 0.9,
                "created_at": "2026-04-25T00:00:00Z",
                "updated_at": "2026-04-25T00:00:00Z",
            },
        )
    )

    resp = client.chat.completions.create(
        model="cm_deadbeef",
        messages=[{"role": "user", "content": "hello"}],
        wake_timeout=0.2,
    )

    assert wake_route.called
    assert chat_route.call_count == 2
    assert resp.choices[0].message.content == "hi back!"
    sent = json.loads(chat_route.calls[0].request.content)
    assert sent["model"] == "custom:cm_deadbeef", (
        "SDK should prepend the 'custom:' routing prefix to bare cm_ ids "
        "before delegating to the OpenAI client; customers should never "
        "have to type the prefix themselves."
    )


def test_chat_does_not_wake_for_built_in_models(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    """A 503 from a built-in model id must not trigger a wake call."""

    from openai import InternalServerError

    from tests.conftest import cp_url

    respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        return_value=httpx.Response(503, json=_COLD_START_BODY)
    )
    wake_route = respx_mock.post(cp_url("custom-models/cm_xxx/wake")).mock(
        return_value=httpx.Response(200, json={})
    )

    with pytest.raises(InternalServerError):
        client.chat.completions.create(
            model="my-llama",
            messages=[{"role": "user", "content": "hello"}],
        )

    assert not wake_route.called


def test_chat_auto_wake_can_be_disabled(
    client: Client, respx_mock: respx.MockRouter
) -> None:
    from openai import InternalServerError

    from tests.conftest import cp_url

    respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        return_value=httpx.Response(503, json=_COLD_START_BODY)
    )
    wake_route = respx_mock.post(cp_url("custom-models/cm_x/wake")).mock(
        return_value=httpx.Response(200, json={})
    )

    with pytest.raises(InternalServerError):
        client.chat.completions.create(
            model="custom:cm_x",
            messages=[{"role": "user", "content": "hello"}],
            auto_wake=False,
        )

    assert not wake_route.called


@pytest.mark.asyncio
async def test_async_chat_auto_wakes_cold_custom_model(
    async_client: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    from tests.conftest import cp_url

    chat_route = respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        side_effect=[
            httpx.Response(503, json=_COLD_START_BODY),
            httpx.Response(200, json=_CHAT_RESPONSE),
        ]
    )
    wake_route = respx_mock.post(
        cp_url("custom-models/cm_aabbccdd/wake")
    ).mock(
        return_value=httpx.Response(
            200,
            json={
                "id": "cm_aabbccdd",
                "name": "my-cm",
                "workspace_id": "ws_test",
                "status": "ready",
                "weight_source": "huggingface",
                "gpu_count": 1,
                "capabilities": [],
                "min_replicas": 0,
                "max_replicas": 1,
                "cooldown_seconds": 600,
                "gpu_memory_utilization": 0.9,
                "created_at": "2026-04-25T00:00:00Z",
                "updated_at": "2026-04-25T00:00:00Z",
            },
        )
    )

    resp = await async_client.chat.completions.create(
        model="cm_aabbccdd",
        messages=[{"role": "user", "content": "hello"}],
        wake_timeout=0.2,
    )

    assert wake_route.called
    assert chat_route.call_count == 2
    assert resp.choices[0].message.content == "hi back!"


@pytest.mark.parametrize(
    ("input_model", "expected_wire"),
    [
        # Bare custom-model id: SDK adds the routing prefix.
        ("cm_abc123", "custom:cm_abc123"),
        # Already-prefixed: idempotent passthrough so old code still works.
        ("custom:cm_abc123", "custom:cm_abc123"),
        # First-party catalog id (HuggingFace-style with a slash):
        # never matches the cm_ shape, so unchanged.
        ("meta-llama/Llama-3.1-8B-Instruct", "meta-llama/Llama-3.1-8B-Instruct"),
        # Hosted single-token models (no slash, not cm_): unchanged.
        ("whisper-large-v3", "whisper-large-v3"),
        # Bare-id-shaped string that isn't actually our id format
        # (uppercase): pass through, let the gateway 404 with a clear
        # error rather than silently rewrite.
        ("cm_NOTHEX", "cm_NOTHEX"),
    ],
)
def test_chat_normalizes_model_param_for_each_namespace(
    client: Client,
    respx_mock: respx.MockRouter,
    input_model: str,
    expected_wire: str,
) -> None:
    """SDK rewrites bare cm_<hex> ids to ``custom:cm_...`` and leaves
    everything else alone, so customers can pass ``model=model.id``
    without knowing about the routing prefix."""

    route = respx_mock.post(inference_url_for("v1/chat/completions")).mock(
        return_value=httpx.Response(200, json=_CHAT_RESPONSE)
    )

    client.chat.completions.create(
        model=input_model,
        messages=[{"role": "user", "content": "hi"}],
    )

    assert route.called
    sent = json.loads(route.calls.last.request.content)
    assert sent["model"] == expected_wire
