from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_invoice_quote import AdminInvoiceQuote


T = TypeVar("T", bound="AdminInvoicePreviewResponse")


@_attrs_define
class AdminInvoicePreviewResponse:
    """
    Attributes:
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        manifest_sha_256 (str):
        quote (AdminInvoiceQuote):
        rendering_mode (str | Unset):
    """

    period_start: datetime.datetime
    period_end: datetime.datetime
    manifest_sha_256: str
    quote: AdminInvoiceQuote
    rendering_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        manifest_sha_256 = self.manifest_sha_256

        quote = self.quote.to_dict()

        rendering_mode = self.rendering_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodStart": period_start,
                "periodEnd": period_end,
                "manifestSha256": manifest_sha_256,
                "quote": quote,
            }
        )
        if rendering_mode is not UNSET:
            field_dict["renderingMode"] = rendering_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_quote import AdminInvoiceQuote

        d = dict(src_dict)
        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        manifest_sha_256 = d.pop("manifestSha256")

        quote = AdminInvoiceQuote.from_dict(d.pop("quote"))

        rendering_mode = d.pop("renderingMode", UNSET)

        admin_invoice_preview_response = cls(
            period_start=period_start,
            period_end=period_end,
            manifest_sha_256=manifest_sha_256,
            quote=quote,
            rendering_mode=rendering_mode,
        )

        admin_invoice_preview_response.additional_properties = d
        return admin_invoice_preview_response

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
