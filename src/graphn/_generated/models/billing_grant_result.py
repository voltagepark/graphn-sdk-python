from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.billing_grant_result_new_status import BillingGrantResultNewStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingGrantResult")


@_attrs_define
class BillingGrantResult:
    """
    Attributes:
        already_done (bool):
        om_grant_id (str):
        new_balance_cents (int):
        new_status (BillingGrantResultNewStatus):
        payment_intent_id (str | Unset):
    """

    already_done: bool
    om_grant_id: str
    new_balance_cents: int
    new_status: BillingGrantResultNewStatus
    payment_intent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        already_done = self.already_done

        om_grant_id = self.om_grant_id

        new_balance_cents = self.new_balance_cents

        new_status = self.new_status.value

        payment_intent_id = self.payment_intent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alreadyDone": already_done,
                "omGrantId": om_grant_id,
                "newBalanceCents": new_balance_cents,
                "newStatus": new_status,
            }
        )
        if payment_intent_id is not UNSET:
            field_dict["paymentIntentId"] = payment_intent_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        already_done = d.pop("alreadyDone")

        om_grant_id = d.pop("omGrantId")

        new_balance_cents = d.pop("newBalanceCents")

        new_status = BillingGrantResultNewStatus(d.pop("newStatus"))

        payment_intent_id = d.pop("paymentIntentId", UNSET)

        billing_grant_result = cls(
            already_done=already_done,
            om_grant_id=om_grant_id,
            new_balance_cents=new_balance_cents,
            new_status=new_status,
            payment_intent_id=payment_intent_id,
        )

        billing_grant_result.additional_properties = d
        return billing_grant_result

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
