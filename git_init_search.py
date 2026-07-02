import requests

USERNAME : str = 'pedroAugustoBorges'

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)

data = response.json()


oi = [1, 2]
cie = [1, 0]
print("structure: ")


for k, v in zip(data[0].keys(), data[0].values()):
    print(f'{k} : {v}')

