class LLMProvider:
    def __init__(self, url, api_token, model):
        self.url = url
        self.api_token = api_token
        self.model = model