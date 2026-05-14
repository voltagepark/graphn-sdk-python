from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.capability import Capability
from ..models.custom_model_quantization import CustomModelQuantization
from ..models.custom_model_status import CustomModelStatus
from ..models.weight_source import WeightSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModel")


@_attrs_define
class CustomModel:
    """Public custom model record. Additional internal fields may be
    present in responses but are not documented and may change
    without notice. Generated SDKs ignore them.

        Attributes:
            id (str): Stable model identifier (`cm_...`).
            name (str): URL-safe model name. Pass this as the `model` field on
                `createChatCompletion` once `status` is `ready`.
            workspace_id (str):
            status (CustomModelStatus): Lifecycle state:
                - `pending`: record created, deployment not yet started
                - `deploying`: weights downloading, replicas booting
                - `ready`: at least one replica is serving (or scaled to zero with cooldown)
                - `failed`: deployment failed; see `error_message`
                - `deleting`: teardown in progress
            weight_source (WeightSource): Source of the model weights:
                - `huggingface`: download from HuggingFace using `huggingface_model_id`
                - `s3_presigned`: download from a presigned S3 URL
                - `s3_assume_role`: download from S3 using an assumed IAM role
            gpu_count (int): Number of GPUs allocated per replica.
            gpu_memory_utilization (float): Fraction of GPU memory the inference runtime is allowed to use.
            capabilities (list[Capability]):
            min_replicas (int): Minimum replicas to keep warm. `0` allows scale-to-zero.
            max_replicas (int): Maximum replicas the autoscaler may run.
            cooldown_seconds (int): Idle seconds before scaling down to `min_replicas`.
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            display_name (str | Unset): Human-friendly name for UI display.
            huggingface_model_id (str | Unset): Set when `weight_source` is `huggingface`.
            s3_url (None | str | Unset): Set when `weight_source` is `s3_presigned` or `s3_assume_role`.
            s3_role_arn (None | str | Unset): Set when `weight_source` is `s3_assume_role`.
            max_model_len (int | None | Unset): Maximum context length in tokens.
            quantization (CustomModelQuantization | Unset): Weight quantization scheme, if any.
            replicas_available (int | None | Unset): Currently serving replicas (live status).
            endpoint (None | str | Unset): Internal cluster endpoint serving this model. Informational only — clients should
                use `chat.completions` with the model's `name`.
            error_message (None | str | Unset): Populated when `status` is `failed`.
            num_params (int | None | Unset): Parameter count detected from the model config.
            estimated_memory_gb (float | None | Unset): Estimated GPU memory required for serving.
            architectures (list[str] | None | Unset): HuggingFace `architectures` field from `config.json`.
    """

    id: str
    name: str
    workspace_id: str
    status: CustomModelStatus
    weight_source: WeightSource
    gpu_count: int
    gpu_memory_utilization: float
    capabilities: list[Capability]
    min_replicas: int
    max_replicas: int
    cooldown_seconds: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    display_name: str | Unset = UNSET
    huggingface_model_id: str | Unset = UNSET
    s3_url: None | str | Unset = UNSET
    s3_role_arn: None | str | Unset = UNSET
    max_model_len: int | None | Unset = UNSET
    quantization: CustomModelQuantization | Unset = UNSET
    replicas_available: int | None | Unset = UNSET
    endpoint: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    num_params: int | None | Unset = UNSET
    estimated_memory_gb: float | None | Unset = UNSET
    architectures: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        workspace_id = self.workspace_id

        status = self.status.value

        weight_source = self.weight_source.value

        gpu_count = self.gpu_count

        gpu_memory_utilization = self.gpu_memory_utilization

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.value
            capabilities.append(capabilities_item)

        min_replicas = self.min_replicas

        max_replicas = self.max_replicas

        cooldown_seconds = self.cooldown_seconds

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        display_name = self.display_name

        huggingface_model_id = self.huggingface_model_id

        s3_url: None | str | Unset
        if isinstance(self.s3_url, Unset):
            s3_url = UNSET
        else:
            s3_url = self.s3_url

        s3_role_arn: None | str | Unset
        if isinstance(self.s3_role_arn, Unset):
            s3_role_arn = UNSET
        else:
            s3_role_arn = self.s3_role_arn

        max_model_len: int | None | Unset
        if isinstance(self.max_model_len, Unset):
            max_model_len = UNSET
        else:
            max_model_len = self.max_model_len

        quantization: str | Unset = UNSET
        if not isinstance(self.quantization, Unset):
            quantization = self.quantization.value

        replicas_available: int | None | Unset
        if isinstance(self.replicas_available, Unset):
            replicas_available = UNSET
        else:
            replicas_available = self.replicas_available

        endpoint: None | str | Unset
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        num_params: int | None | Unset
        if isinstance(self.num_params, Unset):
            num_params = UNSET
        else:
            num_params = self.num_params

        estimated_memory_gb: float | None | Unset
        if isinstance(self.estimated_memory_gb, Unset):
            estimated_memory_gb = UNSET
        else:
            estimated_memory_gb = self.estimated_memory_gb

        architectures: list[str] | None | Unset
        if isinstance(self.architectures, Unset):
            architectures = UNSET
        elif isinstance(self.architectures, list):
            architectures = self.architectures

        else:
            architectures = self.architectures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "workspace_id": workspace_id,
                "status": status,
                "weight_source": weight_source,
                "gpu_count": gpu_count,
                "gpu_memory_utilization": gpu_memory_utilization,
                "capabilities": capabilities,
                "min_replicas": min_replicas,
                "max_replicas": max_replicas,
                "cooldown_seconds": cooldown_seconds,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if huggingface_model_id is not UNSET:
            field_dict["huggingface_model_id"] = huggingface_model_id
        if s3_url is not UNSET:
            field_dict["s3_url"] = s3_url
        if s3_role_arn is not UNSET:
            field_dict["s3_role_arn"] = s3_role_arn
        if max_model_len is not UNSET:
            field_dict["max_model_len"] = max_model_len
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if replicas_available is not UNSET:
            field_dict["replicas_available"] = replicas_available
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if num_params is not UNSET:
            field_dict["num_params"] = num_params
        if estimated_memory_gb is not UNSET:
            field_dict["estimated_memory_gb"] = estimated_memory_gb
        if architectures is not UNSET:
            field_dict["architectures"] = architectures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        workspace_id = d.pop("workspace_id")

        status = CustomModelStatus(d.pop("status"))

        weight_source = WeightSource(d.pop("weight_source"))

        gpu_count = d.pop("gpu_count")

        gpu_memory_utilization = d.pop("gpu_memory_utilization")

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in _capabilities:
            capabilities_item = Capability(capabilities_item_data)

            capabilities.append(capabilities_item)

        min_replicas = d.pop("min_replicas")

        max_replicas = d.pop("max_replicas")

        cooldown_seconds = d.pop("cooldown_seconds")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        display_name = d.pop("display_name", UNSET)

        huggingface_model_id = d.pop("huggingface_model_id", UNSET)

        def _parse_s3_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_url = _parse_s3_url(d.pop("s3_url", UNSET))

        def _parse_s3_role_arn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_role_arn = _parse_s3_role_arn(d.pop("s3_role_arn", UNSET))

        def _parse_max_model_len(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_model_len = _parse_max_model_len(d.pop("max_model_len", UNSET))

        _quantization = d.pop("quantization", UNSET)
        quantization: CustomModelQuantization | Unset
        if isinstance(_quantization, Unset):
            quantization = UNSET
        else:
            quantization = CustomModelQuantization(_quantization)

        def _parse_replicas_available(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        replicas_available = _parse_replicas_available(
            d.pop("replicas_available", UNSET)
        )

        def _parse_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_num_params(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_params = _parse_num_params(d.pop("num_params", UNSET))

        def _parse_estimated_memory_gb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_memory_gb = _parse_estimated_memory_gb(
            d.pop("estimated_memory_gb", UNSET)
        )

        def _parse_architectures(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                architectures_type_0 = cast(list[str], data)

                return architectures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        architectures = _parse_architectures(d.pop("architectures", UNSET))

        custom_model = cls(
            id=id,
            name=name,
            workspace_id=workspace_id,
            status=status,
            weight_source=weight_source,
            gpu_count=gpu_count,
            gpu_memory_utilization=gpu_memory_utilization,
            capabilities=capabilities,
            min_replicas=min_replicas,
            max_replicas=max_replicas,
            cooldown_seconds=cooldown_seconds,
            created_at=created_at,
            updated_at=updated_at,
            display_name=display_name,
            huggingface_model_id=huggingface_model_id,
            s3_url=s3_url,
            s3_role_arn=s3_role_arn,
            max_model_len=max_model_len,
            quantization=quantization,
            replicas_available=replicas_available,
            endpoint=endpoint,
            error_message=error_message,
            num_params=num_params,
            estimated_memory_gb=estimated_memory_gb,
            architectures=architectures,
        )

        custom_model.additional_properties = d
        return custom_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
