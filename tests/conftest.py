"""Shared fixtures for the graphn SDK test suite.

Both the control-plane and inference hosts are mocked with
``respx``. Tests that exercise sync and async clients pull a
ready-to-use client from these fixtures so individual test files stay
focused on behaviour rather than wiring.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator

import pytest
import pytest_asyncio
import respx

from graphn import AsyncClient, Client

API_KEY = "gn_test_token"
WORKSPACE_ID = "ws_test"
BASE_URL = "https://api.graphn.test"
INFERENCE_URL = "https://inference.graphn.test"


@pytest.fixture
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def inference_url() -> str:
    return INFERENCE_URL


@pytest.fixture
def workspace_id() -> str:
    return WORKSPACE_ID


@pytest.fixture
def respx_mock() -> Iterator[respx.MockRouter]:
    """A respx mock router that intercepts both base + inference URLs."""

    with respx.mock(
        assert_all_called=False,
        assert_all_mocked=True,
        base_url=None,
    ) as router:
        yield router


@pytest.fixture
def client(respx_mock: respx.MockRouter) -> Iterator[Client]:
    instance = Client(
        api_key=API_KEY,
        workspace_id=WORKSPACE_ID,
        base_url=BASE_URL,
        inference_url=INFERENCE_URL,
        max_retries=0,
        timeout=5.0,
    )
    yield instance
    instance.close()


@pytest_asyncio.fixture
async def async_client(respx_mock: respx.MockRouter) -> AsyncIterator[AsyncClient]:
    instance = AsyncClient(
        api_key=API_KEY,
        workspace_id=WORKSPACE_ID,
        base_url=BASE_URL,
        inference_url=INFERENCE_URL,
        max_retries=0,
        timeout=5.0,
    )
    try:
        yield instance
    finally:
        await instance.aclose()


def cp_url(path: str) -> str:
    """Build the absolute control-plane URL for ``path``."""

    return f"{BASE_URL}/v1/{WORKSPACE_ID}/{path.lstrip('/')}"


def inference_url_for(path: str) -> str:
    """Build the absolute inference URL for ``path``."""

    return f"{INFERENCE_URL}/{path.lstrip('/')}"
