import time
import random
import string
import os
from colorama import init, Fore
init(convert=True)


Key = input ('input key :')

if Key == "0":
    print  ("key is valid")

else:
    print ("key is invalid, relaunch the program and enter a valid key !")


Wallet = input("Wallet: ")


print ("Checking...")

time.sleep (5)

print ("Wallet is valid !!")

time.sleep (0.3)

print ("Ready, press enter ?")
input("")

time.sleep (2)

print ("...")
time.sleep (0.7)
print ("...")
time.sleep (0.7)
print ("...")
time.sleep (0.7)
print ("...")
time.sleep (0.7)

print ("Starting...")

tries = 0

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

while(True):
    if tries <= random.randint(5000, 10000):
        print(Fore.CYAN + "[-]" + Fore.RED + " bc1" + id_gen() + Fore.CYAN + " | InValid |  " + "0.0000 BTC")
        tries += 1
    else:  # chance to get fake btc
        print(Fore.CYAN + "[-]" + Fore.RED + " bc1" + id_gen() + Fore.GREEN + " |  Valid  |  " + str(
            round(random.uniform(0, 2), 4)), "BTC")
        print(Fore.GREEN + "Withdrawing to your Wallet...")
        time.sleep(10)
        tries = 0
        print(Fore.GREEN + "Done!")
        time.sleep(1)
