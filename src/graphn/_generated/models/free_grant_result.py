from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="FreeGrantResult")


@_attrs_define
class FreeGrantResult:
    """
    Attributes:
        balance_cents (int):
        balance_status (str):
        already_claimed (bool):
    """

    balance_cents: int
    balance_status: str
    already_claimed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_cents = self.balance_cents

        balance_status = self.balance_status

        already_claimed = self.already_claimed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceCents": balance_cents,
                "balanceStatus": balance_status,
                "alreadyClaimed": already_claimed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        balance_cents = d.pop("balanceCents")

        balance_status = d.pop("balanceStatus")

        already_claimed = d.pop("alreadyClaimed")

        free_grant_result = cls(
            balance_cents=balance_cents,
            balance_status=balance_status,
            already_claimed=already_claimed,
        )

        free_grant_result.additional_properties = d
        return free_grant_result

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
