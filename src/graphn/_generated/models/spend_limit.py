from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spend_limit_enforcement_state import SpendLimitEnforcementState
from ..models.spend_limit_period import SpendLimitPeriod
from ..models.spend_limit_reset_period import SpendLimitResetPeriod
from ..models.spend_limit_scope import SpendLimitScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendLimit")


@_attrs_define
class SpendLimit:
    """
    Attributes:
        org_id (str):
        scope (SpendLimitScope):
        subject_id (str):
        period (SpendLimitPeriod):
        reset_period (SpendLimitResetPeriod):
        limit_micros (int | None): Null means unlimited; zero is an explicit deny-all cap.
        enforcement_state (SpendLimitEnforcementState): Whether spend-limit enforcement is active for the current UTC
            window.
        enforcement_starts_at (datetime.datetime): Empty string when active; otherwise the UTC boundary when deferred
            enforcement begins.
        version (int | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    org_id: str
    scope: SpendLimitScope
    subject_id: str
    period: SpendLimitPeriod
    reset_period: SpendLimitResetPeriod
    limit_micros: int | None
    enforcement_state: SpendLimitEnforcementState
    enforcement_starts_at: datetime.datetime
    version: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        scope = self.scope.value

        subject_id = self.subject_id

        period = self.period.value

        reset_period = self.reset_period.value

        limit_micros: int | None
        limit_micros = self.limit_micros

        enforcement_state = self.enforcement_state.value

        enforcement_starts_at = self.enforcement_starts_at.isoformat()

        version = self.version

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "scope": scope,
                "subjectId": subject_id,
                "period": period,
                "resetPeriod": reset_period,
                "limitMicros": limit_micros,
                "enforcementState": enforcement_state,
                "enforcementStartsAt": enforcement_starts_at,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        scope = SpendLimitScope(d.pop("scope"))

        subject_id = d.pop("subjectId")

        period = SpendLimitPeriod(d.pop("period"))

        reset_period = SpendLimitResetPeriod(d.pop("resetPeriod"))

        def _parse_limit_micros(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        limit_micros = _parse_limit_micros(d.pop("limitMicros"))

        enforcement_state = SpendLimitEnforcementState(d.pop("enforcementState"))

        enforcement_starts_at = datetime.datetime.fromisoformat(
            d.pop("enforcementStartsAt")
        )

        version = d.pop("version", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        spend_limit = cls(
            org_id=org_id,
            scope=scope,
            subject_id=subject_id,
            period=period,
            reset_period=reset_period,
            limit_micros=limit_micros,
            enforcement_state=enforcement_state,
            enforcement_starts_at=enforcement_starts_at,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
        )

        spend_limit.additional_properties = d
        return spend_limit

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
