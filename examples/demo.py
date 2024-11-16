from src.amazonbedrock import Bedrock

client = Bedrock()

completion = client.chat.completions.create(
    model="anthropic.claude-3-haiku-20240307-v1:0",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)
