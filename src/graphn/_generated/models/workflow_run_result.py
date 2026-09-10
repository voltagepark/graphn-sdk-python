from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_run_result_node_results_item import (
        WorkflowRunResultNodeResultsItem,
    )
    from ..models.workflow_run_result_resources_accessed_item import (
        WorkflowRunResultResourcesAccessedItem,
    )
    from ..models.workflow_run_result_trace import WorkflowRunResultTrace


T = TypeVar("T", bound="WorkflowRunResult")


@_attrs_define
class WorkflowRunResult:
    """
    Attributes:
        execution_id (str | Unset):
        status (str | Unset):
        output (Any | Unset):
        error (str | Unset):
        trace (WorkflowRunResultTrace | Unset):
        node_results (list[WorkflowRunResultNodeResultsItem] | Unset):
        resources_accessed (list[WorkflowRunResultResourcesAccessedItem] | Unset):
        duration_ms (int | Unset):
    """

    execution_id: str | Unset = UNSET
    status: str | Unset = UNSET
    output: Any | Unset = UNSET
    error: str | Unset = UNSET
    trace: WorkflowRunResultTrace | Unset = UNSET
    node_results: list[WorkflowRunResultNodeResultsItem] | Unset = UNSET
    resources_accessed: list[WorkflowRunResultResourcesAccessedItem] | Unset = UNSET
    duration_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        status = self.status

        output = self.output

        error = self.error

        trace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace, Unset):
            trace = self.trace.to_dict()

        node_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node_results, Unset):
            node_results = []
            for node_results_item_data in self.node_results:
                node_results_item = node_results_item_data.to_dict()
                node_results.append(node_results_item)

        resources_accessed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources_accessed, Unset):
            resources_accessed = []
            for resources_accessed_item_data in self.resources_accessed:
                resources_accessed_item = resources_accessed_item_data.to_dict()
                resources_accessed.append(resources_accessed_item)

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if status is not UNSET:
            field_dict["status"] = status
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if trace is not UNSET:
            field_dict["trace"] = trace
        if node_results is not UNSET:
            field_dict["node_results"] = node_results
        if resources_accessed is not UNSET:
            field_dict["resources_accessed"] = resources_accessed
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_run_result_node_results_item import (
            WorkflowRunResultNodeResultsItem,
        )
        from ..models.workflow_run_result_resources_accessed_item import (
            WorkflowRunResultResourcesAccessedItem,
        )
        from ..models.workflow_run_result_trace import (
            WorkflowRunResultTrace,
        )

        d = dict(src_dict)
        execution_id = d.pop("execution_id", UNSET)

        status = d.pop("status", UNSET)

        output = d.pop("output", UNSET)

        error = d.pop("error", UNSET)

        _trace = d.pop("trace", UNSET)
        trace: WorkflowRunResultTrace | Unset
        if isinstance(_trace, Unset):
            trace = UNSET
        else:
            trace = WorkflowRunResultTrace.from_dict(_trace)

        _node_results = d.pop("node_results", UNSET)
        node_results: list[WorkflowRunResultNodeResultsItem] | Unset = UNSET
        if _node_results is not UNSET:
            node_results = []
            for node_results_item_data in _node_results:
                node_results_item = WorkflowRunResultNodeResultsItem.from_dict(
                    node_results_item_data
                )

                node_results.append(node_results_item)

        _resources_accessed = d.pop("resources_accessed", UNSET)
        resources_accessed: list[WorkflowRunResultResourcesAccessedItem] | Unset = UNSET
        if _resources_accessed is not UNSET:
            resources_accessed = []
            for resources_accessed_item_data in _resources_accessed:
                resources_accessed_item = (
                    WorkflowRunResultResourcesAccessedItem.from_dict(
                        resources_accessed_item_data
                    )
                )

                resources_accessed.append(resources_accessed_item)

        duration_ms = d.pop("duration_ms", UNSET)

        workflow_run_result = cls(
            execution_id=execution_id,
            status=status,
            output=output,
            error=error,
            trace=trace,
            node_results=node_results,
            resources_accessed=resources_accessed,
            duration_ms=duration_ms,
        )

        workflow_run_result.additional_properties = d
        return workflow_run_result

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
