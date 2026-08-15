from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoragePostResult")


@_attrs_define
class StoragePostResult:
    """
    Attributes:
        upload_id (str | Unset):
        max_part_size (int | Unset):
        url (str | Unset):
        expires_in (int | Unset):
        key (str | Unset):
    """

    upload_id: str | Unset = UNSET
    max_part_size: int | Unset = UNSET
    url: str | Unset = UNSET
    expires_in: int | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        max_part_size = self.max_part_size

        url = self.url

        expires_in = self.expires_in

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if max_part_size is not UNSET:
            field_dict["max_part_size"] = max_part_size
        if url is not UNSET:
            field_dict["url"] = url
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upload_id = d.pop("upload_id", UNSET)

        max_part_size = d.pop("max_part_size", UNSET)

        url = d.pop("url", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        key = d.pop("key", UNSET)

        storage_post_result = cls(
            upload_id=upload_id,
            max_part_size=max_part_size,
            url=url,
            expires_in=expires_in,
            key=key,
        )

        storage_post_result.additional_properties = d
        return storage_post_result

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
