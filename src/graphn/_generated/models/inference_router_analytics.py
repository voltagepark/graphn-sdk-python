from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.inference_router_analytics_interval import (
    InferenceRouterAnalyticsInterval,
)
from ..models.inference_router_analytics_shared_candidate_runtime_status import (
    InferenceRouterAnalyticsSharedCandidateRuntimeStatus,
)

if TYPE_CHECKING:
    from ..models.inference_router_analytics_breakdown import (
        InferenceRouterAnalyticsBreakdown,
    )
    from ..models.inference_router_analytics_metrics import (
        InferenceRouterAnalyticsMetrics,
    )
    from ..models.inference_router_analytics_point import InferenceRouterAnalyticsPoint


T = TypeVar("T", bound="InferenceRouterAnalytics")


@_attrs_define
class InferenceRouterAnalytics:
    """
    Attributes:
        router_id (str):
        interval (InferenceRouterAnalyticsInterval):
        summary (InferenceRouterAnalyticsMetrics):
        time_series (list[InferenceRouterAnalyticsPoint]):
        model_breakdown (list[InferenceRouterAnalyticsBreakdown]):
        decision_breakdown (list[InferenceRouterAnalyticsBreakdown]):
        status_breakdown (list[InferenceRouterAnalyticsBreakdown]):
        shard_breakdown (list[InferenceRouterAnalyticsBreakdown]): Requests attributed to the shard that served them,
            which differs from the router's primary placement after a failover or during a shard migration.
        shared_candidate_runtime_status (InferenceRouterAnalyticsSharedCandidateRuntimeStatus):
        shared_candidate_runtime_refs_total (int):
        shared_candidate_runtime_refs_included (int):
        coverage_from (datetime.datetime | None): Earliest complete analytics bucket available from DynamoDB.
        coverage_through (datetime.datetime | None): Exclusive end of complete analytics buckets proven by the ingestion
            frontier.
        complete (bool): True only when the requested range is fully inside analytics coverage.
    """

    router_id: str
    interval: InferenceRouterAnalyticsInterval
    summary: InferenceRouterAnalyticsMetrics
    time_series: list[InferenceRouterAnalyticsPoint]
    model_breakdown: list[InferenceRouterAnalyticsBreakdown]
    decision_breakdown: list[InferenceRouterAnalyticsBreakdown]
    status_breakdown: list[InferenceRouterAnalyticsBreakdown]
    shard_breakdown: list[InferenceRouterAnalyticsBreakdown]
    shared_candidate_runtime_status: (
        InferenceRouterAnalyticsSharedCandidateRuntimeStatus
    )
    shared_candidate_runtime_refs_total: int
    shared_candidate_runtime_refs_included: int
    coverage_from: datetime.datetime | None
    coverage_through: datetime.datetime | None
    complete: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        router_id = self.router_id

        interval = self.interval.value

        summary = self.summary.to_dict()

        time_series = []
        for time_series_item_data in self.time_series:
            time_series_item = time_series_item_data.to_dict()
            time_series.append(time_series_item)

        model_breakdown = []
        for model_breakdown_item_data in self.model_breakdown:
            model_breakdown_item = model_breakdown_item_data.to_dict()
            model_breakdown.append(model_breakdown_item)

        decision_breakdown = []
        for decision_breakdown_item_data in self.decision_breakdown:
            decision_breakdown_item = decision_breakdown_item_data.to_dict()
            decision_breakdown.append(decision_breakdown_item)

        status_breakdown = []
        for status_breakdown_item_data in self.status_breakdown:
            status_breakdown_item = status_breakdown_item_data.to_dict()
            status_breakdown.append(status_breakdown_item)

        shard_breakdown = []
        for shard_breakdown_item_data in self.shard_breakdown:
            shard_breakdown_item = shard_breakdown_item_data.to_dict()
            shard_breakdown.append(shard_breakdown_item)

        shared_candidate_runtime_status = self.shared_candidate_runtime_status.value

        shared_candidate_runtime_refs_total = self.shared_candidate_runtime_refs_total

        shared_candidate_runtime_refs_included = (
            self.shared_candidate_runtime_refs_included
        )

        coverage_from: None | str
        if isinstance(self.coverage_from, datetime.datetime):
            coverage_from = self.coverage_from.isoformat()
        else:
            coverage_from = self.coverage_from

        coverage_through: None | str
        if isinstance(self.coverage_through, datetime.datetime):
            coverage_through = self.coverage_through.isoformat()
        else:
            coverage_through = self.coverage_through

        complete = self.complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "router_id": router_id,
                "interval": interval,
                "summary": summary,
                "time_series": time_series,
                "model_breakdown": model_breakdown,
                "decision_breakdown": decision_breakdown,
                "status_breakdown": status_breakdown,
                "shard_breakdown": shard_breakdown,
                "shared_candidate_runtime_status": shared_candidate_runtime_status,
                "shared_candidate_runtime_refs_total": shared_candidate_runtime_refs_total,
                "shared_candidate_runtime_refs_included": shared_candidate_runtime_refs_included,
                "coverage_from": coverage_from,
                "coverage_through": coverage_through,
                "complete": complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_analytics_breakdown import (
            InferenceRouterAnalyticsBreakdown,
        )
        from ..models.inference_router_analytics_metrics import (
            InferenceRouterAnalyticsMetrics,
        )
        from ..models.inference_router_analytics_point import (
            InferenceRouterAnalyticsPoint,
        )

        d = dict(src_dict)
        router_id = d.pop("router_id")

        interval = InferenceRouterAnalyticsInterval(d.pop("interval"))

        summary = InferenceRouterAnalyticsMetrics.from_dict(d.pop("summary"))

        time_series = []
        _time_series = d.pop("time_series")
        for time_series_item_data in _time_series:
            time_series_item = InferenceRouterAnalyticsPoint.from_dict(
                time_series_item_data
            )

            time_series.append(time_series_item)

        model_breakdown = []
        _model_breakdown = d.pop("model_breakdown")
        for model_breakdown_item_data in _model_breakdown:
            model_breakdown_item = InferenceRouterAnalyticsBreakdown.from_dict(
                model_breakdown_item_data
            )

            model_breakdown.append(model_breakdown_item)

        decision_breakdown = []
        _decision_breakdown = d.pop("decision_breakdown")
        for decision_breakdown_item_data in _decision_breakdown:
            decision_breakdown_item = InferenceRouterAnalyticsBreakdown.from_dict(
                decision_breakdown_item_data
            )

            decision_breakdown.append(decision_breakdown_item)

        status_breakdown = []
        _status_breakdown = d.pop("status_breakdown")
        for status_breakdown_item_data in _status_breakdown:
            status_breakdown_item = InferenceRouterAnalyticsBreakdown.from_dict(
                status_breakdown_item_data
            )

            status_breakdown.append(status_breakdown_item)

        shard_breakdown = []
        _shard_breakdown = d.pop("shard_breakdown")
        for shard_breakdown_item_data in _shard_breakdown:
            shard_breakdown_item = InferenceRouterAnalyticsBreakdown.from_dict(
                shard_breakdown_item_data
            )

            shard_breakdown.append(shard_breakdown_item)

        shared_candidate_runtime_status = (
            InferenceRouterAnalyticsSharedCandidateRuntimeStatus(
                d.pop("shared_candidate_runtime_status")
            )
        )

        shared_candidate_runtime_refs_total = d.pop(
            "shared_candidate_runtime_refs_total"
        )

        shared_candidate_runtime_refs_included = d.pop(
            "shared_candidate_runtime_refs_included"
        )

        def _parse_coverage_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coverage_from_type_0 = datetime.datetime.fromisoformat(data)

                return coverage_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        coverage_from = _parse_coverage_from(d.pop("coverage_from"))

        def _parse_coverage_through(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coverage_through_type_0 = datetime.datetime.fromisoformat(data)

                return coverage_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        coverage_through = _parse_coverage_through(d.pop("coverage_through"))

        complete = d.pop("complete")

        inference_router_analytics = cls(
            router_id=router_id,
            interval=interval,
            summary=summary,
            time_series=time_series,
            model_breakdown=model_breakdown,
            decision_breakdown=decision_breakdown,
            status_breakdown=status_breakdown,
            shard_breakdown=shard_breakdown,
            shared_candidate_runtime_status=shared_candidate_runtime_status,
            shared_candidate_runtime_refs_total=shared_candidate_runtime_refs_total,
            shared_candidate_runtime_refs_included=shared_candidate_runtime_refs_included,
            coverage_from=coverage_from,
            coverage_through=coverage_through,
            complete=complete,
        )

        inference_router_analytics.additional_properties = d
        return inference_router_analytics

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
