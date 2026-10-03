from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminInvoiceDiscount")


@_attrs_define
class AdminInvoiceDiscount:
    """
    Attributes:
        type_ (str):
        input_value (int):
        discount_cents (int):
        reason (str):
        actor (str):
        idempotency_key (str):
        status (str):
        original_amount_cents (int):
        adjusted_amount_cents (int):
        provider_source_id (str | Unset):
        provider_result_id (str | Unset):
        applied_at (datetime.datetime | Unset):
    """

    type_: str
    input_value: int
    discount_cents: int
    reason: str
    actor: str
    idempotency_key: str
    status: str
    original_amount_cents: int
    adjusted_amount_cents: int
    provider_source_id: str | Unset = UNSET
    provider_result_id: str | Unset = UNSET
    applied_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        input_value = self.input_value

        discount_cents = self.discount_cents

        reason = self.reason

        actor = self.actor

        idempotency_key = self.idempotency_key

        status = self.status

        original_amount_cents = self.original_amount_cents

        adjusted_amount_cents = self.adjusted_amount_cents

        provider_source_id = self.provider_source_id

        provider_result_id = self.provider_result_id

        applied_at: str | Unset = UNSET
        if not isinstance(self.applied_at, Unset):
            applied_at = self.applied_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "inputValue": input_value,
                "discountCents": discount_cents,
                "reason": reason,
                "actor": actor,
                "idempotencyKey": idempotency_key,
                "status": status,
                "originalAmountCents": original_amount_cents,
                "adjustedAmountCents": adjusted_amount_cents,
            }
        )
        if provider_source_id is not UNSET:
            field_dict["providerSourceId"] = provider_source_id
        if provider_result_id is not UNSET:
            field_dict["providerResultId"] = provider_result_id
        if applied_at is not UNSET:
            field_dict["appliedAt"] = applied_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        input_value = d.pop("inputValue")

        discount_cents = d.pop("discountCents")

        reason = d.pop("reason")

        actor = d.pop("actor")

        idempotency_key = d.pop("idempotencyKey")

        status = d.pop("status")

        original_amount_cents = d.pop("originalAmountCents")

        adjusted_amount_cents = d.pop("adjustedAmountCents")

        provider_source_id = d.pop("providerSourceId", UNSET)

        provider_result_id = d.pop("providerResultId", UNSET)

        _applied_at = d.pop("appliedAt", UNSET)
        applied_at: datetime.datetime | Unset
        if isinstance(_applied_at, Unset):
            applied_at = UNSET
        else:
            applied_at = datetime.datetime.fromisoformat(_applied_at)

        admin_invoice_discount = cls(
            type_=type_,
            input_value=input_value,
            discount_cents=discount_cents,
            reason=reason,
            actor=actor,
            idempotency_key=idempotency_key,
            status=status,
            original_amount_cents=original_amount_cents,
            adjusted_amount_cents=adjusted_amount_cents,
            provider_source_id=provider_source_id,
            provider_result_id=provider_result_id,
            applied_at=applied_at,
        )

        admin_invoice_discount.additional_properties = d
        return admin_invoice_discount

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
