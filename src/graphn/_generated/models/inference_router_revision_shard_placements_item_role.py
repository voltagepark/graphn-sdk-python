from enum import StrEnum


class InferenceRouterRevisionShardPlacementsItemRole(StrEnum):
    MIGRATING = "migrating"
    PRIMARY = "primary"

    def __str__(self) -> str:
        return str(self.value)
