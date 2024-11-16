from typing import assert_type

from src.amazonbedrock import Bedrock
from src.amazonbedrock.types.chat import ChatCompletion


class TestBedrockClient:

    def test_create(self):
        client = Bedrock()
        completion = client.chat.completions.create(
            model="anthropic.claude-3-haiku-20240307-v1:0",
            messages=[
                {
                    "role": "user",
                    "content": "Hello, how are you?"
                }
            ]
        )
        assert_type(completion, ChatCompletion)
        choice = completion.choices[0]
        assert choice.message is not None
