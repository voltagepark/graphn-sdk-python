from enum import Enum


class InvitationRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
