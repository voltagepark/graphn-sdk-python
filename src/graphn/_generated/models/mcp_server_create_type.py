from enum import StrEnum


class McpServerCreateType(StrEnum):
    HOSTED = "hosted"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
