from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceVersionRef")


@_attrs_define
class ResourceVersionRef:
    """
    Attributes:
        version_id (str):
        version_number (int):
        created_at (datetime.datetime):
        content_hash (str | Unset):
        snapshot_id (str | Unset):
        message (str | Unset):
    """

    version_id: str
    version_number: int
    created_at: datetime.datetime
    content_hash: str | Unset = UNSET
    snapshot_id: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        version_number = self.version_number

        created_at = self.created_at.isoformat()

        content_hash = self.content_hash

        snapshot_id = self.snapshot_id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version_id": version_id,
                "version_number": version_number,
                "created_at": created_at,
            }
        )
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        version_id = d.pop("version_id")

        version_number = d.pop("version_number")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        content_hash = d.pop("content_hash", UNSET)

        snapshot_id = d.pop("snapshot_id", UNSET)

        message = d.pop("message", UNSET)

        resource_version_ref = cls(
            version_id=version_id,
            version_number=version_number,
            created_at=created_at,
            content_hash=content_hash,
            snapshot_id=snapshot_id,
            message=message,
        )

        resource_version_ref.additional_properties = d
        return resource_version_ref

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
