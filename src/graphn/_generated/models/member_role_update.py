from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.member_role_update_role import MemberRoleUpdateRole

T = TypeVar("T", bound="MemberRoleUpdate")


@_attrs_define
class MemberRoleUpdate:
    """
    Attributes:
        role (MemberRoleUpdateRole):
    """

    role: MemberRoleUpdateRole

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role = MemberRoleUpdateRole(d.pop("role"))

        member_role_update = cls(
            role=role,
        )

        return member_role_update
