from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingModel")


@_attrs_define
class EmbeddingModel:
    """
    Attributes:
        id (str):
        name (str):
        vector_size (int):
        supported_inputs (list[str]):
        is_default (bool):
        reranker_model (str | Unset):
    """

    id: str
    name: str
    vector_size: int
    supported_inputs: list[str]
    is_default: bool
    reranker_model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vector_size = self.vector_size

        supported_inputs = self.supported_inputs

        is_default = self.is_default

        reranker_model = self.reranker_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "vector_size": vector_size,
                "supported_inputs": supported_inputs,
                "is_default": is_default,
            }
        )
        if reranker_model is not UNSET:
            field_dict["reranker_model"] = reranker_model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        vector_size = d.pop("vector_size")

        supported_inputs = cast(list[str], d.pop("supported_inputs"))

        is_default = d.pop("is_default")

        reranker_model = d.pop("reranker_model", UNSET)

        embedding_model = cls(
            id=id,
            name=name,
            vector_size=vector_size,
            supported_inputs=supported_inputs,
            is_default=is_default,
            reranker_model=reranker_model,
        )

        embedding_model.additional_properties = d
        return embedding_model

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
