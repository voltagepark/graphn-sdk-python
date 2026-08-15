from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="ToolReference")


@_attrs_define
class ToolReference:
    """
    Attributes:
        server_id (str):
        tool_name (str):
    """

    server_id: str
    tool_name: str

    def to_dict(self) -> dict[str, Any]:
        server_id = self.server_id

        tool_name = self.tool_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_id": server_id,
                "tool_name": tool_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        server_id = d.pop("server_id")

        tool_name = d.pop("tool_name")

        tool_reference = cls(
            server_id=server_id,
            tool_name=tool_name,
        )

        return tool_reference
