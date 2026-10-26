from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_day import UsageDay


T = TypeVar("T", bound="BillingStatementDetail")


@_attrs_define
class BillingStatementDetail:
    """
    Attributes:
        org_id (str):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        status (str):
        opening_cents (int):
        usage_cents (int):
        credited_cents (int):
        debited_cents (int):
        credits_cents (int):
        closing_cents (int):
        amount_due_cents (int):
        revision (int):
        generated_at (datetime.datetime):
        input_fingerprint (str | Unset):
        usage_by_day (list[UsageDay] | Unset):
        statement_pdf (str | Unset):
        statement_preview_url (str | Unset):
    """

    org_id: str
    period_start: datetime.datetime
    period_end: datetime.datetime
    status: str
    opening_cents: int
    usage_cents: int
    credited_cents: int
    debited_cents: int
    credits_cents: int
    closing_cents: int
    amount_due_cents: int
    revision: int
    generated_at: datetime.datetime
    input_fingerprint: str | Unset = UNSET
    usage_by_day: list[UsageDay] | Unset = UNSET
    statement_pdf: str | Unset = UNSET
    statement_preview_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        status = self.status

        opening_cents = self.opening_cents

        usage_cents = self.usage_cents

        credited_cents = self.credited_cents

        debited_cents = self.debited_cents

        credits_cents = self.credits_cents

        closing_cents = self.closing_cents

        amount_due_cents = self.amount_due_cents

        revision = self.revision

        generated_at = self.generated_at.isoformat()

        input_fingerprint = self.input_fingerprint

        usage_by_day: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_by_day, Unset):
            usage_by_day = []
            for usage_by_day_item_data in self.usage_by_day:
                usage_by_day_item = usage_by_day_item_data.to_dict()
                usage_by_day.append(usage_by_day_item)

        statement_pdf = self.statement_pdf

        statement_preview_url = self.statement_preview_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "periodStart": period_start,
                "periodEnd": period_end,
                "status": status,
                "openingCents": opening_cents,
                "usageCents": usage_cents,
                "creditedCents": credited_cents,
                "debitedCents": debited_cents,
                "creditsCents": credits_cents,
                "closingCents": closing_cents,
                "amountDueCents": amount_due_cents,
                "revision": revision,
                "generatedAt": generated_at,
            }
        )
        if input_fingerprint is not UNSET:
            field_dict["inputFingerprint"] = input_fingerprint
        if usage_by_day is not UNSET:
            field_dict["usageByDay"] = usage_by_day
        if statement_pdf is not UNSET:
            field_dict["statementPdf"] = statement_pdf
        if statement_preview_url is not UNSET:
            field_dict["statementPreviewUrl"] = statement_preview_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_day import UsageDay

        d = dict(src_dict)
        org_id = d.pop("orgId")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        status = d.pop("status")

        opening_cents = d.pop("openingCents")

        usage_cents = d.pop("usageCents")

        credited_cents = d.pop("creditedCents")

        debited_cents = d.pop("debitedCents")

        credits_cents = d.pop("creditsCents")

        closing_cents = d.pop("closingCents")

        amount_due_cents = d.pop("amountDueCents")

        revision = d.pop("revision")

        generated_at = datetime.datetime.fromisoformat(d.pop("generatedAt"))

        input_fingerprint = d.pop("inputFingerprint", UNSET)

        _usage_by_day = d.pop("usageByDay", UNSET)
        usage_by_day: list[UsageDay] | Unset = UNSET
        if _usage_by_day is not UNSET:
            usage_by_day = []
            for usage_by_day_item_data in _usage_by_day:
                usage_by_day_item = UsageDay.from_dict(usage_by_day_item_data)

                usage_by_day.append(usage_by_day_item)

        statement_pdf = d.pop("statementPdf", UNSET)

        statement_preview_url = d.pop("statementPreviewUrl", UNSET)

        billing_statement_detail = cls(
            org_id=org_id,
            period_start=period_start,
            period_end=period_end,
            status=status,
            opening_cents=opening_cents,
            usage_cents=usage_cents,
            credited_cents=credited_cents,
            debited_cents=debited_cents,
            credits_cents=credits_cents,
            closing_cents=closing_cents,
            amount_due_cents=amount_due_cents,
            revision=revision,
            generated_at=generated_at,
            input_fingerprint=input_fingerprint,
            usage_by_day=usage_by_day,
            statement_pdf=statement_pdf,
            statement_preview_url=statement_preview_url,
        )

        billing_statement_detail.additional_properties = d
        return billing_statement_detail

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
