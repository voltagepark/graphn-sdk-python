from enum import StrEnum


class ValidateModelRequestWeightSource(StrEnum):
    HUGGINGFACE = "huggingface"
    S3_ASSUME_ROLE = "s3_assume_role"

    def __str__(self) -> str:
        return str(self.value)
