from enum import Enum


class CustomModelArtifactType(str, Enum):
    BASE = "base"
    LORA = "lora"

    def __str__(self) -> str:
        return str(self.value)
