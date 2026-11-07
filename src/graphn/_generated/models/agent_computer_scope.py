from enum import StrEnum


class AgentComputerScope(StrEnum):
    EXECUTION = "execution"
    STEP = "step"

    def __str__(self) -> str:
        return str(self.value)
