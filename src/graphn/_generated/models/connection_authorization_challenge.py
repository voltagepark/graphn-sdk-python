from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="ConnectionAuthorizationChallenge")


@_attrs_define
class ConnectionAuthorizationChallenge:
    """
    Attributes:
        authorization_url (str):
        expires_at (datetime.datetime):
    """

    authorization_url: str
    expires_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        authorization_url = self.authorization_url

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authorization_url": authorization_url,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        authorization_url = d.pop("authorization_url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        connection_authorization_challenge = cls(
            authorization_url=authorization_url,
            expires_at=expires_at,
        )

        return connection_authorization_challenge
