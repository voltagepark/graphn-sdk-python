from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntegrationEvent")


@_attrs_define
class IntegrationEvent:
    """
    Attributes:
        id (str):
        display_name (str):
        description (str | Unset):
        capability (str | Unset):
    """

    id: str
    display_name: str
    description: str | Unset = UNSET
    capability: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        description = self.description

        capability = self.capability

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if capability is not UNSET:
            field_dict["capability"] = capability

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        description = d.pop("description", UNSET)

        capability = d.pop("capability", UNSET)

        integration_event = cls(
            id=id,
            display_name=display_name,
            description=description,
            capability=capability,
        )

        return integration_event
