from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        id (str):
        number (str):
        status (InvoiceStatus):
        amount_due (int):
        currency (str):
        created (int):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        opening_cents (int | Unset):
        usage_cents (int | Unset):
        credits_cents (int | Unset):
        closing_cents (int | Unset):
        hosted_invoice_url (str | Unset):
        invoice_pdf (str | Unset):
        invoice_document_url (str | Unset):
    """

    id: str
    number: str
    status: InvoiceStatus
    amount_due: int
    currency: str
    created: int
    period_start: datetime.datetime
    period_end: datetime.datetime
    opening_cents: int | Unset = UNSET
    usage_cents: int | Unset = UNSET
    credits_cents: int | Unset = UNSET
    closing_cents: int | Unset = UNSET
    hosted_invoice_url: str | Unset = UNSET
    invoice_pdf: str | Unset = UNSET
    invoice_document_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        status = self.status.value

        amount_due = self.amount_due

        currency = self.currency

        created = self.created

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        opening_cents = self.opening_cents

        usage_cents = self.usage_cents

        credits_cents = self.credits_cents

        closing_cents = self.closing_cents

        hosted_invoice_url = self.hosted_invoice_url

        invoice_pdf = self.invoice_pdf

        invoice_document_url = self.invoice_document_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "status": status,
                "amountDue": amount_due,
                "currency": currency,
                "created": created,
                "periodStart": period_start,
                "periodEnd": period_end,
            }
        )
        if opening_cents is not UNSET:
            field_dict["openingCents"] = opening_cents
        if usage_cents is not UNSET:
            field_dict["usageCents"] = usage_cents
        if credits_cents is not UNSET:
            field_dict["creditsCents"] = credits_cents
        if closing_cents is not UNSET:
            field_dict["closingCents"] = closing_cents
        if hosted_invoice_url is not UNSET:
            field_dict["hostedInvoiceUrl"] = hosted_invoice_url
        if invoice_pdf is not UNSET:
            field_dict["invoicePdf"] = invoice_pdf
        if invoice_document_url is not UNSET:
            field_dict["invoiceDocumentUrl"] = invoice_document_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        status = InvoiceStatus(d.pop("status"))

        amount_due = d.pop("amountDue")

        currency = d.pop("currency")

        created = d.pop("created")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        opening_cents = d.pop("openingCents", UNSET)

        usage_cents = d.pop("usageCents", UNSET)

        credits_cents = d.pop("creditsCents", UNSET)

        closing_cents = d.pop("closingCents", UNSET)

        hosted_invoice_url = d.pop("hostedInvoiceUrl", UNSET)

        invoice_pdf = d.pop("invoicePdf", UNSET)

        invoice_document_url = d.pop("invoiceDocumentUrl", UNSET)

        invoice = cls(
            id=id,
            number=number,
            status=status,
            amount_due=amount_due,
            currency=currency,
            created=created,
            period_start=period_start,
            period_end=period_end,
            opening_cents=opening_cents,
            usage_cents=usage_cents,
            credits_cents=credits_cents,
            closing_cents=closing_cents,
            hosted_invoice_url=hosted_invoice_url,
            invoice_pdf=invoice_pdf,
            invoice_document_url=invoice_document_url,
        )

        invoice.additional_properties = d
        return invoice

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
