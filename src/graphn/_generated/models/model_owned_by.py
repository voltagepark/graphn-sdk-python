from enum import StrEnum


class ModelOwnedBy(StrEnum):
    BUILT_IN = "built-in"
    CUSTOM = "custom"
    IMPORTED = "imported"

    def __str__(self) -> str:
        return str(self.value)
