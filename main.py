from providers.base import LLMProvider
import requests
import json
import os

API_TOKEN = os.getenv('API_TOKEN')

llm = LLMProvider("https://openrouter.ai/api/v1/chat/completions", API_TOKEN, "openai/gpt-oss-120b")

headers = {"Authorization" : f"Bearer {llm.api_token}",
           "Content-Type" : "application/json"}


print(headers)
data = json.dumps( {
    "model" : f"{llm.model}",
    "messages" : [
        {
            "role" : "user",
            "content" : "Quem ganhou o premio nobel em 1943?"
        }
    ]
})

response = requests.post(url = llm.url, headers=headers, data = data)

response = response.json()

response = response['choices'][0]['message']

print(response)
