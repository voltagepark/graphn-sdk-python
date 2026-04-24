"""Chat resource module.

Inference is delegated to the official ``openai`` Python SDK; see
:mod:`graphn.chat.completions`.
"""

from graphn.chat.completions import AsyncChat, Chat

__all__ = ["AsyncChat", "Chat"]
