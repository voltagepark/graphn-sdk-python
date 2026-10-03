from enum import StrEnum


class InferenceRouterAnalyticsInterval(StrEnum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
