import requests

response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
print(response.json())