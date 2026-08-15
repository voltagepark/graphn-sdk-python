from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyCreated")


@_attrs_define
class ApiKeyCreated:
    """
    Attributes:
        key (str):
        key_id (str):
        workspace_id (str):
        description (str):
        created_at (datetime.datetime):
        expires_at (datetime.datetime | Unset):
    """

    key: str
    key_id: str
    workspace_id: str
    description: str
    created_at: datetime.datetime
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        key_id = self.key_id

        workspace_id = self.workspace_id

        description = self.description

        created_at = self.created_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "key_id": key_id,
                "workspace_id": workspace_id,
                "description": description,
                "created_at": created_at,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        key_id = d.pop("key_id")

        workspace_id = d.pop("workspace_id")

        description = d.pop("description")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        api_key_created = cls(
            key=key,
            key_id=key_id,
            workspace_id=workspace_id,
            description=description,
            created_at=created_at,
            expires_at=expires_at,
        )

        api_key_created.additional_properties = d
        return api_key_created

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
