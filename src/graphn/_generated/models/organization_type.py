from enum import StrEnum


class OrganizationType(StrEnum):
    PERSONAL = "personal"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
