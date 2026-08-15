from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="MpuPart")


@_attrs_define
class MpuPart:
    """
    Attributes:
        part_number (int):
        etag (str):
    """

    part_number: int
    etag: str

    def to_dict(self) -> dict[str, Any]:
        part_number = self.part_number

        etag = self.etag

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "part_number": part_number,
                "etag": etag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        part_number = d.pop("part_number")

        etag = d.pop("etag")

        mpu_part = cls(
            part_number=part_number,
            etag=etag,
        )

        return mpu_part
