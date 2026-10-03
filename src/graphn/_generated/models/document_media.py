from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentMedia")


@_attrs_define
class DocumentMedia:
    """
    Attributes:
        url (str):
        expires_at (datetime.datetime):
        expires_in (int):
        content_type (str | Unset):
    """

    url: str
    expires_at: datetime.datetime
    expires_in: int
    content_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        expires_at = self.expires_at.isoformat()

        expires_in = self.expires_in

        content_type = self.content_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "expires_at": expires_at,
                "expires_in": expires_in,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        expires_in = d.pop("expires_in")

        content_type = d.pop("content_type", UNSET)

        document_media = cls(
            url=url,
            expires_at=expires_at,
            expires_in=expires_in,
            content_type=content_type,
        )

        return document_media
