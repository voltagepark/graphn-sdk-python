from enum import Enum


class OrganizationType(str, Enum):
    PERSONAL = "personal"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
