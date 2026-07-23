import requests
import base64


def extract_data_repositories(user : str):
    data = []
    url = f"https://api.github.com/users/{user}/repos"
    
    response = requests.get(url)    
    datas_repo = response.json()
    
    for value in datas_repo:
        name = value['name']
        desc = value['description']
        lang = value['language']
        data.append([name, desc, lang])
    
    return data

