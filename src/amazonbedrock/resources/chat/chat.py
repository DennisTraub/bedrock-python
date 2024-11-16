from functools import cached_property

from ...resource import SyncAPIResource
from .completions import Completions


class Chat(SyncAPIResource):
    @cached_property
    def completions(self) -> Completions:
        return Completions(self._client, self._region)
