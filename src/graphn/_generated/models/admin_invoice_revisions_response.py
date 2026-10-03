from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.admin_invoice_revision import AdminInvoiceRevision


T = TypeVar("T", bound="AdminInvoiceRevisionsResponse")


@_attrs_define
class AdminInvoiceRevisionsResponse:
    """
    Attributes:
        org_id (str):
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        revisions (list[AdminInvoiceRevision]):
    """

    org_id: str
    period_start: datetime.datetime
    period_end: datetime.datetime
    revisions: list[AdminInvoiceRevision]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "periodStart": period_start,
                "periodEnd": period_end,
                "revisions": revisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_revision import (
            AdminInvoiceRevision,
        )

        d = dict(src_dict)
        org_id = d.pop("orgId")

        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        revisions = []
        _revisions = d.pop("revisions")
        for revisions_item_data in _revisions:
            revisions_item = AdminInvoiceRevision.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        admin_invoice_revisions_response = cls(
            org_id=org_id,
            period_start=period_start,
            period_end=period_end,
            revisions=revisions,
        )

        admin_invoice_revisions_response.additional_properties = d
        return admin_invoice_revisions_response

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
