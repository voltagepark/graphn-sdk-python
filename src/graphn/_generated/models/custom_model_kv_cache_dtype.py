from enum import StrEnum


class CustomModelKvCacheDtype(StrEnum):
    FP8 = "fp8"

    def __str__(self) -> str:
        return str(self.value)
