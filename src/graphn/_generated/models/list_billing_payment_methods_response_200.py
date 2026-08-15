from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.payment_method import PaymentMethod


T = TypeVar("T", bound="ListBillingPaymentMethodsResponse200")


@_attrs_define
class ListBillingPaymentMethodsResponse200:
    """
    Attributes:
        payment_methods (list[PaymentMethod]):
    """

    payment_methods: list[PaymentMethod]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_methods = []
        for payment_methods_item_data in self.payment_methods:
            payment_methods_item = payment_methods_item_data.to_dict()
            payment_methods.append(payment_methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentMethods": payment_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.payment_method import PaymentMethod

        d = dict(src_dict)
        payment_methods = []
        _payment_methods = d.pop("paymentMethods")
        for payment_methods_item_data in _payment_methods:
            payment_methods_item = PaymentMethod.from_dict(payment_methods_item_data)

            payment_methods.append(payment_methods_item)

        list_billing_payment_methods_response_200 = cls(
            payment_methods=payment_methods,
        )

        list_billing_payment_methods_response_200.additional_properties = d
        return list_billing_payment_methods_response_200

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
