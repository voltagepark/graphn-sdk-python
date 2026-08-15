from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_update_input import TriggerUpdateInput


T = TypeVar("T", bound="TriggerUpdate")


@_attrs_define
class TriggerUpdate:
    """
    Attributes:
        name (str | Unset):
        cron_schedule (str | Unset):
        input_ (TriggerUpdateInput | Unset):
        enabled (bool | Unset):
        webhook_auth (str | Unset):
        hmac_secret_id (str | Unset):
        hmac_algorithm (str | Unset):
        hmac_signature_header (str | Unset):
        webhook_signature_scheme (str | Unset):
    """

    name: str | Unset = UNSET
    cron_schedule: str | Unset = UNSET
    input_: TriggerUpdateInput | Unset = UNSET
    enabled: bool | Unset = UNSET
    webhook_auth: str | Unset = UNSET
    hmac_secret_id: str | Unset = UNSET
    hmac_algorithm: str | Unset = UNSET
    hmac_signature_header: str | Unset = UNSET
    webhook_signature_scheme: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cron_schedule = self.cron_schedule

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        enabled = self.enabled

        webhook_auth = self.webhook_auth

        hmac_secret_id = self.hmac_secret_id

        hmac_algorithm = self.hmac_algorithm

        hmac_signature_header = self.hmac_signature_header

        webhook_signature_scheme = self.webhook_signature_scheme

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule
        if input_ is not UNSET:
            field_dict["input"] = input_
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.trigger_update_input import TriggerUpdateInput

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        cron_schedule = d.pop("cron_schedule", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: TriggerUpdateInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = TriggerUpdateInput.from_dict(_input_)

        enabled = d.pop("enabled", UNSET)

        webhook_auth = d.pop("webhook_auth", UNSET)

        hmac_secret_id = d.pop("hmac_secret_id", UNSET)

        hmac_algorithm = d.pop("hmac_algorithm", UNSET)

        hmac_signature_header = d.pop("hmac_signature_header", UNSET)

        webhook_signature_scheme = d.pop("webhook_signature_scheme", UNSET)

        trigger_update = cls(
            name=name,
            cron_schedule=cron_schedule,
            input_=input_,
            enabled=enabled,
            webhook_auth=webhook_auth,
            hmac_secret_id=hmac_secret_id,
            hmac_algorithm=hmac_algorithm,
            hmac_signature_header=hmac_signature_header,
            webhook_signature_scheme=webhook_signature_scheme,
        )

        return trigger_update
