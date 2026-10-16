from enum import StrEnum


class InferenceRouterStatus(StrEnum):
    ACTIVE = "active"
    DELETED = "deleted"
    DELETING = "deleting"
    DRAFT = "draft"
    FAILED = "failed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
