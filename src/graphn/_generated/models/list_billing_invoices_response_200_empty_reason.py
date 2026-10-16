from enum import StrEnum


class ListBillingInvoicesResponse200EmptyReason(StrEnum):
    NO_BILLING_HISTORY = "no_billing_history"
    STATEMENTS_NOT_GENERATED_YET = "statements_not_generated_yet"

    def __str__(self) -> str:
        return str(self.value)
