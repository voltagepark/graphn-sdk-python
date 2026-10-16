from enum import StrEnum


class ListKnowledgebasesSort(StrEnum):
    CREATED_AT = "created_at"

    def __str__(self) -> str:
        return str(self.value)
