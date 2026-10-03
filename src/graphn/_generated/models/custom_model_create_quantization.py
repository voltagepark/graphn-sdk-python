from enum import StrEnum


class CustomModelCreateQuantization(StrEnum):
    AWQ = "awq"
    FP8 = "fp8"
    GGUF = "gguf"
    GPTQ = "gptq"
    MARLIN = "marlin"
    SQUEEZELLM = "squeezellm"

    def __str__(self) -> str:
        return str(self.value)
