from enum import StrEnum


class ModelObject(StrEnum):
    MODEL = "model"

    def __str__(self) -> str:
        return str(self.value)
