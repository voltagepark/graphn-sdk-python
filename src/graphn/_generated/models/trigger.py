from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_input import TriggerInput


T = TypeVar("T", bound="Trigger")


@_attrs_define
class Trigger:
    """
    Attributes:
        id (str):
        workspace_id (str):
        workflow_id (str):
        name (str):
        enabled (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        cron_schedule (str | Unset):
        input_ (TriggerInput | Unset):
        temporal_schedule_id (str | Unset):
        schedule_synced (bool | Unset):
        schedule_status (str | Unset):
        last_error (str | Unset):
        webhook_auth (str | Unset):
        hmac_secret_id (str | Unset):
        hmac_algorithm (str | Unset):
        hmac_signature_header (str | Unset):
        webhook_signature_scheme (str | Unset):
        owner_user_id (str | Unset):
        owner_org_id (str | Unset):
    """

    id: str
    workspace_id: str
    workflow_id: str
    name: str
    enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    cron_schedule: str | Unset = UNSET
    input_: TriggerInput | Unset = UNSET
    temporal_schedule_id: str | Unset = UNSET
    schedule_synced: bool | Unset = UNSET
    schedule_status: str | Unset = UNSET
    last_error: str | Unset = UNSET
    webhook_auth: str | Unset = UNSET
    hmac_secret_id: str | Unset = UNSET
    hmac_algorithm: str | Unset = UNSET
    hmac_signature_header: str | Unset = UNSET
    webhook_signature_scheme: str | Unset = UNSET
    owner_user_id: str | Unset = UNSET
    owner_org_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        workflow_id = self.workflow_id

        name = self.name

        enabled = self.enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cron_schedule = self.cron_schedule

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        temporal_schedule_id = self.temporal_schedule_id

        schedule_synced = self.schedule_synced

        schedule_status = self.schedule_status

        last_error = self.last_error

        webhook_auth = self.webhook_auth

        hmac_secret_id = self.hmac_secret_id

        hmac_algorithm = self.hmac_algorithm

        hmac_signature_header = self.hmac_signature_header

        webhook_signature_scheme = self.webhook_signature_scheme

        owner_user_id = self.owner_user_id

        owner_org_id = self.owner_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "workflow_id": workflow_id,
                "name": name,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule
        if input_ is not UNSET:
            field_dict["input"] = input_
        if temporal_schedule_id is not UNSET:
            field_dict["temporal_schedule_id"] = temporal_schedule_id
        if schedule_synced is not UNSET:
            field_dict["schedule_synced"] = schedule_synced
        if schedule_status is not UNSET:
            field_dict["schedule_status"] = schedule_status
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if webhook_auth is not UNSET:
            field_dict["webhook_auth"] = webhook_auth
        if hmac_secret_id is not UNSET:
            field_dict["hmac_secret_id"] = hmac_secret_id
        if hmac_algorithm is not UNSET:
            field_dict["hmac_algorithm"] = hmac_algorithm
        if hmac_signature_header is not UNSET:
            field_dict["hmac_signature_header"] = hmac_signature_header
        if webhook_signature_scheme is not UNSET:
            field_dict["webhook_signature_scheme"] = webhook_signature_scheme
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if owner_org_id is not UNSET:
            field_dict["owner_org_id"] = owner_org_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.trigger_input import TriggerInput

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        workflow_id = d.pop("workflow_id")

        name = d.pop("name")

        enabled = d.pop("enabled")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        cron_schedule = d.pop("cron_schedule", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: TriggerInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = TriggerInput.from_dict(_input_)

        temporal_schedule_id = d.pop("temporal_schedule_id", UNSET)

        schedule_synced = d.pop("schedule_synced", UNSET)

        schedule_status = d.pop("schedule_status", UNSET)

        last_error = d.pop("last_error", UNSET)

        webhook_auth = d.pop("webhook_auth", UNSET)

        hmac_secret_id = d.pop("hmac_secret_id", UNSET)

        hmac_algorithm = d.pop("hmac_algorithm", UNSET)

        hmac_signature_header = d.pop("hmac_signature_header", UNSET)

        webhook_signature_scheme = d.pop("webhook_signature_scheme", UNSET)

        owner_user_id = d.pop("owner_user_id", UNSET)

        owner_org_id = d.pop("owner_org_id", UNSET)

        trigger = cls(
            id=id,
            workspace_id=workspace_id,
            workflow_id=workflow_id,
            name=name,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            cron_schedule=cron_schedule,
            input_=input_,
            temporal_schedule_id=temporal_schedule_id,
            schedule_synced=schedule_synced,
            schedule_status=schedule_status,
            last_error=last_error,
            webhook_auth=webhook_auth,
            hmac_secret_id=hmac_secret_id,
            hmac_algorithm=hmac_algorithm,
            hmac_signature_header=hmac_signature_header,
            webhook_signature_scheme=webhook_signature_scheme,
            owner_user_id=owner_user_id,
            owner_org_id=owner_org_id,
        )

        trigger.additional_properties = d
        return trigger

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
