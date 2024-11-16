from typing import List, Iterable, Dict

import boto3

from src.amazonbedrock.resource import SyncAPIResource
from ...types.chat import ChatCompletion
from ...types.chat.chat_completion import Choice
from ...types.chat.chat_completion_message import ChatCompletionMessage
from ...types.chat.chat_completion_message_param import ChatCompletionMessageParam


def _transform(message: ChatCompletionMessageParam):
    user_message = message
    return {
        "role": user_message["role"],
        "content": [{"text": user_message["content"]}]
    }


class Completions(SyncAPIResource):
    def _converse(
            self,
            model: str,
            messages: List[Dict]
    ) -> ChatCompletion:
        client = boto3.client("bedrock-runtime", region_name="us-east-1")
        response = client.converse(
            modelId=model,
            messages=messages
        )

        responses = response["output"]["message"]["content"]
        choices = []
        for response in responses:
            message = ChatCompletionMessage(content=response.get("text", None))
            choices.append(Choice(message=message))

        return ChatCompletion(choices=choices)

    def create(
            self,
            model: str,
            messages: Iterable[ChatCompletionMessageParam]
    ) -> ChatCompletion:
        transformed_messages = []
        for message in messages:
            transformed_messages.append(_transform(message))

        return self._converse(model, transformed_messages)
