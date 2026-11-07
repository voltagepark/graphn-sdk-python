from enum import StrEnum


class OrganizationCreatedType(StrEnum):
    PERSONAL = "personal"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
