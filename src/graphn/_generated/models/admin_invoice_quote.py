from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.admin_invoice_quote_line_item import AdminInvoiceQuoteLineItem


T = TypeVar("T", bound="AdminInvoiceQuote")


@_attrs_define
class AdminInvoiceQuote:
    """
    Attributes:
        org_id (str):
        customer_id (str):
        period (str):
        amount_cents (int):
        line_items (list[AdminInvoiceQuoteLineItem]):
    """

    org_id: str
    customer_id: str
    period: str
    amount_cents: int
    line_items: list[AdminInvoiceQuoteLineItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        customer_id = self.customer_id

        period = self.period

        amount_cents = self.amount_cents

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "customerId": customer_id,
                "period": period,
                "amountCents": amount_cents,
                "lineItems": line_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_quote_line_item import (
            AdminInvoiceQuoteLineItem,
        )

        d = dict(src_dict)
        org_id = d.pop("orgId")

        customer_id = d.pop("customerId")

        period = d.pop("period")

        amount_cents = d.pop("amountCents")

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = AdminInvoiceQuoteLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        admin_invoice_quote = cls(
            org_id=org_id,
            customer_id=customer_id,
            period=period,
            amount_cents=amount_cents,
            line_items=line_items,
        )

        admin_invoice_quote.additional_properties = d
        return admin_invoice_quote

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
