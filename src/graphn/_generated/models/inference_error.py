from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_error_error import InferenceErrorError


T = TypeVar("T", bound="InferenceError")


@_attrs_define
class InferenceError:
    """OpenAI-style error envelope returned by the inference host. The
    shape mirrors the OpenAI API for compatibility with existing
    OpenAI client libraries.

        Attributes:
            error (InferenceErrorError | Unset):
    """

    error: InferenceErrorError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inference_error_error import InferenceErrorError

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: InferenceErrorError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = InferenceErrorError.from_dict(_error)

        inference_error = cls(
            error=error,
        )

        inference_error.additional_properties = d
        return inference_error

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
