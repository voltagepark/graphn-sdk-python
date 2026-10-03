from enum import StrEnum


class PostObjectType(StrEnum):
    DOWNLOAD = "download"
    UPLOAD = "upload"
    UPLOAD_PART = "upload_part"

    def __str__(self) -> str:
        return str(self.value)
