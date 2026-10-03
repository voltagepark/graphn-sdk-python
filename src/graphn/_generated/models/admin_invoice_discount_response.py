from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_invoice_discount import AdminInvoiceDiscount


T = TypeVar("T", bound="AdminInvoiceDiscountResponse")


@_attrs_define
class AdminInvoiceDiscountResponse:
    """
    Attributes:
        org_id (str):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        invoice_id (str):
        invoice_status (str):
        revision (int):
        root_invoice_id (str):
        original_amount_cents (int):
        adjusted_amount_cents (int):
        discount (AdminInvoiceDiscount):
        supersedes_invoice_id (str | Unset):
        hosted_invoice_url (str | Unset):
    """

    org_id: str
    period_start: datetime.datetime
    period_end: datetime.datetime
    invoice_id: str
    invoice_status: str
    revision: int
    root_invoice_id: str
    original_amount_cents: int
    adjusted_amount_cents: int
    discount: AdminInvoiceDiscount
    supersedes_invoice_id: str | Unset = UNSET
    hosted_invoice_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        invoice_id = self.invoice_id

        invoice_status = self.invoice_status

        revision = self.revision

        root_invoice_id = self.root_invoice_id

        original_amount_cents = self.original_amount_cents

        adjusted_amount_cents = self.adjusted_amount_cents

        discount = self.discount.to_dict()

        supersedes_invoice_id = self.supersedes_invoice_id

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
                "revision": revision,
                "rootInvoiceId": root_invoice_id,
                "originalAmountCents": original_amount_cents,
                "adjustedAmountCents": adjusted_amount_cents,
                "discount": discount,
            }
        )
        if supersedes_invoice_id is not UNSET:
            field_dict["supersedesInvoiceId"] = supersedes_invoice_id
        if hosted_invoice_url is not UNSET:
            field_dict["hostedInvoiceUrl"] = hosted_invoice_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_discount import (
            AdminInvoiceDiscount,
        )

        d = dict(src_dict)
        org_id = d.pop("orgId")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        invoice_id = d.pop("invoiceId")

        invoice_status = d.pop("invoiceStatus")

        revision = d.pop("revision")

        root_invoice_id = d.pop("rootInvoiceId")

        original_amount_cents = d.pop("originalAmountCents")

        adjusted_amount_cents = d.pop("adjustedAmountCents")

        discount = AdminInvoiceDiscount.from_dict(d.pop("discount"))

        supersedes_invoice_id = d.pop("supersedesInvoiceId", UNSET)

        hosted_invoice_url = d.pop("hostedInvoiceUrl", UNSET)

        admin_invoice_discount_response = cls(
            org_id=org_id,
            period_start=period_start,
            period_end=period_end,
            invoice_id=invoice_id,
            invoice_status=invoice_status,
            revision=revision,
            root_invoice_id=root_invoice_id,
            original_amount_cents=original_amount_cents,
            adjusted_amount_cents=adjusted_amount_cents,
            discount=discount,
            supersedes_invoice_id=supersedes_invoice_id,
            hosted_invoice_url=hosted_invoice_url,
        )

        admin_invoice_discount_response.additional_properties = d
        return admin_invoice_discount_response

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
