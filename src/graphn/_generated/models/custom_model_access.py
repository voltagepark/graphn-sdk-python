from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CustomModelAccess")


@_attrs_define
class CustomModelAccess:
    """
    Attributes:
        allowed (bool): Whether the workspace may import custom models.
    """

    allowed: bool

    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "allowed": allowed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = d.pop("allowed")

        custom_model_access = cls(
            allowed=allowed,
        )

        return custom_model_access
