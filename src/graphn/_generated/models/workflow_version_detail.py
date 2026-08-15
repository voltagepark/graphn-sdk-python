from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_version_detail_resource_pins import (
        WorkflowVersionDetailResourcePins,
    )
    from ..models.workflow_version_detail_resource_snapshots import (
        WorkflowVersionDetailResourceSnapshots,
    )


T = TypeVar("T", bound="WorkflowVersionDetail")


@_attrs_define
class WorkflowVersionDetail:
    """
    Attributes:
        version_id (str):
        version_number (int):
        created_at (datetime.datetime):
        snapshot_id (str | Unset):
        message (str | Unset):
        dsl (str | Unset):
        resource_pins (WorkflowVersionDetailResourcePins | Unset):
        resource_snapshots (WorkflowVersionDetailResourceSnapshots | Unset):
    """

    version_id: str
    version_number: int
    created_at: datetime.datetime
    snapshot_id: str | Unset = UNSET
    message: str | Unset = UNSET
    dsl: str | Unset = UNSET
    resource_pins: WorkflowVersionDetailResourcePins | Unset = UNSET
    resource_snapshots: WorkflowVersionDetailResourceSnapshots | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        version_number = self.version_number

        created_at = self.created_at.isoformat()

        snapshot_id = self.snapshot_id

        message = self.message

        dsl = self.dsl

        resource_pins: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_pins, Unset):
            resource_pins = self.resource_pins.to_dict()

        resource_snapshots: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_snapshots, Unset):
            resource_snapshots = self.resource_snapshots.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version_id": version_id,
                "version_number": version_number,
                "created_at": created_at,
            }
        )
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if message is not UNSET:
            field_dict["message"] = message
        if dsl is not UNSET:
            field_dict["dsl"] = dsl
        if resource_pins is not UNSET:
            field_dict["resource_pins"] = resource_pins
        if resource_snapshots is not UNSET:
            field_dict["resource_snapshots"] = resource_snapshots

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workflow_version_detail_resource_pins import (
            WorkflowVersionDetailResourcePins,
        )
        from ..models.workflow_version_detail_resource_snapshots import (
            WorkflowVersionDetailResourceSnapshots,
        )

        d = dict(src_dict)
        version_id = d.pop("version_id")

        version_number = d.pop("version_number")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        snapshot_id = d.pop("snapshot_id", UNSET)

        message = d.pop("message", UNSET)

        dsl = d.pop("dsl", UNSET)

        _resource_pins = d.pop("resource_pins", UNSET)
        resource_pins: WorkflowVersionDetailResourcePins | Unset
        if isinstance(_resource_pins, Unset):
            resource_pins = UNSET
        else:
            resource_pins = WorkflowVersionDetailResourcePins.from_dict(_resource_pins)

        _resource_snapshots = d.pop("resource_snapshots", UNSET)
        resource_snapshots: WorkflowVersionDetailResourceSnapshots | Unset
        if isinstance(_resource_snapshots, Unset):
            resource_snapshots = UNSET
        else:
            resource_snapshots = WorkflowVersionDetailResourceSnapshots.from_dict(
                _resource_snapshots
            )

        workflow_version_detail = cls(
            version_id=version_id,
            version_number=version_number,
            created_at=created_at,
            snapshot_id=snapshot_id,
            message=message,
            dsl=dsl,
            resource_pins=resource_pins,
            resource_snapshots=resource_snapshots,
        )

        workflow_version_detail.additional_properties = d
        return workflow_version_detail

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
