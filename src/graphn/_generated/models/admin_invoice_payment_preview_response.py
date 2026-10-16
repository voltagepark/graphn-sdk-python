from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminInvoicePaymentPreviewResponse")


@_attrs_define
class AdminInvoicePaymentPreviewResponse:
    """
    Attributes:
        org_id (str):
        invoice_id (str):
        stripe_customer_id (str):
        currency (str):
        invoice_total_cents (int):
        invoice_amount_paid_cents (int):
        overlay_period_start (datetime.datetime):
        overlay_period_end (datetime.datetime):
        overlay_expected_amount_cents (int):
        idempotency_key (str):
        already_recorded (bool):
        recorded_sequence (int):
        checksum (str):
    """

    org_id: str
    invoice_id: str
    stripe_customer_id: str
    currency: str
    invoice_total_cents: int
    invoice_amount_paid_cents: int
    overlay_period_start: datetime.datetime
    overlay_period_end: datetime.datetime
    overlay_expected_amount_cents: int
    idempotency_key: str
    already_recorded: bool
    recorded_sequence: int
    checksum: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        invoice_id = self.invoice_id

        stripe_customer_id = self.stripe_customer_id

        currency = self.currency

        invoice_total_cents = self.invoice_total_cents

        invoice_amount_paid_cents = self.invoice_amount_paid_cents

        overlay_period_start = self.overlay_period_start.isoformat()

        overlay_period_end = self.overlay_period_end.isoformat()

        overlay_expected_amount_cents = self.overlay_expected_amount_cents

        idempotency_key = self.idempotency_key

        already_recorded = self.already_recorded

        recorded_sequence = self.recorded_sequence

        checksum = self.checksum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "invoiceId": invoice_id,
                "stripeCustomerId": stripe_customer_id,
                "currency": currency,
                "invoiceTotalCents": invoice_total_cents,
                "invoiceAmountPaidCents": invoice_amount_paid_cents,
                "overlayPeriodStart": overlay_period_start,
                "overlayPeriodEnd": overlay_period_end,
                "overlayExpectedAmountCents": overlay_expected_amount_cents,
                "idempotencyKey": idempotency_key,
                "alreadyRecorded": already_recorded,
                "recordedSequence": recorded_sequence,
                "checksum": checksum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        invoice_id = d.pop("invoiceId")

        stripe_customer_id = d.pop("stripeCustomerId")

        currency = d.pop("currency")

        invoice_total_cents = d.pop("invoiceTotalCents")

        invoice_amount_paid_cents = d.pop("invoiceAmountPaidCents")

        overlay_period_start = datetime.datetime.fromisoformat(
            d.pop("overlayPeriodStart")
        )

        overlay_period_end = datetime.datetime.fromisoformat(d.pop("overlayPeriodEnd"))

        overlay_expected_amount_cents = d.pop("overlayExpectedAmountCents")

        idempotency_key = d.pop("idempotencyKey")

        already_recorded = d.pop("alreadyRecorded")

        recorded_sequence = d.pop("recordedSequence")

        checksum = d.pop("checksum")

        admin_invoice_payment_preview_response = cls(
            org_id=org_id,
            invoice_id=invoice_id,
            stripe_customer_id=stripe_customer_id,
            currency=currency,
            invoice_total_cents=invoice_total_cents,
            invoice_amount_paid_cents=invoice_amount_paid_cents,
            overlay_period_start=overlay_period_start,
            overlay_period_end=overlay_period_end,
            overlay_expected_amount_cents=overlay_expected_amount_cents,
            idempotency_key=idempotency_key,
            already_recorded=already_recorded,
            recorded_sequence=recorded_sequence,
            checksum=checksum,
        )

        admin_invoice_payment_preview_response.additional_properties = d
        return admin_invoice_payment_preview_response

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
