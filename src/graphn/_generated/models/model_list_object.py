from enum import StrEnum


class ModelListObject(StrEnum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
