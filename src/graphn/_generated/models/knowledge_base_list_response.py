from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_base import KnowledgeBase


T = TypeVar("T", bound="KnowledgeBaseListResponse")


@_attrs_define
class KnowledgeBaseListResponse:
    """
    Attributes:
        items (list[KnowledgeBase]):
        has_more (bool):
        next_cursor (str | Unset):
        total (int | Unset): Matching item count, returned on the first page.
    """

    items: list[KnowledgeBase]
    has_more: bool
    next_cursor: str | Unset = UNSET
    total: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        has_more = self.has_more

        next_cursor = self.next_cursor

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "has_more": has_more,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_base import KnowledgeBase

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = KnowledgeBase.from_dict(items_item_data)

            items.append(items_item)

        has_more = d.pop("has_more")

        next_cursor = d.pop("next_cursor", UNSET)

        total = d.pop("total", UNSET)

        knowledge_base_list_response = cls(
            items=items,
            has_more=has_more,
            next_cursor=next_cursor,
            total=total,
        )

        return knowledge_base_list_response
