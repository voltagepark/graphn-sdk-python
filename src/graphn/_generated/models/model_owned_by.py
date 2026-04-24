from enum import Enum


class ModelOwnedBy(str, Enum):
    BUILT_IN = "built-in"
    CUSTOM = "custom"
    IMPORTED = "imported"

    def __str__(self) -> str:
        return str(self.value)
