"""Model listing.

Delegates to ``openai.OpenAI(...).models`` so customers get the same
ergonomics they're used to (``client.models.list()`` returns the
familiar ``SyncPage[Model]``). The OpenAI client is configured against
the Graphn inference host so we don't need to maintain a parallel
implementation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from graphn._transport import AsyncTransport, SyncTransport
from graphn.chat.completions import _build_async_openai, _build_sync_openai

if TYPE_CHECKING:  # pragma: no cover
    from openai import AsyncOpenAI, OpenAI
    from openai.resources.models import AsyncModels as _AsyncOpenAIModels
    from openai.resources.models import Models as _OpenAIModels


class Models:
    """Synchronous ``client.models`` namespace."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport
        self._openai: OpenAI | None = None

    @property
    def openai_client(self) -> OpenAI:
        if self._openai is None:
            self._openai = _build_sync_openai(self._transport)
        return self._openai

    @property
    def _models(self) -> _OpenAIModels:
        return self.openai_client.models

    def list(self, **kwargs: Any) -> Any:
        return self._models.list(**kwargs)

    def retrieve(self, model: str, **kwargs: Any) -> Any:
        return self._models.retrieve(model, **kwargs)


class AsyncModels:
    """Asynchronous ``client.models`` namespace."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport
        self._openai: AsyncOpenAI | None = None

    @property
    def openai_client(self) -> AsyncOpenAI:
        if self._openai is None:
            self._openai = _build_async_openai(self._transport)
        return self._openai

    @property
    def _models(self) -> _AsyncOpenAIModels:
        return self.openai_client.models

    async def list(self, **kwargs: Any) -> Any:
        return await self._models.list(**kwargs)

    async def retrieve(self, model: str, **kwargs: Any) -> Any:
        return await self._models.retrieve(model, **kwargs)
