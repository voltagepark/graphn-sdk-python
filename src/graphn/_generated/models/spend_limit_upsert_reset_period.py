from enum import StrEnum


class SpendLimitUpsertResetPeriod(StrEnum):
    DAY = "day"
    FIVE_MINUTE = "five_minute"
    HOUR = "hour"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
