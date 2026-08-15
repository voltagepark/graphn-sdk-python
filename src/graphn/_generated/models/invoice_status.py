from enum import Enum


class InvoiceStatus(str, Enum):
    CLOSED = "closed"
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
