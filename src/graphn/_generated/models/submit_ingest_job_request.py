from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.ingest_item_input import IngestItemInput


T = TypeVar("T", bound="SubmitIngestJobRequest")


@_attrs_define
class SubmitIngestJobRequest:
    """
    Attributes:
        items (list[IngestItemInput]):
    """

    items: list[IngestItemInput]

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
        from ..models.ingest_item_input import IngestItemInput

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = IngestItemInput.from_dict(items_item_data)

            items.append(items_item)

        submit_ingest_job_request = cls(
            items=items,
        )

        return submit_ingest_job_request
