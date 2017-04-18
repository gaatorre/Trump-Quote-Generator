from tkinter import *
from pip._vendor import requests

# Import the modules
import json
from urllib.request import urlopen

class Trump:
    def add_labels(self, background):
        for x in range(0, 24):
            if (x % 2 != 0):
                Label(background, bg='red').pack(expand=True, fill=X)

            else:
                Label(background, bg='white').pack(expand=True, fill=X)

    def __init__(self, master):
        master.minsize(width=666, height=666)
        self.add_labels(master)

    def trump_quote(self):
        resp = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
        data = resp.json()
        return data['message']



root = Tk()
b = Trump(root)

background = Frame()
background.pack(fill=X)

print(b.trump_quote())

root.mainloop()
