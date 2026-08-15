from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.invitation_create_role import InvitationCreateRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationCreate")


@_attrs_define
class InvitationCreate:
    """
    Attributes:
        role (InvitationCreateRole):
        email (str | Unset):
        emails (list[str] | Unset):
    """

    role: InvitationCreateRole
    email: str | Unset = UNSET
    emails: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        email = self.email

        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if emails is not UNSET:
            field_dict["emails"] = emails

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role = InvitationCreateRole(d.pop("role"))

        email = d.pop("email", UNSET)

        emails = cast(list[str], d.pop("emails", UNSET))

        invitation_create = cls(
            role=role,
            email=email,
            emails=emails,
        )

        return invitation_create
