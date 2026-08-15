from enum import Enum


class InvitationStatus(str, Enum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
