from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.member_role import MemberRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """
    Attributes:
        id (str):
        org_id (str):
        user_id (str):
        role (MemberRole):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        email (str | Unset):
        display_name (str | Unset):
    """

    id: str
    org_id: str
    user_id: str
    role: MemberRole
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email: str | Unset = UNSET
    display_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_id = self.org_id

        user_id = self.user_id

        role = self.role.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        email = self.email

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "user_id": user_id,
                "role": role,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        org_id = d.pop("org_id")

        user_id = d.pop("user_id")

        role = MemberRole(d.pop("role"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        email = d.pop("email", UNSET)

        display_name = d.pop("display_name", UNSET)

        member = cls(
            id=id,
            org_id=org_id,
            user_id=user_id,
            role=role,
            created_at=created_at,
            updated_at=updated_at,
            email=email,
            display_name=display_name,
        )

        member.additional_properties = d
        return member

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
