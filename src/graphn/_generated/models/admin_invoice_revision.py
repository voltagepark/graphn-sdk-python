from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_invoice_discount import AdminInvoiceDiscount


T = TypeVar("T", bound="AdminInvoiceRevision")


@_attrs_define
class AdminInvoiceRevision:
    """
    Attributes:
        revision (int):
        invoice_id (str):
        status (str):
        root_invoice_id (str):
        original_amount_cents (int):
        adjusted_amount_cents (int):
        created_at (datetime.datetime):
        supersedes_invoice_id (str | Unset):
        status_updated_at (datetime.datetime | Unset):
        discount (AdminInvoiceDiscount | Unset):
    """

    revision: int
    invoice_id: str
    status: str
    root_invoice_id: str
    original_amount_cents: int
    adjusted_amount_cents: int
    created_at: datetime.datetime
    supersedes_invoice_id: str | Unset = UNSET
    status_updated_at: datetime.datetime | Unset = UNSET
    discount: AdminInvoiceDiscount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision = self.revision

        invoice_id = self.invoice_id

        status = self.status

        root_invoice_id = self.root_invoice_id

        original_amount_cents = self.original_amount_cents

        adjusted_amount_cents = self.adjusted_amount_cents

        created_at = self.created_at.isoformat()

        supersedes_invoice_id = self.supersedes_invoice_id

        status_updated_at: str | Unset = UNSET
        if not isinstance(self.status_updated_at, Unset):
            status_updated_at = self.status_updated_at.isoformat()

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision": revision,
                "invoiceId": invoice_id,
                "status": status,
                "rootInvoiceId": root_invoice_id,
                "originalAmountCents": original_amount_cents,
                "adjustedAmountCents": adjusted_amount_cents,
                "createdAt": created_at,
            }
        )
        if supersedes_invoice_id is not UNSET:
            field_dict["supersedesInvoiceId"] = supersedes_invoice_id
        if status_updated_at is not UNSET:
            field_dict["statusUpdatedAt"] = status_updated_at
        if discount is not UNSET:
            field_dict["discount"] = discount

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.admin_invoice_discount import (
            AdminInvoiceDiscount,
        )

        d = dict(src_dict)
        revision = d.pop("revision")

        invoice_id = d.pop("invoiceId")

        status = d.pop("status")

        root_invoice_id = d.pop("rootInvoiceId")

        original_amount_cents = d.pop("originalAmountCents")

        adjusted_amount_cents = d.pop("adjustedAmountCents")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        supersedes_invoice_id = d.pop("supersedesInvoiceId", UNSET)

        _status_updated_at = d.pop("statusUpdatedAt", UNSET)
        status_updated_at: datetime.datetime | Unset
        if isinstance(_status_updated_at, Unset):
            status_updated_at = UNSET
        else:
            status_updated_at = datetime.datetime.fromisoformat(_status_updated_at)

        _discount = d.pop("discount", UNSET)
        discount: AdminInvoiceDiscount | Unset
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = AdminInvoiceDiscount.from_dict(_discount)

        admin_invoice_revision = cls(
            revision=revision,
            invoice_id=invoice_id,
            status=status,
            root_invoice_id=root_invoice_id,
            original_amount_cents=original_amount_cents,
            adjusted_amount_cents=adjusted_amount_cents,
            created_at=created_at,
            supersedes_invoice_id=supersedes_invoice_id,
            status_updated_at=status_updated_at,
            discount=discount,
        )

        admin_invoice_revision.additional_properties = d
        return admin_invoice_revision

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
