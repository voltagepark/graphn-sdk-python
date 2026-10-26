from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_invoice_quote import AdminInvoiceQuote


T = TypeVar("T", bound="AdminInvoiceCreateResponse")


@_attrs_define
class AdminInvoiceCreateResponse:
    """
    Attributes:
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        manifest_sha_256 (str):
        quote (AdminInvoiceQuote):
        invoice_id (str):
        invoice_status (str):
        amount_due_cents (int):
        rendering_mode (str | Unset):
        hosted_invoice_url (str | Unset):
    """

    period_start: datetime.datetime
    period_end: datetime.datetime
    manifest_sha_256: str
    quote: AdminInvoiceQuote
    invoice_id: str
    invoice_status: str
    amount_due_cents: int
    rendering_mode: str | Unset = UNSET
    hosted_invoice_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        manifest_sha_256 = self.manifest_sha_256

        quote = self.quote.to_dict()

        invoice_id = self.invoice_id

        invoice_status = self.invoice_status

        amount_due_cents = self.amount_due_cents

        rendering_mode = self.rendering_mode

        hosted_invoice_url = self.hosted_invoice_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodStart": period_start,
                "periodEnd": period_end,
                "manifestSha256": manifest_sha_256,
                "quote": quote,
                "invoiceId": invoice_id,
                "invoiceStatus": invoice_status,
                "amountDueCents": amount_due_cents,
            }
        )
        if rendering_mode is not UNSET:
            field_dict["renderingMode"] = rendering_mode
        if hosted_invoice_url is not UNSET:
            field_dict["hostedInvoiceUrl"] = hosted_invoice_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_quote import AdminInvoiceQuote

        d = dict(src_dict)
        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        manifest_sha_256 = d.pop("manifestSha256")

        quote = AdminInvoiceQuote.from_dict(d.pop("quote"))

        invoice_id = d.pop("invoiceId")

        invoice_status = d.pop("invoiceStatus")

        amount_due_cents = d.pop("amountDueCents")

        rendering_mode = d.pop("renderingMode", UNSET)

        hosted_invoice_url = d.pop("hostedInvoiceUrl", UNSET)

        admin_invoice_create_response = cls(
            period_start=period_start,
            period_end=period_end,
            manifest_sha_256=manifest_sha_256,
            quote=quote,
            invoice_id=invoice_id,
            invoice_status=invoice_status,
            amount_due_cents=amount_due_cents,
            rendering_mode=rendering_mode,
            hosted_invoice_url=hosted_invoice_url,
        )

        admin_invoice_create_response.additional_properties = d
        return admin_invoice_create_response

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
