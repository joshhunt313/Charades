import requests
import json
import time

NUM_WORDS = 10

numPlayers = input("Numbers of players: ")

for playerNum in range(int(numPlayers)):
    print("Player " + str(playerNum + 1))
    for roundNum in range(NUM_WORDS):
        response = requests.get("https://random-word-form.herokuapp.com/random/noun")
        pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=1")
        print(response.json()[0] + " " + str(pointResponse.json()[0]))
    
    time.sleep(120)

