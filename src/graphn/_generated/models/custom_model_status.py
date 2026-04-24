from enum import Enum


class CustomModelStatus(str, Enum):
    DELETING = "deleting"
    DEPLOYING = "deploying"
    FAILED = "failed"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
