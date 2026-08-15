from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.organization_create_type import OrganizationCreateType

T = TypeVar("T", bound="OrganizationCreate")


@_attrs_define
class OrganizationCreate:
    """
    Attributes:
        name (str):
        type_ (OrganizationCreateType):
    """

    name: str
    type_: OrganizationCreateType

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = OrganizationCreateType(d.pop("type"))

        organization_create = cls(
            name=name,
            type_=type_,
        )

        return organization_create
