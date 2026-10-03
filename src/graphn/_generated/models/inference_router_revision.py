from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.inference_router_revision_status import InferenceRouterRevisionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inference_router_config import InferenceRouterConfig
    from ..models.inference_router_revision_shard_placements_item import (
        InferenceRouterRevisionShardPlacementsItem,
    )
    from ..models.published_router_custom_lane import PublishedRouterCustomLane


T = TypeVar("T", bound="InferenceRouterRevision")


@_attrs_define
class InferenceRouterRevision:
    """
    Attributes:
        number (int):
        status (InferenceRouterRevisionStatus):
        config (InferenceRouterConfig):
        manifest_hash (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        shard_placements (list[InferenceRouterRevisionShardPlacementsItem] | Unset): Shards carrying this revision. A
            revision has one `primary` placement; a second `migrating` placement exists only while the revision is being
            moved to another shard.
        custom_lanes (list[PublishedRouterCustomLane] | Unset): The custom lane definitions this revision was saved
            with. Compare against the current lanes to tell when a router needs republishing.
        error_message (str | Unset):
    """

    number: int
    status: InferenceRouterRevisionStatus
    config: InferenceRouterConfig
    manifest_hash: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    shard_placements: list[InferenceRouterRevisionShardPlacementsItem] | Unset = UNSET
    custom_lanes: list[PublishedRouterCustomLane] | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        status = self.status.value

        config = self.config.to_dict()

        manifest_hash = self.manifest_hash

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        shard_placements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shard_placements, Unset):
            shard_placements = []
            for shard_placements_item_data in self.shard_placements:
                shard_placements_item = shard_placements_item_data.to_dict()
                shard_placements.append(shard_placements_item)

        custom_lanes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_lanes, Unset):
            custom_lanes = []
            for custom_lanes_item_data in self.custom_lanes:
                custom_lanes_item = custom_lanes_item_data.to_dict()
                custom_lanes.append(custom_lanes_item)

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "status": status,
                "config": config,
                "manifest_hash": manifest_hash,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if shard_placements is not UNSET:
            field_dict["shard_placements"] = shard_placements
        if custom_lanes is not UNSET:
            field_dict["custom_lanes"] = custom_lanes
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inference_router_config import (
            InferenceRouterConfig,
        )
        from ..models.inference_router_revision_shard_placements_item import (
            InferenceRouterRevisionShardPlacementsItem,
        )
        from ..models.published_router_custom_lane import (
            PublishedRouterCustomLane,
        )

        d = dict(src_dict)
        number = d.pop("number")

        status = InferenceRouterRevisionStatus(d.pop("status"))

        config = InferenceRouterConfig.from_dict(d.pop("config"))

        manifest_hash = d.pop("manifest_hash")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _shard_placements = d.pop("shard_placements", UNSET)
        shard_placements: list[InferenceRouterRevisionShardPlacementsItem] | Unset = (
            UNSET
        )
        if _shard_placements is not UNSET:
            shard_placements = []
            for shard_placements_item_data in _shard_placements:
                shard_placements_item = (
                    InferenceRouterRevisionShardPlacementsItem.from_dict(
                        shard_placements_item_data
                    )
                )

                shard_placements.append(shard_placements_item)

        _custom_lanes = d.pop("custom_lanes", UNSET)
        custom_lanes: list[PublishedRouterCustomLane] | Unset = UNSET
        if _custom_lanes is not UNSET:
            custom_lanes = []
            for custom_lanes_item_data in _custom_lanes:
                custom_lanes_item = PublishedRouterCustomLane.from_dict(
                    custom_lanes_item_data
                )

                custom_lanes.append(custom_lanes_item)

        error_message = d.pop("error_message", UNSET)

        inference_router_revision = cls(
            number=number,
            status=status,
            config=config,
            manifest_hash=manifest_hash,
            created_at=created_at,
            updated_at=updated_at,
            shard_placements=shard_placements,
            custom_lanes=custom_lanes,
            error_message=error_message,
        )

        inference_router_revision.additional_properties = d
        return inference_router_revision

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
