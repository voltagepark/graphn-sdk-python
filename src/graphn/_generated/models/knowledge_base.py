from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeBase")


@_attrs_define
class KnowledgeBase:
    """
    Attributes:
        id (str):
        name (str):
        workspace_id (str):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (str | Unset):
        created_by (str | Unset):
        document_count (int | Unset):
        chunk_count (int | Unset):
        embedding_model (str | Unset):
        chunk_size (int | Unset):
        chunk_overlap (int | Unset):
    """

    id: str
    name: str
    workspace_id: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    created_by: str | Unset = UNSET
    document_count: int | Unset = UNSET
    chunk_count: int | Unset = UNSET
    embedding_model: str | Unset = UNSET
    chunk_size: int | Unset = UNSET
    chunk_overlap: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        workspace_id = self.workspace_id

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        created_by = self.created_by

        document_count = self.document_count

        chunk_count = self.chunk_count

        embedding_model = self.embedding_model

        chunk_size = self.chunk_size

        chunk_overlap = self.chunk_overlap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "workspace_id": workspace_id,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if document_count is not UNSET:
            field_dict["document_count"] = document_count
        if chunk_count is not UNSET:
            field_dict["chunk_count"] = chunk_count
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
        id = d.pop("id")

        name = d.pop("name")

        workspace_id = d.pop("workspace_id")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        created_by = d.pop("created_by", UNSET)

        document_count = d.pop("document_count", UNSET)

        chunk_count = d.pop("chunk_count", UNSET)

        embedding_model = d.pop("embedding_model", UNSET)

        chunk_size = d.pop("chunk_size", UNSET)

        chunk_overlap = d.pop("chunk_overlap", UNSET)

        knowledge_base = cls(
            id=id,
            name=name,
            workspace_id=workspace_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            created_by=created_by,
            document_count=document_count,
            chunk_count=chunk_count,
            embedding_model=embedding_model,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        knowledge_base.additional_properties = d
        return knowledge_base

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
