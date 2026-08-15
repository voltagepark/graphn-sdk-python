from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_file import StorageFile


T = TypeVar("T", bound="StorageFileList")


@_attrs_define
class StorageFileList:
    """
    Attributes:
        files (list[StorageFile]):
        total (int):
        prefix (str | Unset):
        is_truncated (bool | Unset):
        continuation_token (str | Unset):
    """

    files: list[StorageFile]
    total: int
    prefix: str | Unset = UNSET
    is_truncated: bool | Unset = UNSET
    continuation_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        total = self.total

        prefix = self.prefix

        is_truncated = self.is_truncated

        continuation_token = self.continuation_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "total": total,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if is_truncated is not UNSET:
            field_dict["is_truncated"] = is_truncated
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.storage_file import StorageFile

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = StorageFile.from_dict(files_item_data)

            files.append(files_item)

        total = d.pop("total")

        prefix = d.pop("prefix", UNSET)

        is_truncated = d.pop("is_truncated", UNSET)

        continuation_token = d.pop("continuation_token", UNSET)

        storage_file_list = cls(
            files=files,
            total=total,
            prefix=prefix,
            is_truncated=is_truncated,
            continuation_token=continuation_token,
        )

        storage_file_list.additional_properties = d
        return storage_file_list

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
