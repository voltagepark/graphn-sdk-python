from enum import StrEnum


class ConnectionKind(StrEnum):
    MCP = "mcp"
    NATIVE = "native"

    def __str__(self) -> str:
        return str(self.value)
