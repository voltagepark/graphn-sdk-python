from enum import StrEnum


class InvitationStatus(StrEnum):
    ACCEPTED = "accepted"
    DECLINED = "declined"
    EXPIRED = "expired"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
