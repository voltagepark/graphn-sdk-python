from enum import StrEnum


class SpendLimitScope(StrEnum):
    USER = "user"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
