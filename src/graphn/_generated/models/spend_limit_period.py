from enum import StrEnum


class SpendLimitPeriod(StrEnum):
    UTC_CALENDAR_DAY = "utc_calendar_day"
    UTC_CALENDAR_MONTH = "utc_calendar_month"
    UTC_CALENDAR_WEEK = "utc_calendar_week"
    UTC_FIVE_MINUTE = "utc_five_minute"
    UTC_HOUR = "utc_hour"

    def __str__(self) -> str:
        return str(self.value)
