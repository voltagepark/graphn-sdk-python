from enum import Enum


class GetBillingUsageFilter(str, Enum):
    ONE_DAY = "ONE_DAY"
    ONE_YEAR = "ONE_YEAR"
    SEVEN_DAY = "SEVEN_DAY"
    THIRTY_DAY = "THIRTY_DAY"

    def __str__(self) -> str:
        return str(self.value)
