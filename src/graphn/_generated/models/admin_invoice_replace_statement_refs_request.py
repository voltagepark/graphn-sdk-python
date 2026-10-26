from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.admin_invoice_statement_ref import AdminInvoiceStatementRef


T = TypeVar("T", bound="AdminInvoiceReplaceStatementRefsRequest")


@_attrs_define
class AdminInvoiceReplaceStatementRefsRequest:
    """
    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        expected_current (list[AdminInvoiceStatementRef]):
        desired (list[AdminInvoiceStatementRef]):
        comment (str):
    """

    from_: datetime.datetime
    to: datetime.datetime
    expected_current: list[AdminInvoiceStatementRef]
    desired: list[AdminInvoiceStatementRef]
    comment: str

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        expected_current = []
        for expected_current_item_data in self.expected_current:
            expected_current_item = expected_current_item_data.to_dict()
            expected_current.append(expected_current_item)

        desired = []
        for desired_item_data in self.desired:
            desired_item = desired_item_data.to_dict()
            desired.append(desired_item)

        comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "to": to,
                "expectedCurrent": expected_current,
                "desired": desired,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_statement_ref import AdminInvoiceStatementRef

        d = dict(src_dict)
        from_ = datetime.datetime.fromisoformat(d.pop("from"))

        to = datetime.datetime.fromisoformat(d.pop("to"))

        expected_current = []
        _expected_current = d.pop("expectedCurrent")
        for expected_current_item_data in _expected_current:
            expected_current_item = AdminInvoiceStatementRef.from_dict(
                expected_current_item_data
            )

            expected_current.append(expected_current_item)

        desired = []
        _desired = d.pop("desired")
        for desired_item_data in _desired:
            desired_item = AdminInvoiceStatementRef.from_dict(desired_item_data)

            desired.append(desired_item)

        comment = d.pop("comment")

        admin_invoice_replace_statement_refs_request = cls(
            from_=from_,
            to=to,
            expected_current=expected_current,
            desired=desired,
            comment=comment,
        )

        return admin_invoice_replace_statement_refs_request
