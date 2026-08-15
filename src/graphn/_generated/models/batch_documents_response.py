from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.batch_document_result import BatchDocumentResult


T = TypeVar("T", bound="BatchDocumentsResponse")


@_attrs_define
class BatchDocumentsResponse:
    """
    Attributes:
        total (int):
        succeeded (int):
        failed (int):
        results (list[BatchDocumentResult]):
    """

    total: int
    succeeded: int
    failed: int
    results: list[BatchDocumentResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        succeeded = self.succeeded

        failed = self.failed

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "succeeded": succeeded,
                "failed": failed,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_document_result import BatchDocumentResult

        d = dict(src_dict)
        total = d.pop("total")

        succeeded = d.pop("succeeded")

        failed = d.pop("failed")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BatchDocumentResult.from_dict(results_item_data)

            results.append(results_item)

        batch_documents_response = cls(
            total=total,
            succeeded=succeeded,
            failed=failed,
            results=results,
        )

        batch_documents_response.additional_properties = d
        return batch_documents_response

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
