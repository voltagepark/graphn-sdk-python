from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeBaseCreate")


@_attrs_define
class KnowledgeBaseCreate:
    """
    Attributes:
        name (str):
        description (str | Unset):
        embedding_model (str | Unset):
        chunk_size (int | Unset):
        chunk_overlap (int | Unset):
    """

    name: str
    description: str | Unset = UNSET
    embedding_model: str | Unset = UNSET
    chunk_size: int | Unset = UNSET
    chunk_overlap: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        embedding_model = self.embedding_model

        chunk_size = self.chunk_size

        chunk_overlap = self.chunk_overlap

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        embedding_model = d.pop("embedding_model", UNSET)

        chunk_size = d.pop("chunk_size", UNSET)

        chunk_overlap = d.pop("chunk_overlap", UNSET)

        knowledge_base_create = cls(
            name=name,
            description=description,
            embedding_model=embedding_model,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        return knowledge_base_create
