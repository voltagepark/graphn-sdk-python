from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PaymentMethod")


@_attrs_define
class PaymentMethod:
    """
    Attributes:
        id (str):
        brand (str):
        last4 (str):
        exp_month (int):
        exp_year (int):
        is_default (bool):
    """

    id: str
    brand: str
    last4: str
    exp_month: int
    exp_year: int
    is_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        brand = self.brand

        last4 = self.last4

        exp_month = self.exp_month

        exp_year = self.exp_year

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "brand": brand,
                "last4": last4,
                "expMonth": exp_month,
                "expYear": exp_year,
                "isDefault": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        brand = d.pop("brand")

        last4 = d.pop("last4")

        exp_month = d.pop("expMonth")

        exp_year = d.pop("expYear")

        is_default = d.pop("isDefault")

        payment_method = cls(
            id=id,
            brand=brand,
            last4=last4,
            exp_month=exp_month,
            exp_year=exp_year,
            is_default=is_default,
        )

        payment_method.additional_properties = d
        return payment_method

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
