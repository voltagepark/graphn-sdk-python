from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key import ApiKey


T = TypeVar("T", bound="ApiKeyList")


@_attrs_define
class ApiKeyList:
    """
    Attributes:
        api_keys (list[ApiKey]):
        continue_token (str | Unset):
    """

    api_keys: list[ApiKey]
    continue_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        continue_token = self.continue_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_keys": api_keys,
            }
        )
        if continue_token is not UNSET:
            field_dict["continue_token"] = continue_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_key import ApiKey

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = ApiKey.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        continue_token = d.pop("continue_token", UNSET)

        api_key_list = cls(
            api_keys=api_keys,
            continue_token=continue_token,
        )

        api_key_list.additional_properties = d
        return api_key_list

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
