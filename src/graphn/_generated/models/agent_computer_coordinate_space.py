from enum import StrEnum


class AgentComputerCoordinateSpace(StrEnum):
    PIXELS = "pixels"
    RELATIVE_1000 = "relative_1000"

    def __str__(self) -> str:
        return str(self.value)
