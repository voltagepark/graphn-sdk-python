"""Client and AsyncClient entrypoints.

Thin scaffolding so ``from graphn import Client, AsyncClient`` works
during the ``sdk-repo-init`` task. The full HTTPX-backed implementation
lands in the ``sdk-client-core`` task; until then both classes raise
on instantiation to make accidental use during this scaffolding phase
loud.
"""

from __future__ import annotations

import os
from typing import Any

DEFAULT_BASE_URL = "https://api.graphn.ai"
DEFAULT_INFERENCE_URL = "https://inference.graphn.ai"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_MAX_RETRIES = 2


def _resolve(value: str | None, env_var: str, *, name: str) -> str:
    """Resolve ``value`` from an explicit argument or fall back to env."""

    resolved = value or os.environ.get(env_var)
    if not resolved:
        raise ValueError(
            f"{name} must be provided explicitly or via the {env_var} "
            "environment variable."
        )
    return resolved


class _BaseClient:
    """Shared configuration for :class:`Client` and :class:`AsyncClient`."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        workspace_id: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        inference_url: str = DEFAULT_INFERENCE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: dict[str, str] | None = None,
    ) -> None:
        self.api_key = _resolve(api_key, "GRAPHN_API_KEY", name="api_key")
        self.workspace_id = _resolve(
            workspace_id, "GRAPHN_WORKSPACE_ID", name="workspace_id"
        )
        self.base_url = base_url.rstrip("/")
        self.inference_url = inference_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.default_headers = dict(default_headers or {})


class Client(_BaseClient):
    """Synchronous Graphn API client.

    Full transport is wired up in the ``sdk-client-core`` task.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # Resource attributes (custom_models, secrets, chat, models, tts,
        # imported_models) are attached in sdk-client-core.

    def close(self) -> None:
        """Close any underlying HTTP transport. No-op until sdk-client-core."""

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class AsyncClient(_BaseClient):
    """Asynchronous Graphn API client.

    Full transport is wired up in the ``sdk-client-core`` task.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    async def aclose(self) -> None:
        """Close any underlying HTTP transport. No-op until sdk-client-core."""

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()
