from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Bedrock


class SyncAPIResource:
    _client: Bedrock

    def __init__(self, client: Bedrock):
        self._client = client
        self._region = client.region
