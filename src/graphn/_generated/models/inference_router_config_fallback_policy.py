from enum import StrEnum


class InferenceRouterConfigFallbackPolicy(StrEnum):
    DEGRADED_GENERAL = "degraded_general"
    FAIL_CLOSED = "fail_closed"

    def __str__(self) -> str:
        return str(self.value)
