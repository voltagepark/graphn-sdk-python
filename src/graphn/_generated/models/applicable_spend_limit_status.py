from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.applicable_spend_limit_status_reset_period import (
    ApplicableSpendLimitStatusResetPeriod,
)
from ..models.applicable_spend_limit_status_scope import ApplicableSpendLimitStatusScope

T = TypeVar("T", bound="ApplicableSpendLimitStatus")


@_attrs_define
class ApplicableSpendLimitStatus:
    """
    Attributes:
        org_id (str):
        scope (ApplicableSpendLimitStatusScope):
        subject_id (str):
        reset_period (ApplicableSpendLimitStatusResetPeriod):
        period_start (datetime.datetime): Aligned UTC period start for the active reset period.
        limit_micros (int | None): Null means unlimited; zero is an explicit deny-all cap.
        spent_micros (int): Committed journal spend in integer micro-USD.
        remaining_micros (int | None): Nonnegative limit remainder; null when unlimited.
    """

    org_id: str
    scope: ApplicableSpendLimitStatusScope
    subject_id: str
    reset_period: ApplicableSpendLimitStatusResetPeriod
    period_start: datetime.datetime
    limit_micros: int | None
    spent_micros: int
    remaining_micros: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        scope = self.scope.value

        subject_id = self.subject_id

        reset_period = self.reset_period.value

        period_start = self.period_start.isoformat()

        limit_micros: int | None
        limit_micros = self.limit_micros

        spent_micros = self.spent_micros

        remaining_micros: int | None
        remaining_micros = self.remaining_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "scope": scope,
                "subjectId": subject_id,
                "resetPeriod": reset_period,
                "periodStart": period_start,
                "limitMicros": limit_micros,
                "spentMicros": spent_micros,
                "remainingMicros": remaining_micros,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        scope = ApplicableSpendLimitStatusScope(d.pop("scope"))

        subject_id = d.pop("subjectId")

        reset_period = ApplicableSpendLimitStatusResetPeriod(d.pop("resetPeriod"))

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        def _parse_limit_micros(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        limit_micros = _parse_limit_micros(d.pop("limitMicros"))

        spent_micros = d.pop("spentMicros")

        def _parse_remaining_micros(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remaining_micros = _parse_remaining_micros(d.pop("remainingMicros"))

        applicable_spend_limit_status = cls(
            org_id=org_id,
            scope=scope,
            subject_id=subject_id,
            reset_period=reset_period,
            period_start=period_start,
            limit_micros=limit_micros,
            spent_micros=spent_micros,
            remaining_micros=remaining_micros,
        )

        applicable_spend_limit_status.additional_properties = d
        return applicable_spend_limit_status

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
