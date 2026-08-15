from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kb_batch_error import KbBatchError
    from ..models.knowledge_base import KnowledgeBase


T = TypeVar("T", bound="BatchKnowledgebaseResult")


@_attrs_define
class BatchKnowledgebaseResult:
    """
    Attributes:
        id (str | Unset):
        knowledgebase (KnowledgeBase | Unset):
        error (KbBatchError | Unset):
    """

    id: str | Unset = UNSET
    knowledgebase: KnowledgeBase | Unset = UNSET
    error: KbBatchError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        knowledgebase: dict[str, Any] | Unset = UNSET
        if not isinstance(self.knowledgebase, Unset):
            knowledgebase = self.knowledgebase.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if knowledgebase is not UNSET:
            field_dict["knowledgebase"] = knowledgebase
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kb_batch_error import KbBatchError
        from ..models.knowledge_base import KnowledgeBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _knowledgebase = d.pop("knowledgebase", UNSET)
        knowledgebase: KnowledgeBase | Unset
        if isinstance(_knowledgebase, Unset):
            knowledgebase = UNSET
        else:
            knowledgebase = KnowledgeBase.from_dict(_knowledgebase)

        _error = d.pop("error", UNSET)
        error: KbBatchError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = KbBatchError.from_dict(_error)

        batch_knowledgebase_result = cls(
            id=id,
            knowledgebase=knowledgebase,
            error=error,
        )

        batch_knowledgebase_result.additional_properties = d
        return batch_knowledgebase_result

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
