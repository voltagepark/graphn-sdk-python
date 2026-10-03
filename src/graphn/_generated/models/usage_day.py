from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="UsageDay")


@_attrs_define
class UsageDay:
    """
    Attributes:
        date (datetime.date):
        amount_cents (int):
    """

    date: datetime.date
    amount_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        amount_cents = self.amount_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "amountCents": amount_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        amount_cents = d.pop("amountCents")

        usage_day = cls(
            date=date,
            amount_cents=amount_cents,
        )

        usage_day.additional_properties = d
        return usage_day

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
