from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_usage import WorkspaceUsage


T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """
    Attributes:
        id (str):
        organization_id (str):
        name (str):
        owner_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        usage (WorkspaceUsage | Unset):
    """

    id: str
    organization_id: str
    name: str
    owner_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    usage: WorkspaceUsage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        name = self.name

        owner_id = self.owner_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization_id": organization_id,
                "name": name,
                "owner_id": owner_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workspace_usage import WorkspaceUsage

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organization_id")

        name = d.pop("name")

        owner_id = d.pop("owner_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _usage = d.pop("usage", UNSET)
        usage: WorkspaceUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = WorkspaceUsage.from_dict(_usage)

        workspace = cls(
            id=id,
            organization_id=organization_id,
            name=name,
            owner_id=owner_id,
            created_at=created_at,
            updated_at=updated_at,
            usage=usage,
        )

        workspace.additional_properties = d
        return workspace

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
