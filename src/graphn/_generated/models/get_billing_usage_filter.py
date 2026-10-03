from enum import StrEnum


class GetBillingUsageFilter(StrEnum):
    ONE_DAY = "ONE_DAY"
    ONE_YEAR = "ONE_YEAR"
    SEVEN_DAY = "SEVEN_DAY"
    THIRTY_DAY = "THIRTY_DAY"

    def __str__(self) -> str:
        return str(self.value)
