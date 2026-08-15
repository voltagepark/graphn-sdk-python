from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="BatchFileRef")


@_attrs_define
class BatchFileRef:
    """
    Attributes:
        store (str):
        key (str):
    """

    store: str
    key: str

    def to_dict(self) -> dict[str, Any]:
        store = self.store

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "store": store,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        store = d.pop("store")

        key = d.pop("key")

        batch_file_ref = cls(
            store=store,
            key=key,
        )

        return batch_file_ref
