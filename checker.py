import requests, os
from colorama import Fore

os.system("cls")

for acc in open("accs.txt","r").read().splitlines():
    api_key=acc.split(":")[2]

    acc = requests.post('https://api.capsolver.com/getBalance',json={
        "clientKey": api_key}).json()

    if acc.get("balance"):
        bal=acc["balance"]
        
        if bal>0:
            print(f"{Fore.LIGHTGREEN_EX}has bal --> {str(bal)}")
            with open("has_bal.txt","a+") as b:
                b.write(api_key+"\n")
        else:
            print(f"{Fore.YELLOW}no balance --> {str(bal)}")
    else:
        print(f"{Fore.RED}invalid --> {api_key}")