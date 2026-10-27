from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_created_type import OrganizationCreatedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace import Workspace


T = TypeVar("T", bound="OrganizationCreated")


@_attrs_define
class OrganizationCreated:
    """The created organization, plus its default workspace when this request
    created one.

        Attributes:
            id (str):
            name (str):
            slug (str):
            type_ (OrganizationCreatedType):
            owner_id (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            default_workspace (Workspace | Unset):
    """

    id: str
    name: str
    slug: str
    type_: OrganizationCreatedType
    owner_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    default_workspace: Workspace | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        type_ = self.type_.value

        owner_id = self.owner_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        default_workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_workspace, Unset):
            default_workspace = self.default_workspace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "type": type_,
                "owner_id": owner_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if default_workspace is not UNSET:
            field_dict["default_workspace"] = default_workspace

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workspace import Workspace

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        type_ = OrganizationCreatedType(d.pop("type"))

        owner_id = d.pop("owner_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _default_workspace = d.pop("default_workspace", UNSET)
        default_workspace: Workspace | Unset
        if isinstance(_default_workspace, Unset):
            default_workspace = UNSET
        else:
            default_workspace = Workspace.from_dict(_default_workspace)

        organization_created = cls(
            id=id,
            name=name,
            slug=slug,
            type_=type_,
            owner_id=owner_id,
            created_at=created_at,
            updated_at=updated_at,
            default_workspace=default_workspace,
        )

        organization_created.additional_properties = d
        return organization_created

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
