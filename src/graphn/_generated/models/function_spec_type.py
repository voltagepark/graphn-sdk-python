from enum import StrEnum


class FunctionSpecType(StrEnum):
    BUILTIN = "builtin"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
