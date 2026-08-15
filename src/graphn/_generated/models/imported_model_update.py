from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportedModelUpdate")


@_attrs_define
class ImportedModelUpdate:
    """
    Attributes:
        name (str | Unset):
        display_name (str | Unset):
        endpoint (str | Unset):
        model_id (str | Unset):
        api_key_secret_id (str | Unset):
        type_ (str | Unset):
        capabilities (list[str] | Unset):
        context_length (int | Unset):
        description (str | Unset):
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    endpoint: str | Unset = UNSET
    model_id: str | Unset = UNSET
    api_key_secret_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    context_length: int | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        endpoint = self.endpoint

        model_id = self.model_id

        api_key_secret_id = self.api_key_secret_id

        type_ = self.type_

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        context_length = self.context_length

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if api_key_secret_id is not UNSET:
            field_dict["api_key_secret_id"] = api_key_secret_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if context_length is not UNSET:
            field_dict["context_length"] = context_length
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("display_name", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        model_id = d.pop("model_id", UNSET)

        api_key_secret_id = d.pop("api_key_secret_id", UNSET)

        type_ = d.pop("type", UNSET)

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        context_length = d.pop("context_length", UNSET)

        description = d.pop("description", UNSET)

        imported_model_update = cls(
            name=name,
            display_name=display_name,
            endpoint=endpoint,
            model_id=model_id,
            api_key_secret_id=api_key_secret_id,
            type_=type_,
            capabilities=capabilities,
            context_length=context_length,
            description=description,
        )

        return imported_model_update
