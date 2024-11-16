from src.amazonbedrock import Bedrock

from pprint import pprint

client = Bedrock(region="us-west-2")

print("\n----- listing models -----")
on_demand_models = client.models.list

print("\n----- retrieving a model -----")
haiku = client.models.retrieve("anthropic.claude-3-haiku-20240307-v1:0")
pprint(haiku)

sonnet_3_5 = client.models.retrieve("claude-3-5-sonnet")
pprint(sonnet_3_5)

print("\n----- standard request with model ID -----")
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
print(completion.model)

print("\n----- standard request with model name -----")
completion = client.chat.completions.create(
    model="mistral-large-2407",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)
print(completion.model)