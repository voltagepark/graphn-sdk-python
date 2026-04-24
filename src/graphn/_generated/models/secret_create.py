from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretCreate")


@_attrs_define
class SecretCreate:
    """
    Attributes:
        name (str):
        value (str): Plaintext secret value. Encrypted at rest.
        provider_id (str | Unset):
        field_name (str | Unset):
    """

    name: str
    value: str
    provider_id: str | Unset = UNSET
    field_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        provider_id = self.provider_id

        field_name = self.field_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if field_name is not UNSET:
            field_dict["field_name"] = field_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        provider_id = d.pop("provider_id", UNSET)

        field_name = d.pop("field_name", UNSET)

        secret_create = cls(
            name=name,
            value=value,
            provider_id=provider_id,
            field_name=field_name,
        )

        return secret_create
