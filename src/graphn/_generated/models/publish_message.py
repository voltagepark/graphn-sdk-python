from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishMessage")


@_attrs_define
class PublishMessage:
    """
    Attributes:
        message (str | Unset):
    """

    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        publish_message = cls(
            message=message,
        )

        return publish_message
