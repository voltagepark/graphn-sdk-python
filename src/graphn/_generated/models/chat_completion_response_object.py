from enum import StrEnum


class ChatCompletionResponseObject(StrEnum):
    CHAT_COMPLETION = "chat.completion"

    def __str__(self) -> str:
        return str(self.value)
