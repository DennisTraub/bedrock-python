from typing import Union

from typing_extensions import Literal, Required, TypedDict


class ChatCompletionUserMessageParam(TypedDict):
    role: Required[Literal["user"]]
    content: Required[Union[str]]
