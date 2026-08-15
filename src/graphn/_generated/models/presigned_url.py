from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PresignedURL")


@_attrs_define
class PresignedURL:
    """
    Attributes:
        url (str):
        expires_in (int):
        key (str):
    """

    url: str
    expires_in: int
    key: str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        expires_in = self.expires_in

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "expires_in": expires_in,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        expires_in = d.pop("expires_in")

        key = d.pop("key")

        presigned_url = cls(
            url=url,
            expires_in=expires_in,
            key=key,
        )

        return presigned_url
