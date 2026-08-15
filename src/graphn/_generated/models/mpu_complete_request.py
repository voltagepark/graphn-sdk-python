from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mpu_part import MpuPart


T = TypeVar("T", bound="MpuCompleteRequest")


@_attrs_define
class MpuCompleteRequest:
    """
    Attributes:
        parts (list[MpuPart] | Unset):
    """

    parts: list[MpuPart] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mpu_part import MpuPart

        d = dict(src_dict)
        _parts = d.pop("parts", UNSET)
        parts: list[MpuPart] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = MpuPart.from_dict(parts_item_data)

                parts.append(parts_item)

        mpu_complete_request = cls(
            parts=parts,
        )

        return mpu_complete_request
