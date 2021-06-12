import random, string
import time
import requests
import os


def clearterminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Fore:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


clearterminal()
print(Fore.YELLOW + """
███╗   ██╗██╗████████╗██████╗  ██████╗ 
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝\n""")
num = input(Fore.BLUE + 'Amount of Nitro codes to generate: ')
clearterminal()
f = open("codes.txt", "w", encoding='utf-8')
for n in range(int(num)):
    y = ''.join(
        random.choice(string.ascii_uppercase + string.digits +
        string.ascii_lowercase) for _ in range(24))
    f.write(y)
    f.write("\n")

f.close()

with open("codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")
        url = f"https://discordapp.com/api/v8/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        r = requests.get(url)
        time.sleep(5)
        if r.status_code == 404:
            print(Fore.RED + f"Invalid > https://discord.gift/{nitro}")
        elif r.status_code == 429:
            print(Fore.CYAN + f"Ratelimited > https://discord.gift/{nitro}")
            time.sleep(30)
            requests.get(url)
            print(Fore.RED + f"Invalid > https://discord.gift/{nitro}")
        else:
            print(Fore.GREEN + f"Valid > https://discord.gift/{nitro}")
