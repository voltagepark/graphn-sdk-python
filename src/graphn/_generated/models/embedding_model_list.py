from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.embedding_model import EmbeddingModel


T = TypeVar("T", bound="EmbeddingModelList")


@_attrs_define
class EmbeddingModelList:
    """
    Attributes:
        models (list[EmbeddingModel]):
    """

    models: list[EmbeddingModel]

    def to_dict(self) -> dict[str, Any]:
        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "models": models,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embedding_model import EmbeddingModel

        d = dict(src_dict)
        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = EmbeddingModel.from_dict(models_item_data)

            models.append(models_item)

        embedding_model_list = cls(
            models=models,
        )

        return embedding_model_list
