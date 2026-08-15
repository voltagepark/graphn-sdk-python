from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingAccount")


@_attrs_define
class BillingAccount:
    """
    Attributes:
        org_id (str):
        stripe_customer_id (str):
        billing_email (str):
        recharge_amount_cents (int):
        auto_recharge_enabled (bool):
        has_purchased (bool):
        auto_recharge_threshold_cents (int | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
    """

    org_id: str
    stripe_customer_id: str
    billing_email: str
    recharge_amount_cents: int
    auto_recharge_enabled: bool
    has_purchased: bool
    auto_recharge_threshold_cents: int | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        stripe_customer_id = self.stripe_customer_id

        billing_email = self.billing_email

        recharge_amount_cents = self.recharge_amount_cents

        auto_recharge_enabled = self.auto_recharge_enabled

        has_purchased = self.has_purchased

        auto_recharge_threshold_cents = self.auto_recharge_threshold_cents

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "stripeCustomerId": stripe_customer_id,
                "billingEmail": billing_email,
                "rechargeAmountCents": recharge_amount_cents,
                "autoRechargeEnabled": auto_recharge_enabled,
                "hasPurchased": has_purchased,
            }
        )
        if auto_recharge_threshold_cents is not UNSET:
            field_dict["autoRechargeThresholdCents"] = auto_recharge_threshold_cents
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        stripe_customer_id = d.pop("stripeCustomerId")

        billing_email = d.pop("billingEmail")

        recharge_amount_cents = d.pop("rechargeAmountCents")

        auto_recharge_enabled = d.pop("autoRechargeEnabled")

        has_purchased = d.pop("hasPurchased")

        auto_recharge_threshold_cents = d.pop("autoRechargeThresholdCents", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        billing_account = cls(
            org_id=org_id,
            stripe_customer_id=stripe_customer_id,
            billing_email=billing_email,
            recharge_amount_cents=recharge_amount_cents,
            auto_recharge_enabled=auto_recharge_enabled,
            has_purchased=has_purchased,
            auto_recharge_threshold_cents=auto_recharge_threshold_cents,
            created_at=created_at,
            updated_at=updated_at,
        )

        billing_account.additional_properties = d
        return billing_account

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
