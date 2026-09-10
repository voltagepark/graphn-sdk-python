from enum import StrEnum


class McpServerSpecType(StrEnum):
    HOSTED = "hosted"
    MANAGED = "managed"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
