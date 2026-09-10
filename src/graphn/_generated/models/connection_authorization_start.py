from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionAuthorizationStart")


@_attrs_define
class ConnectionAuthorizationStart:
    """
    Attributes:
        return_path (str | Unset): Relative path on the configured GraphN web origin. Default: '/settings/connections'.
        requested_capabilities (list[str] | Unset):
    """

    return_path: str | Unset = "/settings/connections"
    requested_capabilities: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        return_path = self.return_path

        requested_capabilities: list[str] | Unset = UNSET
        if not isinstance(self.requested_capabilities, Unset):
            requested_capabilities = self.requested_capabilities

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if return_path is not UNSET:
            field_dict["return_path"] = return_path
        if requested_capabilities is not UNSET:
            field_dict["requested_capabilities"] = requested_capabilities

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        return_path = d.pop("return_path", UNSET)

        requested_capabilities = cast(list[str], d.pop("requested_capabilities", UNSET))

        connection_authorization_start = cls(
            return_path=return_path,
            requested_capabilities=requested_capabilities,
        )

        return connection_authorization_start
