import requests
import json
import time
from tkinter import *

NUM_WORDS = 10

window = Tk()

window.title("Charades Games")

window.geometry('300x300')

output_label = Label(window, text="List of Words")
# num_players_label = Label(window, text="Number of Players")
# num_players_label.grid(row=0, column=0, sticky=W, pady=2, padx=2)

# num_players_entry = Entry(window)
# num_players_entry.grid(row=0, column=1, pady=2)

output = Text(window, height = 15, 
              width = 25, 
              bg = "light cyan")

def run_command():
    charades_text = ""
    # run_button.configure(text="Running", fg="red")
    for word in range(NUM_WORDS):
        response = requests.get("https://random-word-form.herokuapp.com/random/noun")
        pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1")
        charades_text += response.json()[0] + " " + str(pointResponse.json()[0]) + "\n"
    output.insert(END, charades_text)

run_button = Button(window, text="Run", fg="black", command=run_command,)
# run_button.grid(column=2, row=1)

# num_players_label.pack()
# num_players_entry.pack()
output_label.pack()
output.pack()
run_button.pack()

window.mainloop()


# NUM_WORDS = 10

# numPlayers = input("Numbers of players: ")

# for playerNum in range(int(numPlayers)):
#     print("Player " + str(playerNum + 1))
#     for roundNum in range(NUM_WORDS):
#         response = requests.get("https://random-word-form.herokuapp.com/random/noun")
#         pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1")
#         print(response.json()[0] + " " + str(pointResponse.json()[0]))
#     print("***********************************************")
#     time.sleep(120)
