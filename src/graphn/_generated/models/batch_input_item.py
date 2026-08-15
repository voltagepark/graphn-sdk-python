from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_input_item_input import BatchInputItemInput


T = TypeVar("T", bound="BatchInputItem")


@_attrs_define
class BatchInputItem:
    """
    Attributes:
        input_ (BatchInputItemInput):
        custom_id (str | Unset):
    """

    input_: BatchInputItemInput
    custom_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_.to_dict()

        custom_id = self.custom_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input": input_,
            }
        )
        if custom_id is not UNSET:
            field_dict["custom_id"] = custom_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_input_item_input import BatchInputItemInput

        d = dict(src_dict)
        input_ = BatchInputItemInput.from_dict(d.pop("input"))

        custom_id = d.pop("custom_id", UNSET)

        batch_input_item = cls(
            input_=input_,
            custom_id=custom_id,
        )

        return batch_input_item
