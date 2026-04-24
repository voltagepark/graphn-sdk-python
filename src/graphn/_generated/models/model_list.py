from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.model_list_object import ModelListObject

if TYPE_CHECKING:
    from ..models.model import Model


T = TypeVar("T", bound="ModelList")


@_attrs_define
class ModelList:
    """
    Attributes:
        object_ (ModelListObject):
        data (list[Model]):
    """

    object_: ModelListObject
    data: list[Model]

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model import Model

        d = dict(src_dict)
        object_ = ModelListObject(d.pop("object"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Model.from_dict(data_item_data)

            data.append(data_item)

        model_list = cls(
            object_=object_,
            data=data,
        )

        return model_list
