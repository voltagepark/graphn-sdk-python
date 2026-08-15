"""Model listing.

``GET https://model.graphn.ai/v1/models`` is OpenAI-shaped but today only
returns imported/custom rows — built-ins are on the control-plane catalog
(``GET https://cp.graphn.ai/v1/models``, same as ``graphn model list``).
List merges both so ``client.models.list()`` is the full set you can pass
to chat. ``retrieve`` still goes through the OpenAI client against the
inference host.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict

from graphn._exceptions import APIError
from graphn._transport import AsyncTransport, SyncTransport
from graphn.chat.completions import _build_async_openai, _build_sync_openai

if TYPE_CHECKING:  # pragma: no cover
    from openai import AsyncOpenAI, OpenAI
    from openai.resources.models import AsyncModels as _AsyncOpenAIModels
    from openai.resources.models import Models as _OpenAIModels


class Model(BaseModel):
    model_config = ConfigDict(extra="allow", frozen=True)

    id: str
    object: str = "model"
    owned_by: str | None = None
    created: int | None = None


class ModelPage:
    """OpenAI-shaped list: iterate it, or read ``.data``."""

    def __init__(self, data: list[Model]) -> None:
        self.object = "list"
        self.data = data

    def __iter__(self) -> Iterator[Model]:
        return iter(self.data)

    def __len__(self) -> int:
        return len(self.data)


def _from_cp_catalog(body: Any) -> list[Model]:
    if not isinstance(body, dict):
        return []
    rows = body.get("models") or body.get("data") or []
    if not isinstance(rows, list):
        return []
    out: list[Model] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        model_id = row.get("id") or row.get("name")
        if not isinstance(model_id, str) or not model_id:
            continue
        owned = row.get("source") or row.get("owned_by") or row.get("type")
        out.append(
            Model(
                id=model_id,
                owned_by=owned if isinstance(owned, str) else None,
            )
        )
    return out


def _from_openai_list(body: Any) -> list[Model]:
    if isinstance(body, dict):
        rows = body.get("data") or []
    elif isinstance(body, list):
        rows = body
    else:
        return []
    out: list[Model] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        model_id = row.get("id") or row.get("name")
        if not isinstance(model_id, str) or not model_id:
            continue
        owned = row.get("owned_by")
        created = row.get("created")
        out.append(
            Model(
                id=model_id,
                owned_by=owned if isinstance(owned, str) else None,
                created=created if isinstance(created, int) else None,
            )
        )
    return out


def _merge(cp_models: list[Model], inference_models: list[Model]) -> list[Model]:
    by_id: dict[str, Model] = {item.id: item for item in cp_models}
    for item in inference_models:
        by_id.setdefault(item.id, item)
    return list(by_id.values())


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

    def list(self, **kwargs: Any) -> ModelPage:
        del kwargs
        cp_body = self._transport.request("GET", "/v1/models")
        inference: list[Model] = []
        try:
            inf_body = self._transport.request(
                "GET", f"{self._transport.cfg.inference_url}/v1/models"
            )
            inference = _from_openai_list(inf_body)
        except APIError:
            pass
        return ModelPage(_merge(_from_cp_catalog(cp_body), inference))

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

    async def list(self, **kwargs: Any) -> ModelPage:
        del kwargs
        cp_body = await self._transport.request("GET", "/v1/models")
        inference: list[Model] = []
        try:
            inf_body = await self._transport.request(
                "GET", f"{self._transport.cfg.inference_url}/v1/models"
            )
            inference = _from_openai_list(inf_body)
        except APIError:
            pass
        return ModelPage(_merge(_from_cp_catalog(cp_body), inference))

    async def retrieve(self, model: str, **kwargs: Any) -> Any:
        return await self._models.retrieve(model, **kwargs)
