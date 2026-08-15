from enum import Enum


class OrganizationCreateType(str, Enum):
    PERSONAL = "personal"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
