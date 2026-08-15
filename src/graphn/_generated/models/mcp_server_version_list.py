from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_version_ref import ResourceVersionRef


T = TypeVar("T", bound="McpServerVersionList")


@_attrs_define
class McpServerVersionList:
    """
    Attributes:
        versions (list[ResourceVersionRef]):
        published_version_id (str | Unset):
    """

    versions: list[ResourceVersionRef]
    published_version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        published_version_id = self.published_version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "versions": versions,
            }
        )
        if published_version_id is not UNSET:
            field_dict["published_version_id"] = published_version_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resource_version_ref import ResourceVersionRef

        d = dict(src_dict)
        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = ResourceVersionRef.from_dict(versions_item_data)

            versions.append(versions_item)

        published_version_id = d.pop("published_version_id", UNSET)

        mcp_server_version_list = cls(
            versions=versions,
            published_version_id=published_version_id,
        )

        mcp_server_version_list.additional_properties = d
        return mcp_server_version_list

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
