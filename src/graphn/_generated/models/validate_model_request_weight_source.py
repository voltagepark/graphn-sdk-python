from enum import Enum


class ValidateModelRequestWeightSource(str, Enum):
    HUGGINGFACE = "huggingface"
    S3_ASSUME_ROLE = "s3_assume_role"

    def __str__(self) -> str:
        return str(self.value)
