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

def _create_completion_from(raw_response: Dict, model: str) -> ChatCompletion:
    responses = raw_response["output"]["message"]["content"]
    choices = []
    for response in responses:
        message = ChatCompletionMessage(content=response.get("text", None))
        choices.append(Choice(message=message))

    return ChatCompletion(
        choices=choices,
        model=model
    )


class Completions(SyncAPIResource):
    def _converse(
            self,
            model: str,
            messages: List[Dict]
    ) -> Dict:
        client = boto3.client("bedrock-runtime", region_name=self._region)
        response = client.converse(
            modelId=model,
            messages=messages
        )

        return response

    def create(
            self,
            model: str,
            messages: Iterable[ChatCompletionMessageParam]
    ) -> ChatCompletion:

        model_id = self._client.models.retrieve(model)

        transformed_messages = []
        for message in messages:
            transformed_messages.append(_transform(message))

        raw_response = self._converse(model_id, transformed_messages)

        return _create_completion_from(
            raw_response=raw_response,
            model=model_id
        )
