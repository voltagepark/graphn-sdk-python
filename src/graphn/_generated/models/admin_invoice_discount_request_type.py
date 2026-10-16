from enum import StrEnum


class AdminInvoiceDiscountRequestType(StrEnum):
    FIXED_AMOUNT_CENTS = "fixed_amount_cents"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
