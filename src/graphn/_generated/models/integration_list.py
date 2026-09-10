from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.integration import Integration


T = TypeVar("T", bound="IntegrationList")


@_attrs_define
class IntegrationList:
    """
    Attributes:
        items (list[Integration]):
        count (int):
    """

    items: list[Integration]
    count: int

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.integration import Integration

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Integration.from_dict(items_item_data)

            items.append(items_item)

        count = d.pop("count")

        integration_list = cls(
            items=items,
            count=count,
        )

        return integration_list
