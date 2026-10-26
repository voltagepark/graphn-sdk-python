from enum import StrEnum


class InvitationScopeType(StrEnum):
    ORG = "org"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
