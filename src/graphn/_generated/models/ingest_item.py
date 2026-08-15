from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestItem")


@_attrs_define
class IngestItem:
    """
    Attributes:
        id (str):
        job_id (str):
        item_index (int):
        url (str):
        status (str):
        created_at (datetime.datetime):
        filename (str | Unset):
        document_id (str | Unset):
        error_message (str | Unset):
    """

    id: str
    job_id: str
    item_index: int
    url: str
    status: str
    created_at: datetime.datetime
    filename: str | Unset = UNSET
    document_id: str | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        job_id = self.job_id

        item_index = self.item_index

        url = self.url

        status = self.status

        created_at = self.created_at.isoformat()

        filename = self.filename

        document_id = self.document_id

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "job_id": job_id,
                "item_index": item_index,
                "url": url,
                "status": status,
                "created_at": created_at,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        job_id = d.pop("job_id")

        item_index = d.pop("item_index")

        url = d.pop("url")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        filename = d.pop("filename", UNSET)

        document_id = d.pop("document_id", UNSET)

        error_message = d.pop("error_message", UNSET)

        ingest_item = cls(
            id=id,
            job_id=job_id,
            item_index=item_index,
            url=url,
            status=status,
            created_at=created_at,
            filename=filename,
            document_id=document_id,
            error_message=error_message,
        )

        ingest_item.additional_properties = d
        return ingest_item

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
