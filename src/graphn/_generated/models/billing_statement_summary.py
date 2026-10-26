from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingStatementSummary")


@_attrs_define
class BillingStatementSummary:
    """
    Attributes:
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        status (str):
        opening_cents (int | Unset):
        usage_cents (int | Unset):
        credited_cents (int | Unset):
        debited_cents (int | Unset):
        closing_cents (int | Unset):
        amount_due_cents (int | Unset):
        revision (int | Unset):
        input_fingerprint (str | Unset):
    """

    period_start: datetime.datetime
    period_end: datetime.datetime
    status: str
    opening_cents: int | Unset = UNSET
    usage_cents: int | Unset = UNSET
    credited_cents: int | Unset = UNSET
    debited_cents: int | Unset = UNSET
    closing_cents: int | Unset = UNSET
    amount_due_cents: int | Unset = UNSET
    revision: int | Unset = UNSET
    input_fingerprint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        status = self.status

        opening_cents = self.opening_cents

        usage_cents = self.usage_cents

        credited_cents = self.credited_cents

        debited_cents = self.debited_cents

        closing_cents = self.closing_cents

        amount_due_cents = self.amount_due_cents

        revision = self.revision

        input_fingerprint = self.input_fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodStart": period_start,
                "periodEnd": period_end,
                "status": status,
            }
        )
        if opening_cents is not UNSET:
            field_dict["openingCents"] = opening_cents
        if usage_cents is not UNSET:
            field_dict["usageCents"] = usage_cents
        if credited_cents is not UNSET:
            field_dict["creditedCents"] = credited_cents
        if debited_cents is not UNSET:
            field_dict["debitedCents"] = debited_cents
        if closing_cents is not UNSET:
            field_dict["closingCents"] = closing_cents
        if amount_due_cents is not UNSET:
            field_dict["amountDueCents"] = amount_due_cents
        if revision is not UNSET:
            field_dict["revision"] = revision
        if input_fingerprint is not UNSET:
            field_dict["inputFingerprint"] = input_fingerprint

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        status = d.pop("status")

        opening_cents = d.pop("openingCents", UNSET)

        usage_cents = d.pop("usageCents", UNSET)

        credited_cents = d.pop("creditedCents", UNSET)

        debited_cents = d.pop("debitedCents", UNSET)

        closing_cents = d.pop("closingCents", UNSET)

        amount_due_cents = d.pop("amountDueCents", UNSET)

        revision = d.pop("revision", UNSET)

        input_fingerprint = d.pop("inputFingerprint", UNSET)

        billing_statement_summary = cls(
            period_start=period_start,
            period_end=period_end,
            status=status,
            opening_cents=opening_cents,
            usage_cents=usage_cents,
            credited_cents=credited_cents,
            debited_cents=debited_cents,
            closing_cents=closing_cents,
            amount_due_cents=amount_due_cents,
            revision=revision,
            input_fingerprint=input_fingerprint,
        )

        billing_statement_summary.additional_properties = d
        return billing_statement_summary

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
