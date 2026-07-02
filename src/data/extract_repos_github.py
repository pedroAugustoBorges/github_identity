import requests
import base64


print('oi')
USERNAME : str = 'pedroAugustoBorges'
repos = 'first-data-pipeline'

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)

data = response.json()

first = data[0]

name_repository = first['name']
description = first['description']
language = first['language']

print(f"{name_repository} - {description} - {language}")

for k, v in first.items():
    print(f'{k} - {v}')