from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="StorageStats")


@_attrs_define
class StorageStats:
    """
    Attributes:
        name (str):
        object_count (int):
        total_size_bytes (int):
        status (str):
    """

    name: str
    object_count: int
    total_size_bytes: int
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        object_count = self.object_count

        total_size_bytes = self.total_size_bytes

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "object_count": object_count,
                "total_size_bytes": total_size_bytes,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        object_count = d.pop("object_count")

        total_size_bytes = d.pop("total_size_bytes")

        status = d.pop("status")

        storage_stats = cls(
            name=name,
            object_count=object_count,
            total_size_bytes=total_size_bytes,
            status=status,
        )

        storage_stats.additional_properties = d
        return storage_stats

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
