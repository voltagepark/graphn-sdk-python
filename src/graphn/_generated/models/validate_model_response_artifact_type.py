from enum import Enum


class ValidateModelResponseArtifactType(str, Enum):
    BASE = "base"
    LORA = "lora"

    def __str__(self) -> str:
        return str(self.value)
