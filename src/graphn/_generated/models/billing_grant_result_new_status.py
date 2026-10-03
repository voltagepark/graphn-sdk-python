from enum import StrEnum


class BillingGrantResultNewStatus(StrEnum):
    LOW = "low"
    OK = "ok"
    OUT_OF_BALANCE = "out_of_balance"

    def __str__(self) -> str:
        return str(self.value)
