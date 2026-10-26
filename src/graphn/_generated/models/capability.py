from enum import StrEnum


class Capability(StrEnum):
    EMBEDDING = "embedding"
    REASONING = "reasoning"
    TOOL_CALLING = "tool_calling"
    VISION = "vision"

    def __str__(self) -> str:
        return str(self.value)
