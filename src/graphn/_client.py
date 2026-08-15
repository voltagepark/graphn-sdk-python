"""Client and AsyncClient entrypoints.

These wrap an httpx-backed transport (:mod:`graphn._transport`) and
expose the public resource surface. Customers always interact with the
SDK through one of these two classes.

Both clients inject the workspace id into control-plane paths
automatically; resource modules stay agnostic of where the workspace
id lives by going through ``self._transport.cp_path("custom-models")``.
Inference resources route through the official ``openai`` SDK, which
is configured against ``inference_url`` with ``X-Workspace-Id`` as a
default header so the model-gateway can authorize the workspace.
"""

from __future__ import annotations

import os
from collections.abc import Mapping

from graphn._transport import (
    AsyncTransport,
    SyncTransport,
    _TransportConfig,
)

DEFAULT_BASE_URL = "https://cp.graphn.ai"
DEFAULT_INFERENCE_URL = "https://model.graphn.ai"
DEFAULT_GATEWAY_URL = "https://gateway.graphn.ai"
DEFAULT_STORAGE_URL = "https://storage.graphn.ai"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_MAX_RETRIES = 2

_API_KEY_ENV = "GRAPHN_API_KEY"
_WORKSPACE_ENV = "GRAPHN_WORKSPACE_ID"
_BASE_URL_ENV = "GRAPHN_BASE_URL"
_INFERENCE_URL_ENV = "GRAPHN_INFERENCE_URL"
_GATEWAY_URL_ENV = "GRAPHN_GATEWAY_URL"
_STORAGE_URL_ENV = "GRAPHN_STORAGE_URL"


def _resolve(value: str | None, env_var: str, *, name: str, required: bool = True) -> str | None:
    resolved = value if value is not None else os.environ.get(env_var)
    if required and not resolved:
        raise ValueError(
            f"{name} must be provided explicitly or via the {env_var} environment variable."
        )
    return resolved


def _resolve_host_urls(
    base_url: str | None,
    inference_url: str | None,
    gateway_url: str | None,
    storage_url: str | None,
) -> tuple[str, str, str, str]:
    base = base_url or os.environ.get(_BASE_URL_ENV) or DEFAULT_BASE_URL
    inf = inference_url or os.environ.get(_INFERENCE_URL_ENV) or DEFAULT_INFERENCE_URL
    gw = gateway_url or os.environ.get(_GATEWAY_URL_ENV) or DEFAULT_GATEWAY_URL
    storage = storage_url or os.environ.get(_STORAGE_URL_ENV) or DEFAULT_STORAGE_URL
    return base, inf, gw, storage


