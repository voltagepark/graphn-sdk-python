from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_resource_item_spec import BundleResourceItemSpec


T = TypeVar("T", bound="BundleResourceItem")


@_attrs_define
class BundleResourceItem:
    """
    Attributes:
        name (str):
        id (str | Unset):
        spec (BundleResourceItemSpec | Unset):
    """

    name: str
    id: str | Unset = UNSET
    spec: BundleResourceItemSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bundle_resource_item_spec import (
            BundleResourceItemSpec,
        )

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: BundleResourceItemSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = BundleResourceItemSpec.from_dict(_spec)

        bundle_resource_item = cls(
            name=name,
            id=id,
            spec=spec,
        )

        bundle_resource_item.additional_properties = d
        return bundle_resource_item

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
