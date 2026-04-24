"""Ergonomic custom-model resource.

Wraps the raw control-plane endpoints with:

* Typed return values (Pydantic :class:`CustomModel` etc.)
* Auto-paginating :class:`SyncPage` / :class:`AsyncPage` for ``list``
* Polling helpers (:meth:`CustomModels.wait_until_ready` /
  :meth:`AsyncCustomModels.wait_until_ready`) that block until the
  model reaches a terminal state.

The plan deliberately keeps the inference path on the official
``openai`` SDK; this module only covers the lifecycle endpoints
exposed by the graphn-cp control plane.
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Iterable, Mapping
from typing import Any

from graphn._exceptions import APIError
from graphn._pagination import AsyncPage, RawPage, SyncPage
from graphn._transport import AsyncTransport, SyncTransport
from graphn.custom_models.types import (
    Capability,
    CustomModel,
    CustomModelAccess,
    CustomModelStatus,
    GpuHoursResponse,
    Quantization,
    SupportedArchitectures,
    ValidateModelResponse,
    WeightSource,
)

_TERMINAL_STATUSES: frozenset[CustomModelStatus] = frozenset({"ready", "failed"})

_DEFAULT_POLL_INTERVAL_SECONDS = 5.0
_DEFAULT_WAIT_TIMEOUT_SECONDS = 1800.0  # 30 minutes


def _build_create_body(
    *,
    name: str,
    huggingface_model_id: str | None,
    weight_source: WeightSource,
    display_name: str | None,
    s3_url: str | None,
    s3_role_arn: str | None,
    hf_token_secret_id: str | None,
    gpu_count: int | None,
    max_model_len: int | None,
    gpu_memory_utilization: float | None,
    quantization: Quantization | None,
    capabilities: Iterable[Capability] | None,
    min_replicas: int | None,
    max_replicas: int | None,
    cooldown_seconds: int | None,
    extra: Mapping[str, Any] | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"name": name, "weight_source": weight_source}
    if display_name is not None:
        body["display_name"] = display_name
    if huggingface_model_id is not None:
        body["huggingface_model_id"] = huggingface_model_id
    if s3_url is not None:
        body["s3_url"] = s3_url
    if s3_role_arn is not None:
        body["s3_role_arn"] = s3_role_arn
    if hf_token_secret_id is not None:
        body["hf_token_secret_id"] = hf_token_secret_id
    if gpu_count is not None:
        body["gpu_count"] = gpu_count
    if max_model_len is not None:
        body["max_model_len"] = max_model_len
    if gpu_memory_utilization is not None:
        body["gpu_memory_utilization"] = gpu_memory_utilization
    if quantization is not None:
        body["quantization"] = quantization
    if capabilities is not None:
        body["capabilities"] = list(capabilities)
    if min_replicas is not None:
        body["min_replicas"] = min_replicas
    if max_replicas is not None:
        body["max_replicas"] = max_replicas
    if cooldown_seconds is not None:
        body["cooldown_seconds"] = cooldown_seconds
    if extra:
        body.update(extra)
    return body


def _build_validate_body(
    *,
    huggingface_model_id: str,
    hf_token_secret_id: str | None,
    quantization: Quantization | None,
    gpu_memory_utilization: float | None,
) -> dict[str, Any]:
    body: dict[str, Any] = {"huggingface_model_id": huggingface_model_id}
    if hf_token_secret_id is not None:
        body["hf_token_secret_id"] = hf_token_secret_id
    if quantization is not None:
        body["quantization"] = quantization
    if gpu_memory_utilization is not None:
        body["gpu_memory_utilization"] = gpu_memory_utilization
    return body


def _list_params(limit: int | None, continue_token: str | None) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if continue_token is not None:
        params["continue_token"] = continue_token
    return params


class CustomModels:
    """Synchronous custom-model resource."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        name: str,
        huggingface_model_id: str | None = None,
        weight_source: WeightSource = "huggingface",
        display_name: str | None = None,
        s3_url: str | None = None,
        s3_role_arn: str | None = None,
        hf_token_secret_id: str | None = None,
        gpu_count: int | None = None,
        max_model_len: int | None = None,
        gpu_memory_utilization: float | None = None,
        quantization: Quantization | None = None,
        capabilities: Iterable[Capability] | None = None,
        min_replicas: int | None = None,
        max_replicas: int | None = None,
        cooldown_seconds: int | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> CustomModel:
        body = _build_create_body(
            name=name,
            huggingface_model_id=huggingface_model_id,
            weight_source=weight_source,
            display_name=display_name,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            hf_token_secret_id=hf_token_secret_id,
            gpu_count=gpu_count,
            max_model_len=max_model_len,
            gpu_memory_utilization=gpu_memory_utilization,
            quantization=quantization,
            capabilities=capabilities,
            min_replicas=min_replicas,
            max_replicas=max_replicas,
            cooldown_seconds=cooldown_seconds,
            extra=extra,
        )
        data = self._transport.request(
            "POST",
            self._transport.cp_path("custom-models"),
            json=body,
            idempotency_key=idempotency_key,
        )
        return CustomModel.model_validate(data)

    def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> SyncPage[CustomModel]:
        def fetch(token: str | None) -> RawPage[CustomModel]:
            data = self._transport.request(
                "GET",
                self._transport.cp_path("custom-models"),
                params=_list_params(limit, token),
            )
            return RawPage.from_response(data or {}, CustomModel.model_validate)

        first = fetch(continue_token)
        return SyncPage(first=first, fetch_next=fetch)

    def get(self, model_id: str) -> CustomModel:
        data = self._transport.request(
            "GET", self._transport.cp_path("custom-models", model_id)
        )
        return CustomModel.model_validate(data)

    def delete(self, model_id: str) -> None:
        self._transport.request(
            "DELETE", self._transport.cp_path("custom-models", model_id)
        )

    def refresh(self, model_id: str) -> CustomModel:
        data = self._transport.request(
            "POST", self._transport.cp_path("custom-models", model_id, "refresh")
        )
        return CustomModel.model_validate(data)

    def wake(self, model_id: str) -> CustomModel:
        data = self._transport.request(
            "POST", self._transport.cp_path("custom-models", model_id, "wake")
        )
        return CustomModel.model_validate(data)

    def gpu_hours(self, model_id: str) -> GpuHoursResponse:
        data = self._transport.request(
            "GET", self._transport.cp_path("custom-models", model_id, "gpu-hours")
        )
        return GpuHoursResponse.model_validate(data)

    def access(self) -> CustomModelAccess:
        data = self._transport.request(
            "GET", self._transport.cp_path("custom-models", "access")
        )
        return CustomModelAccess.model_validate(data)

    def supported_architectures(self) -> SupportedArchitectures:
        data = self._transport.request(
            "GET",
            self._transport.cp_path("custom-models", "supported-architectures"),
        )
        return SupportedArchitectures.model_validate(data)

    def validate(
        self,
        *,
        huggingface_model_id: str,
        hf_token_secret_id: str | None = None,
        quantization: Quantization | None = None,
        gpu_memory_utilization: float | None = None,
    ) -> ValidateModelResponse:
        body = _build_validate_body(
            huggingface_model_id=huggingface_model_id,
            hf_token_secret_id=hf_token_secret_id,
            quantization=quantization,
            gpu_memory_utilization=gpu_memory_utilization,
        )
        data = self._transport.request(
            "POST",
            self._transport.cp_path("custom-models", "validate"),
            json=body,
        )
        return ValidateModelResponse.model_validate(data)

    def wait_until_ready(
        self,
        model_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> CustomModel:
        """Block until the model reaches a terminal status.

        Polls :meth:`refresh` every ``poll_interval`` seconds until
        ``status`` is ``ready`` or ``failed`` (the only terminal
        states), or until ``timeout`` seconds have elapsed.

        Raises
        ------
        TimeoutError
            If ``timeout`` elapses before the model reaches a terminal
            state.
        graphn.APIError
            If ``status`` is ``failed``; the error's ``message`` is
            the model's ``error_message``.
        """

        deadline = time.monotonic() + timeout
        while True:
            model = self.refresh(model_id)
            if model.status in _TERMINAL_STATUSES:
                if model.status == "failed":
                    raise APIError(
                        model.error_message
                        or f"custom model {model_id} failed without details",
                        status_code=0,
                        code="custom_model_deployment_failed",
                        details={"model_id": model_id},
                    )
                return model
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"custom model {model_id} did not reach 'ready' within "
                    f"{timeout:.0f}s (last status: {model.status!r})"
                )
            time.sleep(poll_interval)


