from typing import Union

from typing_extensions import TypeAlias
from .chat_completion_user_message_param import ChatCompletionUserMessageParam

ChatCompletionMessageParam: TypeAlias = Union[
    ChatCompletionUserMessageParam
]
