from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.custom_model_access_reason import CustomModelAccessReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModelAccess")


@_attrs_define
class CustomModelAccess:
    """
    Attributes:
        allowed (bool): Whether the workspace may import custom models.
        reason (CustomModelAccessReason | Unset): Why `allowed` is false, when graphn-cp's own gate refused before
            the allowlist was consulted.
        shared_lora (bool | Unset): Preview. Present and `true` when this deployment admits shared
            LoRA bases (`lora_enabled` on create) and adapter attaches.
    """

    allowed: bool
    reason: CustomModelAccessReason | Unset = UNSET
    shared_lora: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        shared_lora = self.shared_lora

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "allowed": allowed,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if shared_lora is not UNSET:
            field_dict["shared_lora"] = shared_lora

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allowed = d.pop("allowed")

        _reason = d.pop("reason", UNSET)
        reason: CustomModelAccessReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = CustomModelAccessReason(_reason)

        shared_lora = d.pop("shared_lora", UNSET)

        custom_model_access = cls(
            allowed=allowed,
            reason=reason,
            shared_lora=shared_lora,
        )

        return custom_model_access
