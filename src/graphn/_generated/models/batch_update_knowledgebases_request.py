from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.batch_update_item import BatchUpdateItem


T = TypeVar("T", bound="BatchUpdateKnowledgebasesRequest")


@_attrs_define
class BatchUpdateKnowledgebasesRequest:
    """
    Attributes:
        items (list[BatchUpdateItem]):
    """

    items: list[BatchUpdateItem]

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_update_item import BatchUpdateItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = BatchUpdateItem.from_dict(items_item_data)

            items.append(items_item)

        batch_update_knowledgebases_request = cls(
            items=items,
        )

        return batch_update_knowledgebases_request
