from enum import StrEnum


class AdminInvoiceReplaceStatementRefsResponseDisposition(StrEnum):
    UNCHANGED = "unchanged"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
