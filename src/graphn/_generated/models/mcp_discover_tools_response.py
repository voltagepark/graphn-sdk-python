from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_definition import ToolDefinition


T = TypeVar("T", bound="McpDiscoverToolsResponse")


@_attrs_define
class McpDiscoverToolsResponse:
    """
    Attributes:
        tools (list[ToolDefinition]):
        error (str | Unset):
    """

    tools: list[ToolDefinition]
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tools": tools,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tool_definition import ToolDefinition

        d = dict(src_dict)
        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = ToolDefinition.from_dict(tools_item_data)

            tools.append(tools_item)

        error = d.pop("error", UNSET)

        mcp_discover_tools_response = cls(
            tools=tools,
            error=error,
        )

        mcp_discover_tools_response.additional_properties = d
        return mcp_discover_tools_response

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
