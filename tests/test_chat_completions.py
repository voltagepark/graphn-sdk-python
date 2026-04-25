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


def test_models_list_uses_inference_host(client: Client, respx_mock: respx.MockRouter) -> None:
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
