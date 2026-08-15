from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.list_billing_invoices_response_200_empty_reason import (
    ListBillingInvoicesResponse200EmptyReason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice import Invoice


T = TypeVar("T", bound="ListBillingInvoicesResponse200")


@_attrs_define
class ListBillingInvoicesResponse200:
    """
    Attributes:
        invoices (list[Invoice]):
        empty_reason (ListBillingInvoicesResponse200EmptyReason | Unset):
    """

    invoices: list[Invoice]
    empty_reason: ListBillingInvoicesResponse200EmptyReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)

        empty_reason: str | Unset = UNSET
        if not isinstance(self.empty_reason, Unset):
            empty_reason = self.empty_reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoices": invoices,
            }
        )
        if empty_reason is not UNSET:
            field_dict["emptyReason"] = empty_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.invoice import Invoice

        d = dict(src_dict)
        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in _invoices:
            invoices_item = Invoice.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        _empty_reason = d.pop("emptyReason", UNSET)
        empty_reason: ListBillingInvoicesResponse200EmptyReason | Unset
        if isinstance(_empty_reason, Unset):
            empty_reason = UNSET
        else:
            empty_reason = ListBillingInvoicesResponse200EmptyReason(_empty_reason)

        list_billing_invoices_response_200 = cls(
            invoices=invoices,
            empty_reason=empty_reason,
        )

        list_billing_invoices_response_200.additional_properties = d
        return list_billing_invoices_response_200

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
