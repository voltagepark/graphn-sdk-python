from enum import StrEnum


class MemberRole(StrEnum):
    ADMIN = "admin"
    MEMBER = "member"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
