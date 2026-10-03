from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.inference_router_analytics_metrics import (
        InferenceRouterAnalyticsMetrics,
    )


T = TypeVar("T", bound="InferenceRouterAnalyticsPoint")


@_attrs_define
class InferenceRouterAnalyticsPoint:
    """
    Attributes:
        timestamp (datetime.datetime):
        metrics (InferenceRouterAnalyticsMetrics):
    """

    timestamp: datetime.datetime
    metrics: InferenceRouterAnalyticsMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        metrics = self.metrics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_analytics_metrics import (
            InferenceRouterAnalyticsMetrics,
        )

        d = dict(src_dict)
        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        metrics = InferenceRouterAnalyticsMetrics.from_dict(d.pop("metrics"))

        inference_router_analytics_point = cls(
            timestamp=timestamp,
            metrics=metrics,
        )

        inference_router_analytics_point.additional_properties = d
        return inference_router_analytics_point

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
