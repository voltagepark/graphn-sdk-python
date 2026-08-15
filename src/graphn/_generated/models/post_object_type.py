from enum import Enum


class PostObjectType(str, Enum):
    DOWNLOAD = "download"
    UPLOAD = "upload"
    UPLOAD_PART = "upload_part"

    def __str__(self) -> str:
        return str(self.value)
