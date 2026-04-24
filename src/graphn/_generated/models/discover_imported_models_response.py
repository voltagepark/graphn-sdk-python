from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.discovered_imported_model import DiscoveredImportedModel


T = TypeVar("T", bound="DiscoverImportedModelsResponse")


@_attrs_define
class DiscoverImportedModelsResponse:
    """
    Attributes:
        models (list[DiscoveredImportedModel]):
    """

    models: list[DiscoveredImportedModel]

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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovered_imported_model import DiscoveredImportedModel

        d = dict(src_dict)
        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = DiscoveredImportedModel.from_dict(models_item_data)

            models.append(models_item)

        discover_imported_models_response = cls(
            models=models,
        )

        return discover_imported_models_response
