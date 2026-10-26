"""LoRA adapters on a shared base.

A shared LoRA base is a custom model created with ``lora_enabled=True``.
Adapters attached to it run on the base's replicas and are called as
their own models, ``custom:<adapter-id>``, through ``chat.completions``.
"""

from __future__ import annotations

import asyncio
import time
from typing import Any

from graphn._exceptions import APIError, NotFoundError, ValidationError
from graphn._transport import AsyncTransport, SyncTransport
from graphn.custom_models.types import CustomModel, WeightSource

_DEFAULT_POLL_INTERVAL_SECONDS = 5.0
_DEFAULT_WAIT_TIMEOUT_SECONDS = 1800.0  # 30 minutes


def _build_attach_body(
    *,
    huggingface_model_id: str | None,
    s3_url: str | None,
    s3_role_arn: str | None,
    s3_external_id: str | None,
    hf_token_secret_id: str | None,
    name: str | None,
    display_name: str | None,
    weight_source: WeightSource | None,
    acknowledge_base_mismatch: bool,
) -> dict[str, Any]:
    if bool(huggingface_model_id) == bool(s3_url):
        raise ValidationError(
            "attach() takes exactly one of huggingface_model_id or s3_url.",
            status_code=422,
            code="adapter_source_required",
            details={},
        )
    if weight_source is None:
        if s3_url is None:
            weight_source = "huggingface"
        elif s3_role_arn is not None:
            weight_source = "s3_assume_role"
        else:
            weight_source = "s3_presigned"
    body: dict[str, Any] = {"weight_source": weight_source}
    if name is not None:
        body["name"] = name
    if display_name is not None:
        body["display_name"] = display_name
    if huggingface_model_id is not None:
        body["huggingface_model_id"] = huggingface_model_id
    if hf_token_secret_id is not None:
        body["hf_token_secret_id"] = hf_token_secret_id
    if s3_url is not None:
        body["s3_url"] = s3_url
    if s3_role_arn is not None:
        body["s3_role_arn"] = s3_role_arn
    if s3_external_id is not None:
        body["s3_external_id"] = s3_external_id
    if acknowledge_base_mismatch:
        body["base_mismatch_acknowledged"] = True
    return body


def _items(data: Any) -> list[CustomModel]:
    return [CustomModel.model_validate(item) for item in (data or {}).get("items") or []]


def _failed(model: CustomModel) -> APIError:
    return APIError(
        model.error_message or f"adapter {model.id} failed without details",
        status_code=0,
        code="custom_model_adapter_failed",
        details={"model_id": model.id, "parent_model_id": model.parent_model_id},
    )


