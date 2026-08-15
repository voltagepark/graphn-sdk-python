from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchUpdateItem")


@_attrs_define
class BatchUpdateItem:
    """
    Attributes:
        id (str):
        name (str | Unset):
        description (str | Unset):
    """

    id: str
    name: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        batch_update_item = cls(
            id=id,
            name=name,
            description=description,
        )

        return batch_update_item
