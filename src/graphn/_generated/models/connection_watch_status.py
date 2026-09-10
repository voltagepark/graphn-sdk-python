from enum import StrEnum


class ConnectionWatchStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
