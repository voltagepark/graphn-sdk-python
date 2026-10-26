from enum import StrEnum


class CustomModelAccessReason(StrEnum):
    ADMIN_DISABLED = "admin_disabled"
    PURCHASE_REQUIRED = "purchase_required"

    def __str__(self) -> str:
        return str(self.value)
