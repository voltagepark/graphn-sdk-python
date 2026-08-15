from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="BillingTopUpRequest")


@_attrs_define
class BillingTopUpRequest:
    """
    Attributes:
        amount_cents (int):
        idempotency_key (str):
    """

    amount_cents: int
    idempotency_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
                "idempotencyKey": idempotency_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        idempotency_key = d.pop("idempotencyKey")

        billing_top_up_request = cls(
            amount_cents=amount_cents,
            idempotency_key=idempotency_key,
        )

        billing_top_up_request.additional_properties = d
        return billing_top_up_request

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
