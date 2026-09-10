from enum import StrEnum


class CustomModelStatus(StrEnum):
    DELETING = "deleting"
    DEPLOYING = "deploying"
    FAILED = "failed"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