class Client:
    """Synchronous Graphn API client.

    Parameters
    ----------
    api_key:
        Bearer API key starting with ``gn_``. Falls back to the
        ``GRAPHN_API_KEY`` environment variable.
    workspace_id:
        Workspace this client operates against. Falls back to the
        ``GRAPHN_WORKSPACE_ID`` environment variable.
    base_url:
        Control-plane base URL. Defaults to production
        (``https://cp.graphn.ai``).
    inference_url:
        Inference base URL passed to the underlying OpenAI client.
        Defaults to ``https://model.graphn.ai``.
    gateway_url:
        Gateway host for batch jobs and UUID execution ids.
        Defaults to ``https://gateway.graphn.ai``.
    storage_url:
        S3-style object storage host. Defaults to
        ``https://storage.graphn.ai``.
    timeout:
        Per-request timeout in seconds.
    max_retries:
        Maximum number of retry attempts on connect failures, 429, or
        5xx responses.
    default_headers:
        Extra headers attached to every request.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        workspace_id: str | None = None,
        base_url: str | None = None,
        inference_url: str | None = None,
        gateway_url: str | None = None,
        storage_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
    ) -> None:
        resolved_key = _resolve(api_key, _API_KEY_ENV, name="api_key")
        resolved_workspace = _resolve(workspace_id, _WORKSPACE_ENV, name="workspace_id")
        assert resolved_key is not None and resolved_workspace is not None
        resolved_base, resolved_inference, resolved_gateway, resolved_storage = _resolve_host_urls(
            base_url, inference_url, gateway_url, storage_url
        )

        cfg = _TransportConfig(
            api_key=resolved_key,
            workspace_id=resolved_workspace,
            base_url=resolved_base,
            inference_url=resolved_inference,
            gateway_url=resolved_gateway,
            storage_url=resolved_storage,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._transport = SyncTransport(cfg)
        self._attach_resources()

    @property
    def api_key(self) -> str:
        return self._transport.cfg.api_key

    @property
    def workspace_id(self) -> str:
        return self._transport.cfg.workspace_id

    @property
    def base_url(self) -> str:
        return self._transport.cfg.base_url

    @property
    def inference_url(self) -> str:
        return self._transport.cfg.inference_url

    @property
    def gateway_url(self) -> str:
        return self._transport.cfg.gateway_url

    @property
    def storage_url(self) -> str:
        return self._transport.cfg.storage_url

    def _attach_resources(self) -> None:
        # Imported lazily so cyclic imports stay impossible.
        from graphn.agents import Agents
        from graphn.api_keys import ApiKeys
        from graphn.batch import Batches
        from graphn.blueprints import Blueprints
        from graphn.chat.completions import Chat
        from graphn.custom_models.resource import CustomModels
        from graphn.executions import Executions
        from graphn.functions import Functions
        from graphn.imported_models import ImportedModels
        from graphn.knowledgebases import KnowledgeBases
        from graphn.mcp_servers import McpServers
        from graphn.models import Models
        from graphn.organizations import Organizations
        from graphn.secrets.resource import Secrets
        from graphn.storages import Storages
        from graphn.triggers import Triggers
        from graphn.tts import TTS
        from graphn.workflows import Workflows
        from graphn.workspaces import Workspaces

        self.custom_models = CustomModels(self._transport)
        self.secrets = Secrets(self._transport)
        self.chat = Chat(self._transport)
        self.models = Models(self._transport)
        self.tts = TTS(self._transport)
        self.imported_models = ImportedModels(self._transport)
        self.agents = Agents(self._transport)
        self.functions = Functions(self._transport)
        self.mcp_servers = McpServers(self._transport)
        self.workflows = Workflows(self._transport)
        self.executions = Executions(self._transport)
        self.triggers = Triggers(self._transport)
        self.knowledgebases = KnowledgeBases(self._transport)
        self.organizations = Organizations(self._transport)
        self.workspaces = Workspaces(self._transport)
        self.api_keys = ApiKeys(self._transport)
        self.blueprints = Blueprints(self._transport)
        self.storages = Storages(self._transport)
        self.batch = Batches(self._transport)

    def close(self) -> None:
        self.tts.close()
        self.imported_models.close()
        self._transport.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class AsyncClient:
    """Asynchronous Graphn API client.

    Mirrors :class:`Client` exactly; methods on resource attributes are
    coroutines. Use ``async with AsyncClient(...) as client:`` to
    guarantee the underlying httpx connection pool is released.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        workspace_id: str | None = None,
        base_url: str | None = None,
        inference_url: str | None = None,
        gateway_url: str | None = None,
        storage_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
    ) -> None:
        resolved_key = _resolve(api_key, _API_KEY_ENV, name="api_key")
        resolved_workspace = _resolve(workspace_id, _WORKSPACE_ENV, name="workspace_id")
        assert resolved_key is not None and resolved_workspace is not None
        resolved_base, resolved_inference, resolved_gateway, resolved_storage = _resolve_host_urls(
            base_url, inference_url, gateway_url, storage_url
        )

        cfg = _TransportConfig(
            api_key=resolved_key,
            workspace_id=resolved_workspace,
            base_url=resolved_base,
            inference_url=resolved_inference,
            gateway_url=resolved_gateway,
            storage_url=resolved_storage,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
        )
        self._transport = AsyncTransport(cfg)
        self._attach_resources()

    @property
    def api_key(self) -> str:
        return self._transport.cfg.api_key

    @property
    def workspace_id(self) -> str:
        return self._transport.cfg.workspace_id

    @property
    def base_url(self) -> str:
        return self._transport.cfg.base_url

    @property
    def inference_url(self) -> str:
        return self._transport.cfg.inference_url

    @property
    def gateway_url(self) -> str:
        return self._transport.cfg.gateway_url

    @property
    def storage_url(self) -> str:
        return self._transport.cfg.storage_url

    def _attach_resources(self) -> None:
        from graphn.agents import AsyncAgents
        from graphn.api_keys import AsyncApiKeys
        from graphn.batch import AsyncBatches
        from graphn.blueprints import AsyncBlueprints
        from graphn.chat.completions import AsyncChat
        from graphn.custom_models.resource import AsyncCustomModels
        from graphn.executions import AsyncExecutions
        from graphn.functions import AsyncFunctions
        from graphn.imported_models import AsyncImportedModels
        from graphn.knowledgebases import AsyncKnowledgeBases
        from graphn.mcp_servers import AsyncMcpServers
        from graphn.models import AsyncModels
        from graphn.organizations import AsyncOrganizations
        from graphn.secrets.resource import AsyncSecrets
        from graphn.storages import AsyncStorages
        from graphn.triggers import AsyncTriggers
        from graphn.tts import AsyncTTS
        from graphn.workflows import AsyncWorkflows
        from graphn.workspaces import AsyncWorkspaces

        self.custom_models = AsyncCustomModels(self._transport)
        self.secrets = AsyncSecrets(self._transport)
        self.chat = AsyncChat(self._transport)
        self.models = AsyncModels(self._transport)
        self.tts = AsyncTTS(self._transport)
        self.imported_models = AsyncImportedModels(self._transport)
        self.agents = AsyncAgents(self._transport)
        self.functions = AsyncFunctions(self._transport)
        self.mcp_servers = AsyncMcpServers(self._transport)
        self.workflows = AsyncWorkflows(self._transport)
        self.executions = AsyncExecutions(self._transport)
        self.triggers = AsyncTriggers(self._transport)
        self.knowledgebases = AsyncKnowledgeBases(self._transport)
        self.organizations = AsyncOrganizations(self._transport)
        self.workspaces = AsyncWorkspaces(self._transport)
        self.api_keys = AsyncApiKeys(self._transport)
        self.blueprints = AsyncBlueprints(self._transport)
        self.storages = AsyncStorages(self._transport)
        self.batch = AsyncBatches(self._transport)

    async def aclose(self) -> None:
        await self.tts.aclose()
        await self.imported_models.aclose()
        await self._transport.aclose()

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()
