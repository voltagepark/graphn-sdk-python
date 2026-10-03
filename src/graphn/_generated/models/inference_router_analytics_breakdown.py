from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_router_analytics_metrics import (
        InferenceRouterAnalyticsMetrics,
    )


T = TypeVar("T", bound="InferenceRouterAnalyticsBreakdown")


@_attrs_define
class InferenceRouterAnalyticsBreakdown:
    """
    Attributes:
        key (str):
        metrics (InferenceRouterAnalyticsMetrics):
        model_ref (str | Unset):
        model_source (str | Unset):
    """

    key: str
    metrics: InferenceRouterAnalyticsMetrics
    model_ref: str | Unset = UNSET
    model_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        metrics = self.metrics.to_dict()

        model_ref = self.model_ref

        model_source = self.model_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "metrics": metrics,
            }
        )
        if model_ref is not UNSET:
            field_dict["model_ref"] = model_ref
        if model_source is not UNSET:
            field_dict["model_source"] = model_source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_analytics_metrics import (
            InferenceRouterAnalyticsMetrics,
        )

        d = dict(src_dict)
        key = d.pop("key")

        metrics = InferenceRouterAnalyticsMetrics.from_dict(d.pop("metrics"))

        model_ref = d.pop("model_ref", UNSET)

        model_source = d.pop("model_source", UNSET)

        inference_router_analytics_breakdown = cls(
            key=key,
            metrics=metrics,
            model_ref=model_ref,
            model_source=model_source,
        )

        inference_router_analytics_breakdown.additional_properties = d
        return inference_router_analytics_breakdown

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
