from enum import StrEnum


class ValidateModelResponseArtifactType(StrEnum):
    BASE = "base"
    LORA = "lora"

    def __str__(self) -> str:
        return str(self.value)
