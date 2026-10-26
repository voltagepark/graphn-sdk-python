from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_list_billing_statements_response_200_empty_reason import (
    AdminListBillingStatementsResponse200EmptyReason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_statement_summary import BillingStatementSummary


T = TypeVar("T", bound="AdminListBillingStatementsResponse200")


@_attrs_define
class AdminListBillingStatementsResponse200:
    """
    Attributes:
        statements (list[BillingStatementSummary]):
        empty_reason (AdminListBillingStatementsResponse200EmptyReason | Unset):
    """

    statements: list[BillingStatementSummary]
    empty_reason: AdminListBillingStatementsResponse200EmptyReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statements = []
        for statements_item_data in self.statements:
            statements_item = statements_item_data.to_dict()
            statements.append(statements_item)

        empty_reason: str | Unset = UNSET
        if not isinstance(self.empty_reason, Unset):
            empty_reason = self.empty_reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statements": statements,
            }
        )
        if empty_reason is not UNSET:
            field_dict["emptyReason"] = empty_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.billing_statement_summary import BillingStatementSummary

        d = dict(src_dict)
        statements = []
        _statements = d.pop("statements")
        for statements_item_data in _statements:
            statements_item = BillingStatementSummary.from_dict(statements_item_data)

            statements.append(statements_item)

        _empty_reason = d.pop("emptyReason", UNSET)
        empty_reason: AdminListBillingStatementsResponse200EmptyReason | Unset
        if isinstance(_empty_reason, Unset):
            empty_reason = UNSET
        else:
            empty_reason = AdminListBillingStatementsResponse200EmptyReason(
                _empty_reason
            )

        admin_list_billing_statements_response_200 = cls(
            statements=statements,
            empty_reason=empty_reason,
        )

        admin_list_billing_statements_response_200.additional_properties = d
        return admin_list_billing_statements_response_200

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
