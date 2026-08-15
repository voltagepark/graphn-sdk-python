from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="InvitationAcceptResult")


@_attrs_define
class InvitationAcceptResult:
    """
    Attributes:
        scope_type (str):
        scope_id (str):
        org_id (str):
        role (str):
    """

    scope_type: str
    scope_id: str
    org_id: str
    role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope_type = self.scope_type

        scope_id = self.scope_id

        org_id = self.org_id

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope_type": scope_type,
                "scope_id": scope_id,
                "org_id": org_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scope_type = d.pop("scope_type")

        scope_id = d.pop("scope_id")

        org_id = d.pop("org_id")

        role = d.pop("role")

        invitation_accept_result = cls(
            scope_type=scope_type,
            scope_id=scope_id,
            org_id=org_id,
            role=role,
        )

        invitation_accept_result.additional_properties = d
        return invitation_accept_result

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
