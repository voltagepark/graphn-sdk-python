from enum import StrEnum


class InferenceRouterLaneCreateMatch(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
