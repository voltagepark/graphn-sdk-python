from enum import StrEnum


class PublishedRouterRevisionState(StrEnum):
    ACTIVE = "active"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
