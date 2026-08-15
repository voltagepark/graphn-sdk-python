from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.invitation_role import InvitationRole
from ..models.invitation_scope_type import InvitationScopeType
from ..models.invitation_status import InvitationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        id (str):
        scope_type (InvitationScopeType):
        scope_id (str):
        org_id (str):
        email (str):
        role (InvitationRole):
        status (InvitationStatus):
        created_at (datetime.datetime):
        invited_by (str | Unset):
        token (str | Unset):
        expires_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: str
    scope_type: InvitationScopeType
    scope_id: str
    org_id: str
    email: str
    role: InvitationRole
    status: InvitationStatus
    created_at: datetime.datetime
    invited_by: str | Unset = UNSET
    token: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scope_type = self.scope_type.value

        scope_id = self.scope_id

        org_id = self.org_id

        email = self.email

        role = self.role.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        invited_by = self.invited_by

        token = self.token

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "scope_type": scope_type,
                "scope_id": scope_id,
                "org_id": org_id,
                "email": email,
                "role": role,
                "status": status,
                "created_at": created_at,
            }
        )
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by
        if token is not UNSET:
            field_dict["token"] = token
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        scope_type = InvitationScopeType(d.pop("scope_type"))

        scope_id = d.pop("scope_id")

        org_id = d.pop("org_id")

        email = d.pop("email")

        role = InvitationRole(d.pop("role"))

        status = InvitationStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        invited_by = d.pop("invited_by", UNSET)

        token = d.pop("token", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        invitation = cls(
            id=id,
            scope_type=scope_type,
            scope_id=scope_id,
            org_id=org_id,
            email=email,
            role=role,
            status=status,
            created_at=created_at,
            invited_by=invited_by,
            token=token,
            expires_at=expires_at,
            updated_at=updated_at,
        )

        invitation.additional_properties = d
        return invitation

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
