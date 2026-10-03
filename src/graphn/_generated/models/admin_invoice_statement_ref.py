from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AdminInvoiceStatementRef")


@_attrs_define
class AdminInvoiceStatementRef:
    """
    Attributes:
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        revision (int):
        input_fingerprint (str):
    """

    period_start: datetime.datetime
    period_end: datetime.datetime
    revision: int
    input_fingerprint: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        revision = self.revision

        input_fingerprint = self.input_fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodStart": period_start,
                "periodEnd": period_end,
                "revision": revision,
                "inputFingerprint": input_fingerprint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        revision = d.pop("revision")

        input_fingerprint = d.pop("inputFingerprint")

        admin_invoice_statement_ref = cls(
            period_start=period_start,
            period_end=period_end,
            revision=revision,
            input_fingerprint=input_fingerprint,
        )

        admin_invoice_statement_ref.additional_properties = d
        return admin_invoice_statement_ref

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
