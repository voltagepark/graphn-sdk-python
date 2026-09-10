from enum import StrEnum


class OrganizationCreateType(StrEnum):
    PERSONAL = "personal"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
