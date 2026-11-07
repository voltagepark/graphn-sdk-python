from enum import StrEnum


class SpendLimitEnforcementState(StrEnum):
    ACTIVE = "active"
    DEFERRED_UNTIL_BOUNDARY = "deferred_until_boundary"

    def __str__(self) -> str:
        return str(self.value)
