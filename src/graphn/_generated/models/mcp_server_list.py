from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server import McpServer


T = TypeVar("T", bound="McpServerList")


@_attrs_define
class McpServerList:
    """
    Attributes:
        items (list[McpServer]):
        count (int):
        continue_token (str | Unset):
    """

    items: list[McpServer]
    count: int
    continue_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        count = self.count

        continue_token = self.continue_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "count": count,
            }
        )
        if continue_token is not UNSET:
            field_dict["continue_token"] = continue_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_server import McpServer

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = McpServer.from_dict(items_item_data)

            items.append(items_item)

        count = d.pop("count")

        continue_token = d.pop("continue_token", UNSET)

        mcp_server_list = cls(
            items=items,
            count=count,
            continue_token=continue_token,
        )

        mcp_server_list.additional_properties = d
        return mcp_server_list

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
