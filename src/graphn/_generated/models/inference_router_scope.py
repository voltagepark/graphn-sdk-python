from enum import StrEnum


class InferenceRouterScope(StrEnum):
    PLATFORM = "platform"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
