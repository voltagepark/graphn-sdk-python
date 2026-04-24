from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.model_object import ModelObject
from ..models.model_owned_by import ModelOwnedBy

T = TypeVar("T", bound="Model")


@_attrs_define
class Model:
    """
    Attributes:
        id (str):
        object_ (ModelObject):
        created (int): Unix timestamp.
        owned_by (ModelOwnedBy):
    """

    id: str
    object_: ModelObject
    created: int
    owned_by: ModelOwnedBy

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_.value

        created = self.created

        owned_by = self.owned_by.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created": created,
                "owned_by": owned_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        object_ = ModelObject(d.pop("object"))

        created = d.pop("created")

        owned_by = ModelOwnedBy(d.pop("owned_by"))

        model = cls(
            id=id,
            object_=object_,
            created=created,
            owned_by=owned_by,
        )

        return model
