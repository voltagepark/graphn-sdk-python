from enum import StrEnum


class IntegrationAuthMode(StrEnum):
    OAUTH2 = "oauth2"

    def __str__(self) -> str:
        return str(self.value)
