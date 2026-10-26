from enum import StrEnum


class InferenceRouterConfigPreset(StrEnum):
    BALANCED = "balanced"

    def __str__(self) -> str:
        return str(self.value)
