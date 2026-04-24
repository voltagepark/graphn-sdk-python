"""Tests for client configuration: env-var fallback, headers, defaults."""

from __future__ import annotations

import pytest

from graphn import Client


def test_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GRAPHN_API_KEY", raising=False)
    monkeypatch.delenv("GRAPHN_WORKSPACE_ID", raising=False)
    with pytest.raises(ValueError, match="api_key"):
        Client(workspace_id="ws_x")


def test_requires_workspace_id(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GRAPHN_WORKSPACE_ID", raising=False)
    with pytest.raises(ValueError, match="workspace_id"):
        Client(api_key="gn_x")


def test_resolves_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GRAPHN_API_KEY", "gn_env")
    monkeypatch.setenv("GRAPHN_WORKSPACE_ID", "ws_env")
    monkeypatch.setenv("GRAPHN_BASE_URL", "https://api.graphn.test")
    monkeypatch.setenv("GRAPHN_INFERENCE_URL", "https://inference.graphn.test")

    client = Client()
    try:
        assert client.api_key == "gn_env"
        assert client.workspace_id == "ws_env"
        assert client.base_url == "https://api.graphn.test"
        assert client.inference_url == "https://inference.graphn.test"
    finally:
        client.close()


def test_default_base_urls() -> None:
    client = Client(api_key="gn_x", workspace_id="ws_y")
    try:
        assert client.base_url == "https://api.graphn.ai"
        assert client.inference_url == "https://inference.graphn.ai"
    finally:
        client.close()


def test_cp_path_url_encodes_segments() -> None:
    client = Client(api_key="gn_x", workspace_id="ws_y")
    try:
        path = client._transport.cp_path("custom-models", "with space/slash")
        assert path == "/v1/ws_y/custom-models/with%20space%2Fslash"
    finally:
        client.close()
