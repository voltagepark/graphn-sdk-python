from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_week import UsageWeek


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        id (str):
        invoice_id (str):
        status (InvoiceStatus):
        amount_due (int):
        currency (str):
        created (int):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        number (str | Unset):
        hosted_invoice_url (str | Unset):
        invoice_pdf (str | Unset):
        usage_by_week (list[UsageWeek] | Unset):
    """

    id: str
    invoice_id: str
    status: InvoiceStatus
    amount_due: int
    currency: str
    created: int
    period_start: datetime.datetime
    period_end: datetime.datetime
    number: str | Unset = UNSET
    hosted_invoice_url: str | Unset = UNSET
    invoice_pdf: str | Unset = UNSET
    usage_by_week: list[UsageWeek] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        invoice_id = self.invoice_id

        status = self.status.value

        amount_due = self.amount_due

        currency = self.currency

        created = self.created

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        number = self.number

        hosted_invoice_url = self.hosted_invoice_url

        invoice_pdf = self.invoice_pdf

        usage_by_week: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_by_week, Unset):
            usage_by_week = []
            for usage_by_week_item_data in self.usage_by_week:
                usage_by_week_item = usage_by_week_item_data.to_dict()
                usage_by_week.append(usage_by_week_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "invoiceId": invoice_id,
                "status": status,
                "amountDue": amount_due,
                "currency": currency,
                "created": created,
                "periodStart": period_start,
                "periodEnd": period_end,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if hosted_invoice_url is not UNSET:
            field_dict["hostedInvoiceUrl"] = hosted_invoice_url
        if invoice_pdf is not UNSET:
            field_dict["invoicePdf"] = invoice_pdf
        if usage_by_week is not UNSET:
            field_dict["usageByWeek"] = usage_by_week

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_week import UsageWeek

        d = dict(src_dict)
        id = d.pop("id")

        invoice_id = d.pop("invoiceId")

        status = InvoiceStatus(d.pop("status"))

        amount_due = d.pop("amountDue")

        currency = d.pop("currency")

        created = d.pop("created")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        number = d.pop("number", UNSET)

        hosted_invoice_url = d.pop("hostedInvoiceUrl", UNSET)

        invoice_pdf = d.pop("invoicePdf", UNSET)

        _usage_by_week = d.pop("usageByWeek", UNSET)
        usage_by_week: list[UsageWeek] | Unset = UNSET
        if _usage_by_week is not UNSET:
            usage_by_week = []
            for usage_by_week_item_data in _usage_by_week:
                usage_by_week_item = UsageWeek.from_dict(usage_by_week_item_data)

                usage_by_week.append(usage_by_week_item)

        invoice = cls(
            id=id,
            invoice_id=invoice_id,
            status=status,
            amount_due=amount_due,
            currency=currency,
            created=created,
            period_start=period_start,
            period_end=period_end,
            number=number,
            hosted_invoice_url=hosted_invoice_url,
            invoice_pdf=invoice_pdf,
            usage_by_week=usage_by_week,
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
