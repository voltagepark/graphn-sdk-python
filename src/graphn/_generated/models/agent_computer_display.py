from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentComputerDisplay")


@_attrs_define
class AgentComputerDisplay:
    """
    Attributes:
        width (int | Unset):
        height (int | Unset):
    """

    width: int | Unset = UNSET
    height: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        agent_computer_display = cls(
            width=width,
            height=height,
        )

        return agent_computer_display
