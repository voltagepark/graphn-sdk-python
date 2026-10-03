from enum import StrEnum


class InferenceRouterLaneMatch(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
