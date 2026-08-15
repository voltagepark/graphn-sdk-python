from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportedModel")


@_attrs_define
class ImportedModel:
    """
    Attributes:
        id (str):
        name (str):
        display_name (str):
        workspace_id (str):
        endpoint (str):
        model_id (str):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        owner_id (str | Unset):
        api_key_secret_id (str | Unset):
        type_ (str | Unset):
        capabilities (list[str] | Unset):
        context_length (int | Unset):
        description (str | Unset):
    """

    id: str
    name: str
    display_name: str
    workspace_id: str
    endpoint: str
    model_id: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    owner_id: str | Unset = UNSET
    api_key_secret_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    context_length: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        workspace_id = self.workspace_id

        endpoint = self.endpoint

        model_id = self.model_id

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        owner_id = self.owner_id

        api_key_secret_id = self.api_key_secret_id

        type_ = self.type_

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        context_length = self.context_length

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "workspace_id": workspace_id,
                "endpoint": endpoint,
                "model_id": model_id,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
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
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("display_name")

        workspace_id = d.pop("workspace_id")

        endpoint = d.pop("endpoint")

        model_id = d.pop("model_id")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        owner_id = d.pop("owner_id", UNSET)

        api_key_secret_id = d.pop("api_key_secret_id", UNSET)

        type_ = d.pop("type", UNSET)

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        context_length = d.pop("context_length", UNSET)

        description = d.pop("description", UNSET)

        imported_model = cls(
            id=id,
            name=name,
            display_name=display_name,
            workspace_id=workspace_id,
            endpoint=endpoint,
            model_id=model_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            owner_id=owner_id,
            api_key_secret_id=api_key_secret_id,
            type_=type_,
            capabilities=capabilities,
            context_length=context_length,
            description=description,
        )

        imported_model.additional_properties = d
        return imported_model

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
