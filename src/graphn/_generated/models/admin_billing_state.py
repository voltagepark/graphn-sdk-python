from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminBillingState")


@_attrs_define
class AdminBillingState:
    """
    Attributes:
        org_id (str):
        billing_account_exists (bool):
        balance_cents (int):
        balance_status (str):
        stripe_customer_id (str | Unset):
        billing_email (str | Unset):
        recharge_amount_cents (int | Unset):
        auto_recharge_enabled (bool | Unset):
        auto_recharge_threshold_cents (int | Unset):
        has_purchased (bool | Unset):
        custom_models_disabled (bool | Unset):
        allow_negative_balance (bool | Unset):
        negative_limit_cents (int | Unset):
    """

    org_id: str
    billing_account_exists: bool
    balance_cents: int
    balance_status: str
    stripe_customer_id: str | Unset = UNSET
    billing_email: str | Unset = UNSET
    recharge_amount_cents: int | Unset = UNSET
    auto_recharge_enabled: bool | Unset = UNSET
    auto_recharge_threshold_cents: int | Unset = UNSET
    has_purchased: bool | Unset = UNSET
    custom_models_disabled: bool | Unset = UNSET
    allow_negative_balance: bool | Unset = UNSET
    negative_limit_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        billing_account_exists = self.billing_account_exists

        balance_cents = self.balance_cents

        balance_status = self.balance_status

        stripe_customer_id = self.stripe_customer_id

        billing_email = self.billing_email

        recharge_amount_cents = self.recharge_amount_cents

        auto_recharge_enabled = self.auto_recharge_enabled

        auto_recharge_threshold_cents = self.auto_recharge_threshold_cents

        has_purchased = self.has_purchased

        custom_models_disabled = self.custom_models_disabled

        allow_negative_balance = self.allow_negative_balance

        negative_limit_cents = self.negative_limit_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "billingAccountExists": billing_account_exists,
                "balanceCents": balance_cents,
                "balanceStatus": balance_status,
            }
        )
        if stripe_customer_id is not UNSET:
            field_dict["stripeCustomerId"] = stripe_customer_id
        if billing_email is not UNSET:
            field_dict["billingEmail"] = billing_email
        if recharge_amount_cents is not UNSET:
            field_dict["rechargeAmountCents"] = recharge_amount_cents
        if auto_recharge_enabled is not UNSET:
            field_dict["autoRechargeEnabled"] = auto_recharge_enabled
        if auto_recharge_threshold_cents is not UNSET:
            field_dict["autoRechargeThresholdCents"] = auto_recharge_threshold_cents
        if has_purchased is not UNSET:
            field_dict["hasPurchased"] = has_purchased
        if custom_models_disabled is not UNSET:
            field_dict["customModelsDisabled"] = custom_models_disabled
        if allow_negative_balance is not UNSET:
            field_dict["allowNegativeBalance"] = allow_negative_balance
        if negative_limit_cents is not UNSET:
            field_dict["negativeLimitCents"] = negative_limit_cents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        billing_account_exists = d.pop("billingAccountExists")

        balance_cents = d.pop("balanceCents")

        balance_status = d.pop("balanceStatus")

        stripe_customer_id = d.pop("stripeCustomerId", UNSET)

        billing_email = d.pop("billingEmail", UNSET)

        recharge_amount_cents = d.pop("rechargeAmountCents", UNSET)

        auto_recharge_enabled = d.pop("autoRechargeEnabled", UNSET)

        auto_recharge_threshold_cents = d.pop("autoRechargeThresholdCents", UNSET)

        has_purchased = d.pop("hasPurchased", UNSET)

        custom_models_disabled = d.pop("customModelsDisabled", UNSET)

        allow_negative_balance = d.pop("allowNegativeBalance", UNSET)

        negative_limit_cents = d.pop("negativeLimitCents", UNSET)

        admin_billing_state = cls(
            org_id=org_id,
            billing_account_exists=billing_account_exists,
            balance_cents=balance_cents,
            balance_status=balance_status,
            stripe_customer_id=stripe_customer_id,
            billing_email=billing_email,
            recharge_amount_cents=recharge_amount_cents,
            auto_recharge_enabled=auto_recharge_enabled,
            auto_recharge_threshold_cents=auto_recharge_threshold_cents,
            has_purchased=has_purchased,
            custom_models_disabled=custom_models_disabled,
            allow_negative_balance=allow_negative_balance,
            negative_limit_cents=negative_limit_cents,
        )

        admin_billing_state.additional_properties = d
        return admin_billing_state

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
