from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminInvoiceRecordPaymentResponse")


@_attrs_define
class AdminInvoiceRecordPaymentResponse:
    """
    Attributes:
        org_id (str):
        invoice_id (str):
        idempotency_key (str):
        already_recorded (bool):
        journal_sequence (int):
        projection_status (str):
        balance_projection_pending (bool):
    """

    org_id: str
    invoice_id: str
    idempotency_key: str
    already_recorded: bool
    journal_sequence: int
    projection_status: str
    balance_projection_pending: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        invoice_id = self.invoice_id

        idempotency_key = self.idempotency_key

        already_recorded = self.already_recorded

        journal_sequence = self.journal_sequence

        projection_status = self.projection_status

        balance_projection_pending = self.balance_projection_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orgId": org_id,
                "invoiceId": invoice_id,
                "idempotencyKey": idempotency_key,
                "alreadyRecorded": already_recorded,
                "journalSequence": journal_sequence,
                "projectionStatus": projection_status,
                "balanceProjectionPending": balance_projection_pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        invoice_id = d.pop("invoiceId")

        idempotency_key = d.pop("idempotencyKey")

        already_recorded = d.pop("alreadyRecorded")

        journal_sequence = d.pop("journalSequence")

        projection_status = d.pop("projectionStatus")

        balance_projection_pending = d.pop("balanceProjectionPending")

        admin_invoice_record_payment_response = cls(
            org_id=org_id,
            invoice_id=invoice_id,
            idempotency_key=idempotency_key,
            already_recorded=already_recorded,
            journal_sequence=journal_sequence,
            projection_status=projection_status,
            balance_projection_pending=balance_projection_pending,
        )

        admin_invoice_record_payment_response.additional_properties = d
        return admin_invoice_record_payment_response

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
