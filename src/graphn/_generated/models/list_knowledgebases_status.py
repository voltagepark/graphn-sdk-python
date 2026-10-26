from enum import StrEnum


class ListKnowledgebasesStatus(StrEnum):
    ACTIVE = "active"
    ERROR = "error"
    INDEXING = "indexing"

    def __str__(self) -> str:
        return str(self.value)
