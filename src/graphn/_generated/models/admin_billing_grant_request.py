from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminBillingGrantRequest")


@_attrs_define
class AdminBillingGrantRequest:
    """
    Attributes:
        amount_cents (int):
        comment (str):
        idempotency_key (str | Unset):
    """

    amount_cents: int
    comment: str
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        comment = self.comment

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
                "comment": comment,
            }
        )
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        comment = d.pop("comment")

        idempotency_key = d.pop("idempotencyKey", UNSET)

        admin_billing_grant_request = cls(
            amount_cents=amount_cents,
            comment=comment,
            idempotency_key=idempotency_key,
        )

        admin_billing_grant_request.additional_properties = d
        return admin_billing_grant_request

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
