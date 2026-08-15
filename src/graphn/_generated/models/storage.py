from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Storage")


@_attrs_define
class Storage:
    """
    Attributes:
        name (str):
        status (str):
        display_name (str | Unset):
        description (str | Unset):
        object_count (int | Unset):
        total_size_bytes (int | Unset):
    """

    name: str
    status: str
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    object_count: int | Unset = UNSET
    total_size_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        display_name = self.display_name

        description = self.description

        object_count = self.object_count

        total_size_bytes = self.total_size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if object_count is not UNSET:
            field_dict["object_count"] = object_count
        if total_size_bytes is not UNSET:
            field_dict["total_size_bytes"] = total_size_bytes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        object_count = d.pop("object_count", UNSET)

        total_size_bytes = d.pop("total_size_bytes", UNSET)

        storage = cls(
            name=name,
            status=status,
            display_name=display_name,
            description=description,
            object_count=object_count,
            total_size_bytes=total_size_bytes,
        )

        storage.additional_properties = d
        return storage

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
