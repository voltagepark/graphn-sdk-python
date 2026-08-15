from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSettingsUpdate")


@_attrs_define
class BillingSettingsUpdate:
    """
    Attributes:
        billing_email (str | Unset):
        recharge_amount_cents (int | Unset):
        auto_recharge_enabled (bool | Unset):
        auto_recharge_threshold_cents (int | Unset):
    """

    billing_email: str | Unset = UNSET
    recharge_amount_cents: int | Unset = UNSET
    auto_recharge_enabled: bool | Unset = UNSET
    auto_recharge_threshold_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_email = self.billing_email

        recharge_amount_cents = self.recharge_amount_cents

        auto_recharge_enabled = self.auto_recharge_enabled

        auto_recharge_threshold_cents = self.auto_recharge_threshold_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_email is not UNSET:
            field_dict["billingEmail"] = billing_email
        if recharge_amount_cents is not UNSET:
            field_dict["rechargeAmountCents"] = recharge_amount_cents
        if auto_recharge_enabled is not UNSET:
            field_dict["autoRechargeEnabled"] = auto_recharge_enabled
        if auto_recharge_threshold_cents is not UNSET:
            field_dict["autoRechargeThresholdCents"] = auto_recharge_threshold_cents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        billing_email = d.pop("billingEmail", UNSET)

        recharge_amount_cents = d.pop("rechargeAmountCents", UNSET)

        auto_recharge_enabled = d.pop("autoRechargeEnabled", UNSET)

        auto_recharge_threshold_cents = d.pop("autoRechargeThresholdCents", UNSET)

        billing_settings_update = cls(
            billing_email=billing_email,
            recharge_amount_cents=recharge_amount_cents,
            auto_recharge_enabled=auto_recharge_enabled,
            auto_recharge_threshold_cents=auto_recharge_threshold_cents,
        )

        billing_settings_update.additional_properties = d
        return billing_settings_update

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
