from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="KnowledgeBaseStats")


@_attrs_define
class KnowledgeBaseStats:
    """
    Attributes:
        id (str):
        name (str):
        document_count (int):
        chunk_count (int):
        vector_count (int):
        status (str):
    """

    id: str
    name: str
    document_count: int
    chunk_count: int
    vector_count: int
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        document_count = self.document_count

        chunk_count = self.chunk_count

        vector_count = self.vector_count

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "document_count": document_count,
                "chunk_count": chunk_count,
                "vector_count": vector_count,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        document_count = d.pop("document_count")

        chunk_count = d.pop("chunk_count")

        vector_count = d.pop("vector_count")

        status = d.pop("status")

        knowledge_base_stats = cls(
            id=id,
            name=name,
            document_count=document_count,
            chunk_count=chunk_count,
            vector_count=vector_count,
            status=status,
        )

        knowledge_base_stats.additional_properties = d
        return knowledge_base_stats

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
