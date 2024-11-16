from pydantic import BaseModel
from typing import List

from .chat_completion_message import ChatCompletionMessage


class Choice(BaseModel):
    message: ChatCompletionMessage


class ChatCompletion(BaseModel):
    choices: List[Choice]
