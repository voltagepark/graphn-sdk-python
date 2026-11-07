from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingTopUpChargeRequest")


@_attrs_define
class BillingTopUpChargeRequest:
    """
    Attributes:
        amount_cents (int):
        idempotency_key (str):
        probe_only (bool | Unset):
        require_stripe_test_mode (bool | Unset): Fail the charge unless Stripe is in test mode.
    """

    amount_cents: int
    idempotency_key: str
    probe_only: bool | Unset = UNSET
    require_stripe_test_mode: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        idempotency_key = self.idempotency_key

        probe_only = self.probe_only

        require_stripe_test_mode = self.require_stripe_test_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
                "idempotencyKey": idempotency_key,
            }
        )
        if probe_only is not UNSET:
            field_dict["probeOnly"] = probe_only
        if require_stripe_test_mode is not UNSET:
            field_dict["requireStripeTestMode"] = require_stripe_test_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        idempotency_key = d.pop("idempotencyKey")

        probe_only = d.pop("probeOnly", UNSET)

        require_stripe_test_mode = d.pop("requireStripeTestMode", UNSET)

        billing_top_up_charge_request = cls(
            amount_cents=amount_cents,
            idempotency_key=idempotency_key,
            probe_only=probe_only,
            require_stripe_test_mode=require_stripe_test_mode,
        )

        billing_top_up_charge_request.additional_properties = d
        return billing_top_up_charge_request

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
