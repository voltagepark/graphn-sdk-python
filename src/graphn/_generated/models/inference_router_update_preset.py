from enum import StrEnum


class InferenceRouterUpdatePreset(StrEnum):
    BALANCED = "balanced"

    def __str__(self) -> str:
        return str(self.value)
