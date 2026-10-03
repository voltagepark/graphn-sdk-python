from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.inference_router_revision_shard_placements_item_role import (
    InferenceRouterRevisionShardPlacementsItemRole,
)
from ..models.inference_router_revision_shard_placements_item_state import (
    InferenceRouterRevisionShardPlacementsItemState,
)

T = TypeVar("T", bound="InferenceRouterRevisionShardPlacementsItem")


@_attrs_define
class InferenceRouterRevisionShardPlacementsItem:
    """
    Attributes:
        shard_id (str):
        alias (str):
        role (InferenceRouterRevisionShardPlacementsItemRole):
        state (InferenceRouterRevisionShardPlacementsItemState):
    """

    shard_id: str
    alias: str
    role: InferenceRouterRevisionShardPlacementsItemRole
    state: InferenceRouterRevisionShardPlacementsItemState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shard_id = self.shard_id

        alias = self.alias

        role = self.role.value

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shard_id": shard_id,
                "alias": alias,
                "role": role,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shard_id = d.pop("shard_id")

        alias = d.pop("alias")

        role = InferenceRouterRevisionShardPlacementsItemRole(d.pop("role"))

        state = InferenceRouterRevisionShardPlacementsItemState(d.pop("state"))

        inference_router_revision_shard_placements_item = cls(
            shard_id=shard_id,
            alias=alias,
            role=role,
            state=state,
        )

        inference_router_revision_shard_placements_item.additional_properties = d
        return inference_router_revision_shard_placements_item

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
