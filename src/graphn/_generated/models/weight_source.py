from enum import Enum


class WeightSource(str, Enum):
    HUGGINGFACE = "huggingface"
    S3_ASSUME_ROLE = "s3_assume_role"
    S3_PRESIGNED = "s3_presigned"

    def __str__(self) -> str:
        return str(self.value)
