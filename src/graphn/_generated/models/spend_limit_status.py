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

T = TypeVar("T", bound="SpendLimitStatus")


@_attrs_define
class SpendLimitStatus:
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
        period_start (datetime.datetime): Aligned UTC period start for the active reset period.
        spent_micros (int): Committed journal spend in integer micro-USD.
        remaining_micros (int | None): Nonnegative limit remainder (limit minus settled spend, reservations not
            subtracted); null when unlimited.
        reserved_micros (int): Active unexpired reserved micro-USD for the same subject and reset window.
        available_micros (int | None): Nonnegative admission budget (limit minus settled spend minus reserved); null
            when unlimited.
        can_admit_next_run (bool): Whether a new run can reserve its fixed per-run hold against this subject now.
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
    period_start: datetime.datetime
    spent_micros: int
    remaining_micros: int | None
    reserved_micros: int
    available_micros: int | None
    can_admit_next_run: bool
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

        period_start = self.period_start.isoformat()

        spent_micros = self.spent_micros

        remaining_micros: int | None
        remaining_micros = self.remaining_micros

        reserved_micros = self.reserved_micros

        available_micros: int | None
        available_micros = self.available_micros

        can_admit_next_run = self.can_admit_next_run

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
                "periodStart": period_start,
                "spentMicros": spent_micros,
                "remainingMicros": remaining_micros,
                "reservedMicros": reserved_micros,
                "availableMicros": available_micros,
                "canAdmitNextRun": can_admit_next_run,
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

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        spent_micros = d.pop("spentMicros")

        def _parse_remaining_micros(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remaining_micros = _parse_remaining_micros(d.pop("remainingMicros"))

        reserved_micros = d.pop("reservedMicros")

        def _parse_available_micros(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        available_micros = _parse_available_micros(d.pop("availableMicros"))

        can_admit_next_run = d.pop("canAdmitNextRun")

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

        spend_limit_status = cls(
            org_id=org_id,
            scope=scope,
            subject_id=subject_id,
            period=period,
            reset_period=reset_period,
            limit_micros=limit_micros,
            enforcement_state=enforcement_state,
            enforcement_starts_at=enforcement_starts_at,
            period_start=period_start,
            spent_micros=spent_micros,
            remaining_micros=remaining_micros,
            reserved_micros=reserved_micros,
            available_micros=available_micros,
            can_admit_next_run=can_admit_next_run,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
        )

        spend_limit_status.additional_properties = d
        return spend_limit_status

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
