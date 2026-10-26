from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.billing_statement_detail import BillingStatementDetail


T = TypeVar("T", bound="GetBillingStatementResponse200")


@_attrs_define
class GetBillingStatementResponse200:
    """
    Attributes:
        statement (BillingStatementDetail):
    """

    statement: BillingStatementDetail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statement = self.statement.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statement": statement,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.billing_statement_detail import BillingStatementDetail

        d = dict(src_dict)
        statement = BillingStatementDetail.from_dict(d.pop("statement"))

        get_billing_statement_response_200 = cls(
            statement=statement,
        )

        get_billing_statement_response_200.additional_properties = d
        return get_billing_statement_response_200

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
