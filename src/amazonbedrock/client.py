from src.amazonbedrock import resources


class Bedrock:
    chat: resources.Chat

    def __init__(self):
        self.chat = resources.Chat(self)
