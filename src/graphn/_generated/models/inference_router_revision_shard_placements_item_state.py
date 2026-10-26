from enum import StrEnum


class InferenceRouterRevisionShardPlacementsItemState(StrEnum):
    ACTIVE = "active"
    ASSIGNED = "assigned"
    DRAINING = "draining"

    def __str__(self) -> str:
        return str(self.value)
