from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageUpload")


@_attrs_define
class StorageUpload:
    """
    Attributes:
        key (str):
        size (int):
        store_name (str):
        etag (str | Unset):
    """

    key: str
    size: int
    store_name: str
    etag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        size = self.size

        store_name = self.store_name

        etag = self.etag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "size": size,
                "store_name": store_name,
            }
        )
        if etag is not UNSET:
            field_dict["etag"] = etag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        size = d.pop("size")

        store_name = d.pop("store_name")

        etag = d.pop("etag", UNSET)

        storage_upload = cls(
            key=key,
            size=size,
            store_name=store_name,
            etag=etag,
        )

        storage_upload.additional_properties = d
        return storage_upload

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
