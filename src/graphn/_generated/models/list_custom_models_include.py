from enum import StrEnum


class ListCustomModelsInclude(StrEnum):
    ADAPTERS = "adapters"

    def __str__(self) -> str:
        return str(self.value)
