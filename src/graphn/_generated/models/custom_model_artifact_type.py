from enum import StrEnum


class CustomModelArtifactType(StrEnum):
    BASE = "base"
    LORA = "lora"

    def __str__(self) -> str:
        return str(self.value)
