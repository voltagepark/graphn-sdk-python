from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.spend_limit_upsert_reset_period import SpendLimitUpsertResetPeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendLimitUpsert")


@_attrs_define
class SpendLimitUpsert:
    """
    Attributes:
        limit_micros (int): Monetary cap in integer micro-USD. Zero denies all spend.
        reset_period (SpendLimitUpsertResetPeriod | Unset): Reset period for budget tracking. `five_minute` requires
            trusted admin JWT + AAL2 and is rejected for API key, builder-session, and internal credentials.
    """

    limit_micros: int
    reset_period: SpendLimitUpsertResetPeriod | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit_micros = self.limit_micros

        reset_period: str | Unset = UNSET
        if not isinstance(self.reset_period, Unset):
            reset_period = self.reset_period.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limitMicros": limit_micros,
            }
        )
        if reset_period is not UNSET:
            field_dict["resetPeriod"] = reset_period

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        limit_micros = d.pop("limitMicros")

        _reset_period = d.pop("resetPeriod", UNSET)
        reset_period: SpendLimitUpsertResetPeriod | Unset
        if isinstance(_reset_period, Unset):
            reset_period = UNSET
        else:
            reset_period = SpendLimitUpsertResetPeriod(_reset_period)

        spend_limit_upsert = cls(
            limit_micros=limit_micros,
            reset_period=reset_period,
        )

        return spend_limit_upsert
