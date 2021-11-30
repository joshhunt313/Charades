import requests
import json
import time

NUM_WORDS = 10

numPlayers = input("Numbers of players: ")

for playerNum in range(int(numPlayers)):
    print("Player " + str(playerNum + 1))
    for roundNum in range(NUM_WORDS):
        response = requests.get("https://random-word-form.herokuapp.com/random/noun")
        pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1")
        print(response.json()[0] + " " + str(pointResponse.json()[0]))
    print("***********************************************")
    time.sleep(120)
