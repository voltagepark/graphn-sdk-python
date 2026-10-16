from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_day import UsageDay


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        id (str): Statement identity key (`periodStart`, RFC3339). This stays statement-scoped even when the row is
            covered by Stripe invoice lifecycle metadata; use `invoiceId` for Stripe identity.
        number (str): Statement display number (`STM-YYYYMMDD`) derived from `periodStart`. It no longer switches to
            `INV-*` on invoiced rows.
        status (InvoiceStatus):
        currency (str):
        created (int):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        invoice_id (str | Unset): Optional Stripe invoice id for statement rows that are covered by an invoice lifecycle
            record.
        detail_kind (str | Unset): Optional invoice-detail source marker (`statement`, `invoice_close`, or
            `invoice_overlay`) for clients that need to distinguish statement-native rows from Stripe-backed overlays.
        amount_due (int | Unset): Compatibility field for legacy invoice clients. For prepaid statements this is
            max(-closingCents, 0), not a collections balance with payment terms. It is omitted when statement figures could
            not be read; an explicit 0 means the amount due is known to be zero.
        opening_cents (int | Unset):
        usage_cents (int | Unset):
        credits_cents (int | Unset):
        credited_cents (int | Unset):
        debited_cents (int | Unset):
        closing_cents (int | Unset):
        amount_total_cents (int | Unset): Stripe invoice face value when available. Distinct from `amountDue`
            compatibility semantics on prepaid statements.
        revision (int | Unset):
        input_fingerprint (str | Unset): Exact immutable statement input fingerprint. Omitted when billing-cp could not
            read the underlying statement object.
        invoice_amount_due_cents (int | Unset): Authoritative invoice-level amount from invoice metadata. Distinct from
            per-statement amountDue and omitted when unavailable.
        usage_by_day (list[UsageDay] | Unset):
        hosted_invoice_url (str | Unset): Stripe-hosted invoice page URL. Statement-backed responses leave this empty.
        invoice_pdf (str | Unset):
        invoice_preview_url (str | Unset): Inline-renderable statement URL. For statement rows this is a separately
            signed URL with inline content disposition; it may be empty when no preview artifact exists.
    """

    id: str
    number: str
    status: InvoiceStatus
    currency: str
    created: int
    period_start: datetime.datetime
    period_end: datetime.datetime
    invoice_id: str | Unset = UNSET
    detail_kind: str | Unset = UNSET
    amount_due: int | Unset = UNSET
    opening_cents: int | Unset = UNSET
    usage_cents: int | Unset = UNSET
    credits_cents: int | Unset = UNSET
    credited_cents: int | Unset = UNSET
    debited_cents: int | Unset = UNSET
    closing_cents: int | Unset = UNSET
    amount_total_cents: int | Unset = UNSET
    revision: int | Unset = UNSET
    input_fingerprint: str | Unset = UNSET
    invoice_amount_due_cents: int | Unset = UNSET
    usage_by_day: list[UsageDay] | Unset = UNSET
    hosted_invoice_url: str | Unset = UNSET
    invoice_pdf: str | Unset = UNSET
    invoice_preview_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        status = self.status.value

        currency = self.currency

        created = self.created

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        invoice_id = self.invoice_id

        detail_kind = self.detail_kind

        amount_due = self.amount_due

        opening_cents = self.opening_cents

        usage_cents = self.usage_cents

        credits_cents = self.credits_cents

        credited_cents = self.credited_cents

        debited_cents = self.debited_cents

        closing_cents = self.closing_cents

        amount_total_cents = self.amount_total_cents

        revision = self.revision

        input_fingerprint = self.input_fingerprint

        invoice_amount_due_cents = self.invoice_amount_due_cents

        usage_by_day: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_by_day, Unset):
            usage_by_day = []
            for usage_by_day_item_data in self.usage_by_day:
                usage_by_day_item = usage_by_day_item_data.to_dict()
                usage_by_day.append(usage_by_day_item)

        hosted_invoice_url = self.hosted_invoice_url

        invoice_pdf = self.invoice_pdf

        invoice_preview_url = self.invoice_preview_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "status": status,
                "currency": currency,
                "created": created,
                "periodStart": period_start,
                "periodEnd": period_end,
            }
        )
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if detail_kind is not UNSET:
            field_dict["detailKind"] = detail_kind
        if amount_due is not UNSET:
            field_dict["amountDue"] = amount_due
        if opening_cents is not UNSET:
            field_dict["openingCents"] = opening_cents
        if usage_cents is not UNSET:
            field_dict["usageCents"] = usage_cents
        if credits_cents is not UNSET:
            field_dict["creditsCents"] = credits_cents
        if credited_cents is not UNSET:
            field_dict["creditedCents"] = credited_cents
        if debited_cents is not UNSET:
            field_dict["debitedCents"] = debited_cents
        if closing_cents is not UNSET:
            field_dict["closingCents"] = closing_cents
        if amount_total_cents is not UNSET:
            field_dict["amountTotalCents"] = amount_total_cents
        if revision is not UNSET:
            field_dict["revision"] = revision
        if input_fingerprint is not UNSET:
            field_dict["inputFingerprint"] = input_fingerprint
        if invoice_amount_due_cents is not UNSET:
            field_dict["invoiceAmountDueCents"] = invoice_amount_due_cents
        if usage_by_day is not UNSET:
            field_dict["usageByDay"] = usage_by_day
        if hosted_invoice_url is not UNSET:
            field_dict["hostedInvoiceUrl"] = hosted_invoice_url
        if invoice_pdf is not UNSET:
            field_dict["invoicePdf"] = invoice_pdf
        if invoice_preview_url is not UNSET:
            field_dict["invoicePreviewUrl"] = invoice_preview_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_day import UsageDay

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        status = InvoiceStatus(d.pop("status"))

        currency = d.pop("currency")

        created = d.pop("created")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        invoice_id = d.pop("invoiceId", UNSET)

        detail_kind = d.pop("detailKind", UNSET)

        amount_due = d.pop("amountDue", UNSET)

        opening_cents = d.pop("openingCents", UNSET)

        usage_cents = d.pop("usageCents", UNSET)

        credits_cents = d.pop("creditsCents", UNSET)

        credited_cents = d.pop("creditedCents", UNSET)

        debited_cents = d.pop("debitedCents", UNSET)

        closing_cents = d.pop("closingCents", UNSET)

        amount_total_cents = d.pop("amountTotalCents", UNSET)

        revision = d.pop("revision", UNSET)

        input_fingerprint = d.pop("inputFingerprint", UNSET)

        invoice_amount_due_cents = d.pop("invoiceAmountDueCents", UNSET)

        _usage_by_day = d.pop("usageByDay", UNSET)
        usage_by_day: list[UsageDay] | Unset = UNSET
        if _usage_by_day is not UNSET:
            usage_by_day = []
            for usage_by_day_item_data in _usage_by_day:
                usage_by_day_item = UsageDay.from_dict(usage_by_day_item_data)

                usage_by_day.append(usage_by_day_item)

        hosted_invoice_url = d.pop("hostedInvoiceUrl", UNSET)

        invoice_pdf = d.pop("invoicePdf", UNSET)

        invoice_preview_url = d.pop("invoicePreviewUrl", UNSET)

        invoice = cls(
            id=id,
            number=number,
            status=status,
            currency=currency,
            created=created,
            period_start=period_start,
            period_end=period_end,
            invoice_id=invoice_id,
            detail_kind=detail_kind,
            amount_due=amount_due,
            opening_cents=opening_cents,
            usage_cents=usage_cents,
            credits_cents=credits_cents,
            credited_cents=credited_cents,
            debited_cents=debited_cents,
            closing_cents=closing_cents,
            amount_total_cents=amount_total_cents,
            revision=revision,
            input_fingerprint=input_fingerprint,
            invoice_amount_due_cents=invoice_amount_due_cents,
            usage_by_day=usage_by_day,
            hosted_invoice_url=hosted_invoice_url,
            invoice_pdf=invoice_pdf,
            invoice_preview_url=invoice_preview_url,
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
