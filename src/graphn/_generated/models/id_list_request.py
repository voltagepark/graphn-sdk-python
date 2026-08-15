from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="IdListRequest")


@_attrs_define
class IdListRequest:
    """
    Attributes:
        ids (list[str]):
    """

    ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        id_list_request = cls(
            ids=ids,
        )

        return id_list_request
