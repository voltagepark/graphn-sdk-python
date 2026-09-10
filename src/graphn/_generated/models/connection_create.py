from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.connection_create_kind import ConnectionCreateKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionCreate")


@_attrs_define
class ConnectionCreate:
    """
    Attributes:
        name (str):
        kind (ConnectionCreateKind):
        provider_id (str):
        resource_id (str | Unset): Optional linked MCP resource ID.
    """

    name: str
    kind: ConnectionCreateKind
    provider_id: str
    resource_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind.value

        provider_id = self.provider_id

        resource_id = self.resource_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "provider_id": provider_id,
            }
        )
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        kind = ConnectionCreateKind(d.pop("kind"))

        provider_id = d.pop("provider_id")

        resource_id = d.pop("resource_id", UNSET)

        connection_create = cls(
            name=name,
            kind=kind,
            provider_id=provider_id,
            resource_id=resource_id,
        )

        return connection_create
