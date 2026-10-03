from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InferenceRouterAnalyticsMetrics")


@_attrs_define
class InferenceRouterAnalyticsMetrics:
    """
    Attributes:
        requests (int):
        input_tokens (float):
        output_tokens (float):
        total_tokens (float):
        success_count (int):
        error_count (int):
        duration_ms_sum (float):
        average_latency_ms (float):
        estimated_cost (float | None): Sum of event-provided estimated_cost_usd; no local rates are applied.
        shared_candidate_gpu_seconds (float | None): Shared runtime for historically selected custom models, not router-
            attributed cost.
        approximate_p50_latency_ms (float | None | Unset):
        approximate_p95_latency_ms (float | None | Unset):
    """

    requests: int
    input_tokens: float
    output_tokens: float
    total_tokens: float
    success_count: int
    error_count: int
    duration_ms_sum: float
    average_latency_ms: float
    estimated_cost: float | None
    shared_candidate_gpu_seconds: float | None
    approximate_p50_latency_ms: float | None | Unset = UNSET
    approximate_p95_latency_ms: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        total_tokens = self.total_tokens

        success_count = self.success_count

        error_count = self.error_count

        duration_ms_sum = self.duration_ms_sum

        average_latency_ms = self.average_latency_ms

        estimated_cost: float | None
        estimated_cost = self.estimated_cost

        shared_candidate_gpu_seconds: float | None
        shared_candidate_gpu_seconds = self.shared_candidate_gpu_seconds

        approximate_p50_latency_ms: float | None | Unset
        if isinstance(self.approximate_p50_latency_ms, Unset):
            approximate_p50_latency_ms = UNSET
        else:
            approximate_p50_latency_ms = self.approximate_p50_latency_ms

        approximate_p95_latency_ms: float | None | Unset
        if isinstance(self.approximate_p95_latency_ms, Unset):
            approximate_p95_latency_ms = UNSET
        else:
            approximate_p95_latency_ms = self.approximate_p95_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests": requests,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens,
                "success_count": success_count,
                "error_count": error_count,
                "duration_ms_sum": duration_ms_sum,
                "average_latency_ms": average_latency_ms,
                "estimated_cost": estimated_cost,
                "shared_candidate_gpu_seconds": shared_candidate_gpu_seconds,
            }
        )
        if approximate_p50_latency_ms is not UNSET:
            field_dict["approximate_p50_latency_ms"] = approximate_p50_latency_ms
        if approximate_p95_latency_ms is not UNSET:
            field_dict["approximate_p95_latency_ms"] = approximate_p95_latency_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        requests = d.pop("requests")

        input_tokens = d.pop("input_tokens")

        output_tokens = d.pop("output_tokens")

        total_tokens = d.pop("total_tokens")

        success_count = d.pop("success_count")

        error_count = d.pop("error_count")

        duration_ms_sum = d.pop("duration_ms_sum")

        average_latency_ms = d.pop("average_latency_ms")

        def _parse_estimated_cost(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        estimated_cost = _parse_estimated_cost(d.pop("estimated_cost"))

        def _parse_shared_candidate_gpu_seconds(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        shared_candidate_gpu_seconds = _parse_shared_candidate_gpu_seconds(
            d.pop("shared_candidate_gpu_seconds")
        )

        def _parse_approximate_p50_latency_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        approximate_p50_latency_ms = _parse_approximate_p50_latency_ms(
            d.pop("approximate_p50_latency_ms", UNSET)
        )

        def _parse_approximate_p95_latency_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        approximate_p95_latency_ms = _parse_approximate_p95_latency_ms(
            d.pop("approximate_p95_latency_ms", UNSET)
        )

        inference_router_analytics_metrics = cls(
            requests=requests,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            success_count=success_count,
            error_count=error_count,
            duration_ms_sum=duration_ms_sum,
            average_latency_ms=average_latency_ms,
            estimated_cost=estimated_cost,
            shared_candidate_gpu_seconds=shared_candidate_gpu_seconds,
            approximate_p50_latency_ms=approximate_p50_latency_ms,
            approximate_p95_latency_ms=approximate_p95_latency_ms,
        )

        inference_router_analytics_metrics.additional_properties = d
        return inference_router_analytics_metrics

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
