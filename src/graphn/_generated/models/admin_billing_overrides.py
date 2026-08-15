from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminBillingOverrides")


@_attrs_define
class AdminBillingOverrides:
    """
    Attributes:
        comment (str):
        custom_models_disabled (bool | Unset):
        allow_negative_balance (bool | Unset):
        negative_limit_cents (int | Unset):
        has_purchased (bool | Unset):
    """

    comment: str
    custom_models_disabled: bool | Unset = UNSET
    allow_negative_balance: bool | Unset = UNSET
    negative_limit_cents: int | Unset = UNSET
    has_purchased: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        custom_models_disabled = self.custom_models_disabled

        allow_negative_balance = self.allow_negative_balance

        negative_limit_cents = self.negative_limit_cents

        has_purchased = self.has_purchased

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
            }
        )
        if custom_models_disabled is not UNSET:
            field_dict["customModelsDisabled"] = custom_models_disabled
        if allow_negative_balance is not UNSET:
            field_dict["allowNegativeBalance"] = allow_negative_balance
        if negative_limit_cents is not UNSET:
            field_dict["negativeLimitCents"] = negative_limit_cents
        if has_purchased is not UNSET:
            field_dict["hasPurchased"] = has_purchased

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        comment = d.pop("comment")

        custom_models_disabled = d.pop("customModelsDisabled", UNSET)

        allow_negative_balance = d.pop("allowNegativeBalance", UNSET)

        negative_limit_cents = d.pop("negativeLimitCents", UNSET)

        has_purchased = d.pop("hasPurchased", UNSET)

        admin_billing_overrides = cls(
            comment=comment,
            custom_models_disabled=custom_models_disabled,
            allow_negative_balance=allow_negative_balance,
            negative_limit_cents=negative_limit_cents,
            has_purchased=has_purchased,
        )

        admin_billing_overrides.additional_properties = d
        return admin_billing_overrides

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
