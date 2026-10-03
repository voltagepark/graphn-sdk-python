from enum import StrEnum


class InvoiceStatus(StrEnum):
    CLOSED = "closed"
    CURRENT = "current"
    FAILED = "failed"
    MISMATCH = "mismatch"
    OPEN = "open"
    PAID = "paid"
    RESERVED = "reserved"
    STALE = "stale"
    VOID = "void"
    VOIDING = "voiding"

    def __str__(self) -> str:
        return str(self.value)
