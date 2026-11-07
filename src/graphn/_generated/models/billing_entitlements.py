from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingEntitlements")


@_attrs_define
class BillingEntitlements:
    """
    Attributes:
        balance_cents (int):
        balance_status (str):
        has_purchased (bool):
        allow_negative_balance (bool | Unset): True when the org is permitted to run below zero (invoice terms). A
            negative balanceCents is expected usage for these orgs, not a debt blocking them.
        negative_limit_cents (int | Unset): Positive magnitude of how far below zero the org may run; the org is blocked
            at -negativeLimitCents. Omitted when the allowance is uncapped, and meaningless when allowNegativeBalance is
            false.
        free_grant_status (str | Unset):
        top_up_cents (int | Unset): Settled top-ups and paid invoices since org creation, in cents. Omitted when the
            journal read failed, so the UI can tell unknown from zero. Never counts grants, refunds or adjustments.
        top_up_threshold_cents (int | Unset):
    """

    balance_cents: int
    balance_status: str
    has_purchased: bool
    allow_negative_balance: bool | Unset = UNSET
    negative_limit_cents: int | Unset = UNSET
    free_grant_status: str | Unset = UNSET
    top_up_cents: int | Unset = UNSET
    top_up_threshold_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_cents = self.balance_cents

        balance_status = self.balance_status

        has_purchased = self.has_purchased

        allow_negative_balance = self.allow_negative_balance

        negative_limit_cents = self.negative_limit_cents

        free_grant_status = self.free_grant_status

        top_up_cents = self.top_up_cents

        top_up_threshold_cents = self.top_up_threshold_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceCents": balance_cents,
                "balanceStatus": balance_status,
                "hasPurchased": has_purchased,
            }
        )
        if allow_negative_balance is not UNSET:
            field_dict["allowNegativeBalance"] = allow_negative_balance
        if negative_limit_cents is not UNSET:
            field_dict["negativeLimitCents"] = negative_limit_cents
        if free_grant_status is not UNSET:
            field_dict["freeGrantStatus"] = free_grant_status
        if top_up_cents is not UNSET:
            field_dict["topUpCents"] = top_up_cents
        if top_up_threshold_cents is not UNSET:
            field_dict["topUpThresholdCents"] = top_up_threshold_cents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        balance_cents = d.pop("balanceCents")

        balance_status = d.pop("balanceStatus")

        has_purchased = d.pop("hasPurchased")

        allow_negative_balance = d.pop("allowNegativeBalance", UNSET)

        negative_limit_cents = d.pop("negativeLimitCents", UNSET)

        free_grant_status = d.pop("freeGrantStatus", UNSET)

        top_up_cents = d.pop("topUpCents", UNSET)

        top_up_threshold_cents = d.pop("topUpThresholdCents", UNSET)

        billing_entitlements = cls(
            balance_cents=balance_cents,
            balance_status=balance_status,
            has_purchased=has_purchased,
            allow_negative_balance=allow_negative_balance,
            negative_limit_cents=negative_limit_cents,
            free_grant_status=free_grant_status,
            top_up_cents=top_up_cents,
            top_up_threshold_cents=top_up_threshold_cents,
        )

        billing_entitlements.additional_properties = d
        return billing_entitlements

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
