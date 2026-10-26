from enum import StrEnum


class ConnectionCreateKind(StrEnum):
    MCP = "mcp"
    NATIVE = "native"

    def __str__(self) -> str:
        return str(self.value)
