from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.billing_usage_time_series_item import BillingUsageTimeSeriesItem


T = TypeVar("T", bound="BillingUsage")


@_attrs_define
class BillingUsage:
    """
    Attributes:
        total_spend_cents (int):
        current_period_start (datetime.datetime):
        current_period_end (datetime.datetime):
        next_billing_date (str):
        time_series (list[BillingUsageTimeSeriesItem]):
    """

    total_spend_cents: int
    current_period_start: datetime.datetime
    current_period_end: datetime.datetime
    next_billing_date: str
    time_series: list[BillingUsageTimeSeriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_spend_cents = self.total_spend_cents

        current_period_start = self.current_period_start.isoformat()

        current_period_end = self.current_period_end.isoformat()

        next_billing_date = self.next_billing_date

        time_series = []
        for time_series_item_data in self.time_series:
            time_series_item = time_series_item_data.to_dict()
            time_series.append(time_series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSpendCents": total_spend_cents,
                "currentPeriodStart": current_period_start,
                "currentPeriodEnd": current_period_end,
                "nextBillingDate": next_billing_date,
                "timeSeries": time_series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.billing_usage_time_series_item import (
            BillingUsageTimeSeriesItem,
        )

        d = dict(src_dict)
        total_spend_cents = d.pop("totalSpendCents")

        current_period_start = datetime.datetime.fromisoformat(
            d.pop("currentPeriodStart")
        )

        current_period_end = datetime.datetime.fromisoformat(d.pop("currentPeriodEnd"))

        next_billing_date = d.pop("nextBillingDate")

        time_series = []
        _time_series = d.pop("timeSeries")
        for time_series_item_data in _time_series:
            time_series_item = BillingUsageTimeSeriesItem.from_dict(
                time_series_item_data
            )

            time_series.append(time_series_item)

        billing_usage = cls(
            total_spend_cents=total_spend_cents,
            current_period_start=current_period_start,
            current_period_end=current_period_end,
            next_billing_date=next_billing_date,
            time_series=time_series,
        )

        billing_usage.additional_properties = d
        return billing_usage

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
