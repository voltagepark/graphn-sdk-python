from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_model_response_artifact_type import (
    ValidateModelResponseArtifactType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateModelResponse")


@_attrs_define
class ValidateModelResponse:
    """
    Attributes:
        valid (bool):
        error (None | str | Unset): Populated when `valid` is `false`.
        architectures (list[str] | Unset):
        supports_mtp (bool | Unset): Whether the model architecture supports native MTP speculative decoding.
        num_params (int | None | Unset):
        estimated_memory_gb (float | None | Unset):
        max_context_length (int | None | Unset):
        artifact_type (ValidateModelResponseArtifactType | Unset): `lora` when AF detected an `adapter_config.json` in
            the HuggingFace
            repo at validate time; `base` otherwise (the default — what every
            existing caller saw before the LoRA auto-detect work landed). Use
            this to branch in client code without keeping track of two
            different `weight_source` enum values for the HF case.

            When `artifact_type=lora`, the `architectures`, `num_params`,
            `estimated_memory_gb`, and `max_context_length` fields describe
            the **base** model (resolved from `adapter_config.json`), not
            the adapter itself.
             Default: ValidateModelResponseArtifactType.BASE.
        detected_base_model_id (None | str | Unset): Populated only when `artifact_type=lora`. The base model id read
            from `adapter_config.json::base_model_name_or_path`. Use to pin
            the base on subsequent deploy calls or to surface a "detected as
            LoRA adapter for X" affordance in your UI.
        lora_rank (int | None | Unset): Populated only when `artifact_type=lora`. The `r` value from
            `adapter_config.json` (LoRA rank).
    """

    valid: bool
    error: None | str | Unset = UNSET
    architectures: list[str] | Unset = UNSET
    supports_mtp: bool | Unset = UNSET
    num_params: int | None | Unset = UNSET
    estimated_memory_gb: float | None | Unset = UNSET
    max_context_length: int | None | Unset = UNSET
    artifact_type: ValidateModelResponseArtifactType | Unset = (
        ValidateModelResponseArtifactType.BASE
    )
    detected_base_model_id: None | str | Unset = UNSET
    lora_rank: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        architectures: list[str] | Unset = UNSET
        if not isinstance(self.architectures, Unset):
            architectures = self.architectures

        supports_mtp = self.supports_mtp

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

        max_context_length: int | None | Unset
        if isinstance(self.max_context_length, Unset):
            max_context_length = UNSET
        else:
            max_context_length = self.max_context_length

        artifact_type: str | Unset = UNSET
        if not isinstance(self.artifact_type, Unset):
            artifact_type = self.artifact_type.value

        detected_base_model_id: None | str | Unset
        if isinstance(self.detected_base_model_id, Unset):
            detected_base_model_id = UNSET
        else:
            detected_base_model_id = self.detected_base_model_id

        lora_rank: int | None | Unset
        if isinstance(self.lora_rank, Unset):
            lora_rank = UNSET
        else:
            lora_rank = self.lora_rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if architectures is not UNSET:
            field_dict["architectures"] = architectures
        if supports_mtp is not UNSET:
            field_dict["supports_mtp"] = supports_mtp
        if num_params is not UNSET:
            field_dict["num_params"] = num_params
        if estimated_memory_gb is not UNSET:
            field_dict["estimated_memory_gb"] = estimated_memory_gb
        if max_context_length is not UNSET:
            field_dict["max_context_length"] = max_context_length
        if artifact_type is not UNSET:
            field_dict["artifact_type"] = artifact_type
        if detected_base_model_id is not UNSET:
            field_dict["detected_base_model_id"] = detected_base_model_id
        if lora_rank is not UNSET:
            field_dict["lora_rank"] = lora_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        architectures = cast(list[str], d.pop("architectures", UNSET))

        supports_mtp = d.pop("supports_mtp", UNSET)

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

        def _parse_max_context_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_context_length = _parse_max_context_length(
            d.pop("max_context_length", UNSET)
        )

        _artifact_type = d.pop("artifact_type", UNSET)
        artifact_type: ValidateModelResponseArtifactType | Unset
        if isinstance(_artifact_type, Unset):
            artifact_type = UNSET
        else:
            artifact_type = ValidateModelResponseArtifactType(_artifact_type)

        def _parse_detected_base_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detected_base_model_id = _parse_detected_base_model_id(
            d.pop("detected_base_model_id", UNSET)
        )

        def _parse_lora_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lora_rank = _parse_lora_rank(d.pop("lora_rank", UNSET))

        validate_model_response = cls(
            valid=valid,
            error=error,
            architectures=architectures,
            supports_mtp=supports_mtp,
            num_params=num_params,
            estimated_memory_gb=estimated_memory_gb,
            max_context_length=max_context_length,
            artifact_type=artifact_type,
            detected_base_model_id=detected_base_model_id,
            lora_rank=lora_rank,
        )

        validate_model_response.additional_properties = d
        return validate_model_response

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
