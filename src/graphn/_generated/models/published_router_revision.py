from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.published_router_revision_state import PublishedRouterRevisionState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.published_router_candidate import PublishedRouterCandidate
    from ..models.published_router_custom_lane import PublishedRouterCustomLane
    from ..models.published_router_decision import PublishedRouterDecision


T = TypeVar("T", bound="PublishedRouterRevision")


@_attrs_define
class PublishedRouterRevision:
    """
    Attributes:
        router_id (str):
        revision (str):
        state (PublishedRouterRevisionState):
        candidates (list[PublishedRouterCandidate]):
        decisions (list[PublishedRouterDecision]):
        general_candidate_refs (list[str]):
        manifest_hash (str):
        preferred_shard_id (str | Unset): Operator-owned placement hint; populated only for Platform Auto.
        custom_lanes (list[PublishedRouterCustomLane] | Unset): Snapshot of every workspace custom lane the revision
            uses.
    """

    router_id: str
    revision: str
    state: PublishedRouterRevisionState
    candidates: list[PublishedRouterCandidate]
    decisions: list[PublishedRouterDecision]
    general_candidate_refs: list[str]
    manifest_hash: str
    preferred_shard_id: str | Unset = UNSET
    custom_lanes: list[PublishedRouterCustomLane] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        router_id = self.router_id

        revision = self.revision

        state = self.state.value

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        decisions = []
        for decisions_item_data in self.decisions:
            decisions_item = decisions_item_data.to_dict()
            decisions.append(decisions_item)

        general_candidate_refs = self.general_candidate_refs

        manifest_hash = self.manifest_hash

        preferred_shard_id = self.preferred_shard_id

        custom_lanes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_lanes, Unset):
            custom_lanes = []
            for custom_lanes_item_data in self.custom_lanes:
                custom_lanes_item = custom_lanes_item_data.to_dict()
                custom_lanes.append(custom_lanes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "router_id": router_id,
                "revision": revision,
                "state": state,
                "candidates": candidates,
                "decisions": decisions,
                "general_candidate_refs": general_candidate_refs,
                "manifest_hash": manifest_hash,
            }
        )
        if preferred_shard_id is not UNSET:
            field_dict["preferred_shard_id"] = preferred_shard_id
        if custom_lanes is not UNSET:
            field_dict["custom_lanes"] = custom_lanes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.published_router_candidate import (
            PublishedRouterCandidate,
        )
        from ..models.published_router_custom_lane import (
            PublishedRouterCustomLane,
        )
        from ..models.published_router_decision import (
            PublishedRouterDecision,
        )

        d = dict(src_dict)
        router_id = d.pop("router_id")

        revision = d.pop("revision")

        state = PublishedRouterRevisionState(d.pop("state"))

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = PublishedRouterCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        decisions = []
        _decisions = d.pop("decisions")
        for decisions_item_data in _decisions:
            decisions_item = PublishedRouterDecision.from_dict(decisions_item_data)

            decisions.append(decisions_item)

        general_candidate_refs = cast(list[str], d.pop("general_candidate_refs"))

        manifest_hash = d.pop("manifest_hash")

        preferred_shard_id = d.pop("preferred_shard_id", UNSET)

        _custom_lanes = d.pop("custom_lanes", UNSET)
        custom_lanes: list[PublishedRouterCustomLane] | Unset = UNSET
        if _custom_lanes is not UNSET:
            custom_lanes = []
            for custom_lanes_item_data in _custom_lanes:
                custom_lanes_item = PublishedRouterCustomLane.from_dict(
                    custom_lanes_item_data
                )

                custom_lanes.append(custom_lanes_item)

        published_router_revision = cls(
            router_id=router_id,
            revision=revision,
            state=state,
            candidates=candidates,
            decisions=decisions,
            general_candidate_refs=general_candidate_refs,
            manifest_hash=manifest_hash,
            preferred_shard_id=preferred_shard_id,
            custom_lanes=custom_lanes,
        )

        published_router_revision.additional_properties = d
        return published_router_revision

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
