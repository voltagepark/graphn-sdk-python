from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.invoice import Invoice


T = TypeVar("T", bound="AdminInvoiceResponse")


@_attrs_define
class AdminInvoiceResponse:
    """
    Attributes:
        invoice (Invoice):
    """

    invoice: Invoice
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice = self.invoice.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice": invoice,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.invoice import Invoice

        d = dict(src_dict)
        invoice = Invoice.from_dict(d.pop("invoice"))

        admin_invoice_response = cls(
            invoice=invoice,
        )

        admin_invoice_response.additional_properties = d
        return admin_invoice_response

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
