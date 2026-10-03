from enum import StrEnum


class ConnectionStatus(StrEnum):
    ACTIVE = "active"
    ERROR = "error"
    NEEDS_REAUTH = "needs_reauth"
    PENDING = "pending"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
