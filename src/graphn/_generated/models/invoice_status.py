from enum import StrEnum


class InvoiceStatus(StrEnum):
    CLOSED = "closed"
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
