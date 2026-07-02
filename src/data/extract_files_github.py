import requests
import base64

USERNAME : str = 'pedroAugustoBorges'
repos = 'first-data-pipeline'

url = f"https://api.github.com/repos/{USERNAME}/{repos}/contents/src/db/connection.py?ref=master"

response = requests.get(url)

files = response.json()

content = base64.b64decode(
    files['content']
).decode('utf-8')


print(content)