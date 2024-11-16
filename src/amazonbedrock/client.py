import boto3

from src.amazonbedrock import resources


class Bedrock:
    chat: resources.Chat

    def __init__(self, region: str = "us-east-1"):
        self.chat = resources.Chat(self, region)
        self._region = region

    def find_model(self, model):
        client = boto3.client("bedrock", region_name=self._region)

        models = client.list_foundation_models(
            byInferenceType="ON_DEMAND"
        )["modelSummaries"]

        model_ids = [model_details["modelId"] for model_details in models if model in model_details["modelId"]]

        if len(model_ids) == 0:
            raise ValueError(f"Model '{model}' can't be found.")
        elif len(model_ids) == 1:
            return model_ids[0]
        else:
            return max(model_ids)
