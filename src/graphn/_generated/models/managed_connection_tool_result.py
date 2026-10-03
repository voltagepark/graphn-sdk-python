from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedConnectionToolResult")


@_attrs_define
class ManagedConnectionToolResult:
    """
    Attributes:
        success (bool):
        output (Any | Unset):
    """

    success: bool
    output: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        output = self.output

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        output = d.pop("output", UNSET)

        managed_connection_tool_result = cls(
            success=success,
            output=output,
        )

        return managed_connection_tool_result
