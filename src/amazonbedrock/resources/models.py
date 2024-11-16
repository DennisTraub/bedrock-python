from functools import cached_property
from typing import List, Dict

from src.amazonbedrock.resource import SyncAPIResource


class Models(SyncAPIResource):
    def retrieve(self, model: str) -> str:
        models = self.list

        model_ids = [model_details["modelId"] for model_details in models if model in model_details["modelId"]]

        if len(model_ids) == 0:
            raise ValueError(f"Model '{model}' can't be found.")
        elif len(model_ids) == 1:
            return model_ids[0]
        else:
            return max(model_ids)

    @cached_property
    def list(self, active: bool = True, on_demand: bool = True) -> List[Dict]:
        kwargs = {"byInferenceType": "ON_DEMAND"} if on_demand else {}

        models = self._client.raw_bedrock_client.list_foundation_models(**kwargs)["modelSummaries"]

        return [model for model in models if not active or "ACTIVE" == model["modelLifecycle"]["status"]]
