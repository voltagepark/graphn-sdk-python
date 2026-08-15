from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolTestResponse")


@_attrs_define
class ToolTestResponse:
    """
    Attributes:
        success (bool):
        output (Any | Unset):
        error (str | Unset):
        duration_ms (int | Unset):
    """

    success: bool
    output: Any | Unset = UNSET
    error: str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        output = self.output

        error = self.error

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        output = d.pop("output", UNSET)

        error = d.pop("error", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        tool_test_response = cls(
            success=success,
            output=output,
            error=error,
            duration_ms=duration_ms,
        )

        tool_test_response.additional_properties = d
        return tool_test_response

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
