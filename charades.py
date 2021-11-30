import requests
import json
import time

NUM_ROUNDS = 10;

for roundNum in range(10):
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1")
    print(response.json()[0] + " " + str(pointResponse.json()[0]))
    time.sleep(60)
