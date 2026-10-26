from enum import StrEnum


class InferenceRouterAnalyticsSharedCandidateRuntimeStatus(StrEnum):
    COMPLETE = "complete"
    DEGRADED = "degraded"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self) -> str:
        return str(self.value)
