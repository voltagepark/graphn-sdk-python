from enum import Enum


class InvitationScopeType(str, Enum):
    ORG = "org"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
