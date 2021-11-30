import requests
import json
import time

NUM_ROUNDS = 10

numPlayers = input("Numbers of players: ")

for roundNum in range(10):
    response = requests.get("https://random-word-form.herokuapp.com/random/noun")
    pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1")
    print(response.json()[0] + " " + str(pointResponse.json()[0]))

