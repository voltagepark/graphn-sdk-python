from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.admin_invoice_discount_request_type import AdminInvoiceDiscountRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminInvoiceDiscountRequest")


@_attrs_define
class AdminInvoiceDiscountRequest:
    """
    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        expected_revision (int):
        type_ (AdminInvoiceDiscountRequestType):
        value (int): Discount input value. For percentage discounts this is basis points
            (1..9999 = 0.01%..99.99%). For fixed_amount_cents this is cents.
        reason (str):
        comment (str):
        idempotency_key (str | Unset):
    """

    from_: datetime.datetime
    to: datetime.datetime
    expected_revision: int
    type_: AdminInvoiceDiscountRequestType
    value: int
    reason: str
    comment: str
    idempotency_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        expected_revision = self.expected_revision

        type_ = self.type_.value

        value = self.value

        reason = self.reason

        comment = self.comment

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "to": to,
                "expectedRevision": expected_revision,
                "type": type_,
                "value": value,
                "reason": reason,
                "comment": comment,
            }
        )
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = datetime.datetime.fromisoformat(d.pop("from"))

        to = datetime.datetime.fromisoformat(d.pop("to"))

        expected_revision = d.pop("expectedRevision")

        type_ = AdminInvoiceDiscountRequestType(d.pop("type"))

        value = d.pop("value")

        reason = d.pop("reason")

        comment = d.pop("comment")

        idempotency_key = d.pop("idempotencyKey", UNSET)

        admin_invoice_discount_request = cls(
            from_=from_,
            to=to,
            expected_revision=expected_revision,
            type_=type_,
            value=value,
            reason=reason,
            comment=comment,
            idempotency_key=idempotency_key,
        )

        return admin_invoice_discount_request
