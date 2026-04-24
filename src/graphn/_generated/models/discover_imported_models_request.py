from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DiscoverImportedModelsRequest")


@_attrs_define
class DiscoverImportedModelsRequest:
    """
    Attributes:
        endpoint (str): Base URL of the OpenAI-compatible endpoint.
        api_key_secret_id (str): Workspace secret containing the upstream API key.
    """

    endpoint: str
    api_key_secret_id: str

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        api_key_secret_id = self.api_key_secret_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
                "api_key_secret_id": api_key_secret_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        api_key_secret_id = d.pop("api_key_secret_id")

        discover_imported_models_request = cls(
            endpoint=endpoint,
            api_key_secret_id=api_key_secret_id,
        )

        return discover_imported_models_request
