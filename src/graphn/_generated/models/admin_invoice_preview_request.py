from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminInvoicePreviewRequest")


@_attrs_define
class AdminInvoicePreviewRequest:
    """Preview always requires explicit [from, to) bounds.

    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        rendering_mode (str | Unset):
    """

    from_: datetime.datetime
    to: datetime.datetime
    rendering_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        rendering_mode = self.rendering_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if rendering_mode is not UNSET:
            field_dict["renderingMode"] = rendering_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = datetime.datetime.fromisoformat(d.pop("from"))

        to = datetime.datetime.fromisoformat(d.pop("to"))

        rendering_mode = d.pop("renderingMode", UNSET)

        admin_invoice_preview_request = cls(
            from_=from_,
            to=to,
            rendering_mode=rendering_mode,
        )

        admin_invoice_preview_request.additional_properties = d
        return admin_invoice_preview_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
