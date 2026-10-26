from enum import IntEnum


class CustomModelCreateMaxLoraRank(IntEnum):
    VALUE_16 = 16
    VALUE_64 = 64

    def __str__(self) -> str:
        return str(self.value)
