from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AdminInvoiceCreateRequest")


@_attrs_define
class AdminInvoiceCreateRequest:
    """
    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        manifest_sha_256 (str):
        comment (str):
    """

    from_: datetime.datetime
    to: datetime.datetime
    manifest_sha_256: str
    comment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        manifest_sha_256 = self.manifest_sha_256

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "manifestSha256": manifest_sha_256,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        from_ = datetime.datetime.fromisoformat(d.pop("from"))

        to = datetime.datetime.fromisoformat(d.pop("to"))

        manifest_sha_256 = d.pop("manifestSha256")

        comment = d.pop("comment")

        admin_invoice_create_request = cls(
            from_=from_,
            to=to,
            manifest_sha_256=manifest_sha_256,
            comment=comment,
        )

        admin_invoice_create_request.additional_properties = d
        return admin_invoice_create_request

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
