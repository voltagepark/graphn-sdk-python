from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.validate_model_request_quantization import (
    ValidateModelRequestQuantization,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateModelRequest")


@_attrs_define
class ValidateModelRequest:
    """
    Attributes:
        huggingface_model_id (str):
        hf_token_secret_id (None | str | Unset): ID of a workspace secret holding a HuggingFace token.
        quantization (ValidateModelRequestQuantization | Unset):
        gpu_memory_utilization (float | Unset):  Default: 0.9.
        model_size_gb (int | None | Unset): Optional caller-supplied estimate of the on-disk weights size,
            in GiB. When provided, the platform sizes the model-weights PVC
            from this hint instead of waiting for a HuggingFace head-bytes
            probe; useful for very large models where the probe would
            otherwise stall the validate response.
    """

    huggingface_model_id: str
    hf_token_secret_id: None | str | Unset = UNSET
    quantization: ValidateModelRequestQuantization | Unset = UNSET
    gpu_memory_utilization: float | Unset = 0.9
    model_size_gb: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        huggingface_model_id = self.huggingface_model_id

        hf_token_secret_id: None | str | Unset
        if isinstance(self.hf_token_secret_id, Unset):
            hf_token_secret_id = UNSET
        else:
            hf_token_secret_id = self.hf_token_secret_id

        quantization: str | Unset = UNSET
        if not isinstance(self.quantization, Unset):
            quantization = self.quantization.value

        gpu_memory_utilization = self.gpu_memory_utilization

        model_size_gb: int | None | Unset
        if isinstance(self.model_size_gb, Unset):
            model_size_gb = UNSET
        else:
            model_size_gb = self.model_size_gb

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "huggingface_model_id": huggingface_model_id,
            }
        )
        if hf_token_secret_id is not UNSET:
            field_dict["hf_token_secret_id"] = hf_token_secret_id
        if quantization is not UNSET:
            field_dict["quantization"] = quantization
        if gpu_memory_utilization is not UNSET:
            field_dict["gpu_memory_utilization"] = gpu_memory_utilization
        if model_size_gb is not UNSET:
            field_dict["model_size_gb"] = model_size_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        huggingface_model_id = d.pop("huggingface_model_id")

        def _parse_hf_token_secret_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hf_token_secret_id = _parse_hf_token_secret_id(
            d.pop("hf_token_secret_id", UNSET)
        )

        _quantization = d.pop("quantization", UNSET)
        quantization: ValidateModelRequestQuantization | Unset
        if isinstance(_quantization, Unset):
            quantization = UNSET
        else:
            quantization = ValidateModelRequestQuantization(_quantization)

        gpu_memory_utilization = d.pop("gpu_memory_utilization", UNSET)

        def _parse_model_size_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        model_size_gb = _parse_model_size_gb(d.pop("model_size_gb", UNSET))

        validate_model_request = cls(
            huggingface_model_id=huggingface_model_id,
            hf_token_secret_id=hf_token_secret_id,
            quantization=quantization,
            gpu_memory_utilization=gpu_memory_utilization,
            model_size_gb=model_size_gb,
        )

        return validate_model_request
