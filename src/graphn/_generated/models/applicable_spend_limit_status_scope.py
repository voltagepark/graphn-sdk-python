from enum import StrEnum


class ApplicableSpendLimitStatusScope(StrEnum):
    USER = "user"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
