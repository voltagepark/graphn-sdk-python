from enum import StrEnum


class InferenceRouterCreatePreset(StrEnum):
    BALANCED = "balanced"

    def __str__(self) -> str:
        return str(self.value)
