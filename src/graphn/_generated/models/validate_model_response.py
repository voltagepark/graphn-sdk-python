from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    """

    valid: bool
    error: None | str | Unset = UNSET
    architectures: list[str] | Unset = UNSET
    supports_mtp: bool | Unset = UNSET
    num_params: int | None | Unset = UNSET
    estimated_memory_gb: float | None | Unset = UNSET
    max_context_length: int | None | Unset = UNSET
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

        validate_model_response = cls(
            valid=valid,
            error=error,
            architectures=architectures,
            supports_mtp=supports_mtp,
            num_params=num_params,
            estimated_memory_gb=estimated_memory_gb,
            max_context_length=max_context_length,
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
