import requests, random
import colorama
from colorama import Fore
from colorama import Fore, 
colorama.init()


with open("tokens.txt") as x:
    for d in x:
        tokens = d.strip("\n")
        r = requests.get("https://discord.com/api/v9/users/@me/library", headers={"Authorization": tokens})
        if r.status_code == 200:
            print(Fore.GREEN + "{}".format(d.strip("\n")))

# Shitty code lmao