class AsyncCustomModels:
    """Asynchronous custom-model resource. Mirrors :class:`CustomModels`."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        name: str,
        huggingface_model_id: str | None = None,
        weight_source: WeightSource = "huggingface",
        display_name: str | None = None,
        s3_url: str | None = None,
        s3_role_arn: str | None = None,
        hf_token_secret_id: str | None = None,
        gpu_count: int | None = None,
        max_model_len: int | None = None,
        gpu_memory_utilization: float | None = None,
        quantization: Quantization | None = None,
        capabilities: Iterable[Capability] | None = None,
        min_replicas: int | None = None,
        max_replicas: int | None = None,
        cooldown_seconds: int | None = None,
        extra: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> CustomModel:
        body = _build_create_body(
            name=name,
            huggingface_model_id=huggingface_model_id,
            weight_source=weight_source,
            display_name=display_name,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            hf_token_secret_id=hf_token_secret_id,
            gpu_count=gpu_count,
            max_model_len=max_model_len,
            gpu_memory_utilization=gpu_memory_utilization,
            quantization=quantization,
            capabilities=capabilities,
            min_replicas=min_replicas,
            max_replicas=max_replicas,
            cooldown_seconds=cooldown_seconds,
            extra=extra,
        )
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("custom-models"),
            json=body,
            idempotency_key=idempotency_key,
        )
        return CustomModel.model_validate(data)

    async def list(
        self,
        *,
        limit: int | None = None,
        continue_token: str | None = None,
    ) -> AsyncPage[CustomModel]:
        """Return the first page; ``async for`` to auto-paginate."""

        async def fetch(token: str | None) -> RawPage[CustomModel]:
            data = await self._transport.request(
                "GET",
                self._transport.cp_path("custom-models"),
                params=_list_params(limit, token),
            )
            return RawPage.from_response(data or {}, CustomModel.model_validate)

        first = await fetch(continue_token)
        return AsyncPage(first=first, fetch_next=fetch)

    async def get(self, model_id: str) -> CustomModel:
        data = await self._transport.request(
            "GET", self._transport.cp_path("custom-models", model_id)
        )
        return CustomModel.model_validate(data)

    async def delete(self, model_id: str) -> None:
        await self._transport.request(
            "DELETE", self._transport.cp_path("custom-models", model_id)
        )

    async def refresh(self, model_id: str) -> CustomModel:
        data = await self._transport.request(
            "POST", self._transport.cp_path("custom-models", model_id, "refresh")
        )
        return CustomModel.model_validate(data)

    async def wake(self, model_id: str) -> CustomModel:
        data = await self._transport.request(
            "POST", self._transport.cp_path("custom-models", model_id, "wake")
        )
        return CustomModel.model_validate(data)

    async def gpu_hours(self, model_id: str) -> GpuHoursResponse:
        data = await self._transport.request(
            "GET", self._transport.cp_path("custom-models", model_id, "gpu-hours")
        )
        return GpuHoursResponse.model_validate(data)

    async def access(self) -> CustomModelAccess:
        data = await self._transport.request(
            "GET", self._transport.cp_path("custom-models", "access")
        )
        return CustomModelAccess.model_validate(data)

    async def supported_architectures(self) -> SupportedArchitectures:
        data = await self._transport.request(
            "GET",
            self._transport.cp_path("custom-models", "supported-architectures"),
        )
        return SupportedArchitectures.model_validate(data)

    async def validate(
        self,
        *,
        huggingface_model_id: str,
        hf_token_secret_id: str | None = None,
        quantization: Quantization | None = None,
        gpu_memory_utilization: float | None = None,
    ) -> ValidateModelResponse:
        body = _build_validate_body(
            huggingface_model_id=huggingface_model_id,
            hf_token_secret_id=hf_token_secret_id,
            quantization=quantization,
            gpu_memory_utilization=gpu_memory_utilization,
        )
        data = await self._transport.request(
            "POST",
            self._transport.cp_path("custom-models", "validate"),
            json=body,
        )
        return ValidateModelResponse.model_validate(data)

    async def wait_until_ready(
        self,
        model_id: str,
        *,
        timeout: float = _DEFAULT_WAIT_TIMEOUT_SECONDS,
        poll_interval: float = _DEFAULT_POLL_INTERVAL_SECONDS,
    ) -> CustomModel:
        loop = asyncio.get_event_loop()
        deadline = loop.time() + timeout
        while True:
            model = await self.refresh(model_id)
            if model.status in _TERMINAL_STATUSES:
                if model.status == "failed":
                    raise APIError(
                        model.error_message
                        or f"custom model {model_id} failed without details",
                        status_code=0,
                        code="custom_model_deployment_failed",
                        details={"model_id": model_id},
                    )
                return model
            if loop.time() >= deadline:
                raise TimeoutError(
                    f"custom model {model_id} did not reach 'ready' within "
                    f"{timeout:.0f}s (last status: {model.status!r})"
                )
            await asyncio.sleep(poll_interval)