class CustomModelAdapters:
    """Synchronous adapter resource, reached as ``client.custom_models.adapters``."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def attach(
        self,
        base_id: str,
        *,
        huggingface_model_id: str | None = None,
        s3_url: str | None = None,
        s3_role_arn: str | None = None,
        s3_external_id: str | None = None,
        hf_token_secret_id: str | None = None,
        name: str | None = None,
        display_name: str | None = None,
        weight_source: WeightSource | None = None,
        acknowledge_base_mismatch: bool = False,
        idempotency_key: str | None = None,
    ) -> CustomModel:
        """Attach a LoRA adapter to the shared base ``base_id``.

        Pass a Hugging Face repo, or an ``s3_url``: a presigned URL to a
        ``.tar.gz`` of the adapter, or an ``s3://`` prefix ending in ``/``
        together with ``s3_role_arn``. ``weight_source`` is inferred from
        those. Returns at once with the adapter ``pending``; use
        :meth:`wait_until_ready` to block until it can serve.

        ``acknowledge_base_mismatch`` accepts an adapter whose
        ``adapter_config.json`` names a different base than this one's
        Hugging Face ID. A base deployed from S3 has no ID to compare.
        """

        body = _build_attach_body(
            huggingface_model_id=huggingface_model_id,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            s3_external_id=s3_external_id,
            hf_token_secret_id=hf_token_secret_id,
            name=name,
            display_name=display_name,
            weight_source=weight_source,
            acknowledge_base_mismatch=acknowledge_base_mismatch,
        )
        data = self._transport.request(
            "POST",
            self._transport.cp_path("custom-models", base_id, "adapters"),
            json=body,
            idempotency_key=idempotency_key,
        )
        return CustomModel.model_validate(data)

    def list(self, base_id: str) -> list[CustomModel]:
        """Every adapter on the base, oldest first, including failed and deleting ones."""

        data = self._transport.request(
            "GET", self._transport.cp_path("custom-models", base_id, "adapters")
        )
        return _items(data)

    def get(self, adapter_id: str) -> CustomModel:
        data = self._transport.request("GET", self._transport.cp_path("custom-models", adapter_id))
        return CustomModel.model_validate(data)

    def delete(self, adapter_id: str) -> None:
        """Start removing an adapter. It reads ``deleting`` while the base
        finishes its in-flight requests and unloads it; see
        :meth:`wait_until_deleted`."""

        self._transport.request("DELETE", self._transport.cp_path("custom-models", adapter_id))

    def wait_until_ready(
        self,
        adapter_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> CustomModel:
        """Block until the adapter is ``ready``.

        Raises :class:`graphn.APIError` if it fails (the message starts with
        a reason code such as ``ADAPTER_RANK_EXCEEDS_BASE``), and
        :class:`TimeoutError` if ``timeout`` elapses first.
        """

        deadline = time.monotonic() + timeout
        while True:
            model = self.get(adapter_id)
            if model.status == "ready":
                return model
            if model.status == "failed":
                raise _failed(model)
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"adapter {adapter_id} did not reach 'ready' within "
                    f"{timeout:.0f}s (last status: {model.status!r})"
                )
            time.sleep(poll_interval)

    def wait_until_deleted(
        self,
        adapter_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> None:
        """Block until a deleted adapter is gone. A base can only be
        deleted once all its adapters are."""

        deadline = time.monotonic() + timeout
        while True:
            try:
                model = self.get(adapter_id)
            except NotFoundError:
                return
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"adapter {adapter_id} was not removed within "
                    f"{timeout:.0f}s (last status: {model.status!r})"
                )
            time.sleep(poll_interval)


class AsyncCustomModelAdapters:
    """Asynchronous mirror of :class:`CustomModelAdapters`."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def attach(
        self,
        base_id: str,
        *,
        huggingface_model_id: str | None = None,
        s3_url: str | None = None,
        s3_role_arn: str | None = None,
        s3_external_id: str | None = None,
        hf_token_secret_id: str | None = None,
        name: str | None = None,
        display_name: str | None = None,
        weight_source: WeightSource | None = None,
        acknowledge_base_mismatch: bool = False,
        idempotency_key: str | None = None,
    ) -> CustomModel:
        body = _build_attach_body(
            huggingface_model_id=huggingface_model_id,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            s3_external_id=s3_external_id,
            hf_token_secret_id=hf_token_secret_id,
            name=name,
            display_name=display_name,
            weight_source=weight_source,
            acknowledge_base_mismatch=acknowledge_base_mismatch,
        )
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("custom-models", base_id, "adapters"),
            json=body,
            idempotency_key=idempotency_key,
        )
        return CustomModel.model_validate(data)

    async def list(self, base_id: str) -> list[CustomModel]:
        data = await self._transport.request(
            "GET", self._transport.cp_path("custom-models", base_id, "adapters")
        )
        return _items(data)

    async def get(self, adapter_id: str) -> CustomModel:
        data = await self._transport.request(
            "GET", self._transport.cp_path("custom-models", adapter_id)
        )
        return CustomModel.model_validate(data)

    async def delete(self, adapter_id: str) -> None:
        await self._transport.request(
            "DELETE", self._transport.cp_path("custom-models", adapter_id)
        )

    async def wait_until_ready(
        self,
        adapter_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> CustomModel:
        loop = asyncio.get_event_loop()
        deadline = loop.time() + timeout
        while True:
            model = await self.get(adapter_id)
            if model.status == "ready":
                return model
            if model.status == "failed":
                raise _failed(model)
            if loop.time() >= deadline:
                raise TimeoutError(
                    f"adapter {adapter_id} did not reach 'ready' within "
                    f"{timeout:.0f}s (last status: {model.status!r})"
                )
            await asyncio.sleep(poll_interval)

    async def wait_until_deleted(
        self,
        adapter_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> None:
        loop = asyncio.get_event_loop()
        deadline = loop.time() + timeout
        while True:
            try:
                model = await self.get(adapter_id)
            except NotFoundError:
                return
            if loop.time() >= deadline:
                raise TimeoutError(
                    f"adapter {adapter_id} was not removed within "
                    f"{timeout:.0f}s (last status: {model.status!r})"
                )
            await asyncio.sleep(poll_interval)
