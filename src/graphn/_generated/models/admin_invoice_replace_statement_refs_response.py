from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_invoice_replace_statement_refs_response_disposition import (
    AdminInvoiceReplaceStatementRefsResponseDisposition,
)

if TYPE_CHECKING:
    from ..models.admin_invoice_statement_ref import AdminInvoiceStatementRef


T = TypeVar("T", bound="AdminInvoiceReplaceStatementRefsResponse")


@_attrs_define
class AdminInvoiceReplaceStatementRefsResponse:
    """
    Attributes:
        current (list[AdminInvoiceStatementRef]):
        updated (list[AdminInvoiceStatementRef]):
        disposition (AdminInvoiceReplaceStatementRefsResponseDisposition):
    """

    current: list[AdminInvoiceStatementRef]
    updated: list[AdminInvoiceStatementRef]
    disposition: AdminInvoiceReplaceStatementRefsResponseDisposition
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = []
        for current_item_data in self.current:
            current_item = current_item_data.to_dict()
            current.append(current_item)

        updated = []
        for updated_item_data in self.updated:
            updated_item = updated_item_data.to_dict()
            updated.append(updated_item)

        disposition = self.disposition.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "updated": updated,
                "disposition": disposition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_statement_ref import AdminInvoiceStatementRef

        d = dict(src_dict)
        current = []
        _current = d.pop("current")
        for current_item_data in _current:
            current_item = AdminInvoiceStatementRef.from_dict(current_item_data)

            current.append(current_item)

        updated = []
        _updated = d.pop("updated")
        for updated_item_data in _updated:
            updated_item = AdminInvoiceStatementRef.from_dict(updated_item_data)

            updated.append(updated_item)

        disposition = AdminInvoiceReplaceStatementRefsResponseDisposition(
            d.pop("disposition")
        )

        admin_invoice_replace_statement_refs_response = cls(
            current=current,
            updated=updated,
            disposition=disposition,
        )

        admin_invoice_replace_statement_refs_response.additional_properties = d
        return admin_invoice_replace_statement_refs_response

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
