from enum import Enum


class ModelObject(str, Enum):
    MODEL = "model"

    def __str__(self) -> str:
        return str(self.value)
