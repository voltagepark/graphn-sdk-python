from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BillingTopUpProbeResult")


@_attrs_define
class BillingTopUpProbeResult:
    """
    Attributes:
        probe_only (bool):
        stripe_test_mode (bool):
    """

    probe_only: bool
    stripe_test_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        probe_only = self.probe_only

        stripe_test_mode = self.stripe_test_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "probeOnly": probe_only,
                "stripeTestMode": stripe_test_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        probe_only = d.pop("probeOnly")

        stripe_test_mode = d.pop("stripeTestMode")

        billing_top_up_probe_result = cls(
            probe_only=probe_only,
            stripe_test_mode=stripe_test_mode,
        )

        billing_top_up_probe_result.additional_properties = d
        return billing_top_up_probe_result

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
