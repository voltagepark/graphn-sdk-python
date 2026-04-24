from enum import Enum


class Capability(str, Enum):
    EMBEDDING = "embedding"
    REASONING = "reasoning"
    TOOL_CALLING = "tool_calling"
    VISION = "vision"

    def __str__(self) -> str:
        return str(self.value)
