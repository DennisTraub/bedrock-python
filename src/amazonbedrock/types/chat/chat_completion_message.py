from typing import Optional

from pydantic import BaseModel


class ChatCompletionMessage(BaseModel):
    content: Optional[str] = None
