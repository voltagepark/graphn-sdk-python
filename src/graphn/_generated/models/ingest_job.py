from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingest_item import IngestItem
    from ..models.ingest_job_summary import IngestJobSummary


T = TypeVar("T", bound="IngestJob")


@_attrs_define
class IngestJob:
    """
    Attributes:
        id (str):
        kb_id (str):
        status (str):
        summary (IngestJobSummary):
        created_at (datetime.datetime):
        updated_at (datetime.datetime | Unset):
        items (list[IngestItem] | Unset):
    """

    id: str
    kb_id: str
    status: str
    summary: IngestJobSummary
    created_at: datetime.datetime
    updated_at: datetime.datetime | Unset = UNSET
    items: list[IngestItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kb_id = self.kb_id

        status = self.status

        summary = self.summary.to_dict()

        created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kb_id": kb_id,
                "status": status,
                "summary": summary,
                "created_at": created_at,
            }
        )
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ingest_item import IngestItem
        from ..models.ingest_job_summary import IngestJobSummary

        d = dict(src_dict)
        id = d.pop("id")

        kb_id = d.pop("kb_id")

        status = d.pop("status")

        summary = IngestJobSummary.from_dict(d.pop("summary"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _items = d.pop("items", UNSET)
        items: list[IngestItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = IngestItem.from_dict(items_item_data)

                items.append(items_item)

        ingest_job = cls(
            id=id,
            kb_id=kb_id,
            status=status,
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            items=items,
        )

        ingest_job.additional_properties = d
        return ingest_job

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
