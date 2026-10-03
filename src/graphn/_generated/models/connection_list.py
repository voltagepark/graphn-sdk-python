from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection import Connection


T = TypeVar("T", bound="ConnectionList")


@_attrs_define
class ConnectionList:
    """
    Attributes:
        items (list[Connection]):
        count (int):
        continue_token (str | Unset):
    """

    items: list[Connection]
    count: int
    continue_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        count = self.count

        continue_token = self.continue_token

        field_dict: dict[str, Any] = {}

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
        from ..models.connection import Connection

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Connection.from_dict(items_item_data)

            items.append(items_item)

        count = d.pop("count")

        continue_token = d.pop("continue_token", UNSET)

        connection_list = cls(
            items=items,
            count=count,
            continue_token=continue_token,
        )

        return connection_list
