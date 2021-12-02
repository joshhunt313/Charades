import requests
import time
from tkinter import *
from tkinter import messagebox

NUM_WORDS = 10

window = Tk()

window.title("Charades Games")

window.geometry('300x350')

output_label = Label(window, text="List of Words")

output = Text(window, height = 15, 
              width = 25, 
              bg = "light cyan")

timer = StringVar()
timer.set("120")
time_entry = Entry(window, textvariable=timer, width=3)

def run_command():
    output.delete('1.0', END)
    temp = int(timer.get())
    charades_text = ""
    for word in range(NUM_WORDS):
        response = requests.get("https://random-word-form.herokuapp.com/random/noun")
        pointResponse = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1")
        charades_text += response.json()[0] + " " + str(pointResponse.json()[0]) + "\n"
    output.insert(END, charades_text)

    while temp > -1:
        timer.set("{0:3d}".format(temp))
        window.update()
        time.sleep(1)
        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up! Calculate your points earned")
        temp -= 1


run_button = Button(window, text="Run", fg="black", command=run_command)

time_entry.pack()
output_label.pack()
output.pack()
run_button.pack()

window.mainloop()
