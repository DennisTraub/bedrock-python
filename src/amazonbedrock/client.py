import boto3

from src.amazonbedrock import resources


class Bedrock:
    chat: resources.Chat
    models: resources.Models
    region: str

    def __init__(self, region: str = "us-east-1"):
        self.region = region
        self.raw_bedrock_client = boto3.client("bedrock", region_name=region)

        self.chat = resources.Chat(self)
        self.models = resources.Models(self)
