from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Secret")


@_attrs_define
class Secret:
    """Workspace secret record. Additional internal fields may be
    present and are not part of the public contract.

        Attributes:
            id (str):
            workspace_id (str):
            name (str):
            value_preview (str): First few characters of the secret value, suitable for UI
                disambiguation. The full plaintext value is never returned.
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            provider_id (str | Unset): Optional connector / provider this secret belongs to.
            field_name (str | Unset): Optional connector field name.
    """

    id: str
    workspace_id: str
    name: str
    value_preview: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    provider_id: str | Unset = UNSET
    field_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        name = self.name

        value_preview = self.value_preview

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        provider_id = self.provider_id

        field_name = self.field_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "name": name,
                "value_preview": value_preview,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if field_name is not UNSET:
            field_dict["field_name"] = field_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        name = d.pop("name")

        value_preview = d.pop("value_preview")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        provider_id = d.pop("provider_id", UNSET)

        field_name = d.pop("field_name", UNSET)

        secret = cls(
            id=id,
            workspace_id=workspace_id,
            name=name,
            value_preview=value_preview,
            created_at=created_at,
            updated_at=updated_at,
            provider_id=provider_id,
            field_name=field_name,
        )

        secret.additional_properties = d
        return secret

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
