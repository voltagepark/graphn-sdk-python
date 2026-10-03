from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminInvoiceVoidResponse")


@_attrs_define
class AdminInvoiceVoidResponse:
    """
    Attributes:
        org_id (str):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        invoice_id (str):
        invoice_status (str):
        amount_due_cents (int):
        hosted_invoice_url (str | Unset):
    """

    org_id: str
    period_start: datetime.datetime
    period_end: datetime.datetime
    invoice_id: str
    invoice_status: str
    amount_due_cents: int
    hosted_invoice_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        invoice_id = self.invoice_id

        invoice_status = self.invoice_status

        amount_due_cents = self.amount_due_cents

        hosted_invoice_url = self.hosted_invoice_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "periodStart": period_start,
                "periodEnd": period_end,
                "invoiceId": invoice_id,
                "invoiceStatus": invoice_status,
                "amountDueCents": amount_due_cents,
            }
        )
        if hosted_invoice_url is not UNSET:
            field_dict["hostedInvoiceUrl"] = hosted_invoice_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        invoice_id = d.pop("invoiceId")

        invoice_status = d.pop("invoiceStatus")

        amount_due_cents = d.pop("amountDueCents")

        hosted_invoice_url = d.pop("hostedInvoiceUrl", UNSET)

        admin_invoice_void_response = cls(
            org_id=org_id,
            period_start=period_start,
            period_end=period_end,
            invoice_id=invoice_id,
            invoice_status=invoice_status,
            amount_due_cents=amount_due_cents,
            hosted_invoice_url=hosted_invoice_url,
        )

        admin_invoice_void_response.additional_properties = d
        return admin_invoice_void_response

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
