from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.admin_invoice_quote import AdminInvoiceQuote
    from ..models.admin_invoice_statement_ref import AdminInvoiceStatementRef


T = TypeVar("T", bound="AdminInvoicePreviewResponse")


@_attrs_define
class AdminInvoicePreviewResponse:
    """
    Attributes:
        period_start (datetime.datetime):
        period_end (datetime.datetime):
        statement_refs (list[AdminInvoiceStatementRef]):
        manifest_sha_256 (str):
        quote (AdminInvoiceQuote):
    """

    period_start: datetime.datetime
    period_end: datetime.datetime
    statement_refs: list[AdminInvoiceStatementRef]
    manifest_sha_256: str
    quote: AdminInvoiceQuote
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        statement_refs = []
        for statement_refs_item_data in self.statement_refs:
            statement_refs_item = statement_refs_item_data.to_dict()
            statement_refs.append(statement_refs_item)

        manifest_sha_256 = self.manifest_sha_256

        quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periodStart": period_start,
                "periodEnd": period_end,
                "statementRefs": statement_refs,
                "manifestSha256": manifest_sha_256,
                "quote": quote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_quote import AdminInvoiceQuote
        from ..models.admin_invoice_statement_ref import (
            AdminInvoiceStatementRef,
        )

        d = dict(src_dict)
        period_start = datetime.datetime.fromisoformat(d.pop("periodStart"))

        period_end = datetime.datetime.fromisoformat(d.pop("periodEnd"))

        statement_refs = []
        _statement_refs = d.pop("statementRefs")
        for statement_refs_item_data in _statement_refs:
            statement_refs_item = AdminInvoiceStatementRef.from_dict(
                statement_refs_item_data
            )

            statement_refs.append(statement_refs_item)

        manifest_sha_256 = d.pop("manifestSha256")

        quote = AdminInvoiceQuote.from_dict(d.pop("quote"))

        admin_invoice_preview_response = cls(
            period_start=period_start,
            period_end=period_end,
            statement_refs=statement_refs,
            manifest_sha_256=manifest_sha_256,
            quote=quote,
        )

        admin_invoice_preview_response.additional_properties = d
        return admin_invoice_preview_response

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
