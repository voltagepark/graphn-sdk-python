from enum import Enum


class TTSRequestResponseFormat(str, Enum):
    FLAC = "flac"
    MP3 = "mp3"
    OPUS = "opus"
    PCM = "pcm"
    WAV = "wav"

    def __str__(self) -> str:
        return str(self.value)
