from ping3 import *
from colorama import *
import ctypes
from colorama import init, Fore, Back, Style
import colorama
from os import system, name
from sys import *
import sys

def clear():
    if name == 'nt':
        _ = system('cls')

def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

clear()

ctypes.windll.kernel32.SetConsoleTitleW("DEMON PING ; VERSION 1.2 ; STATUS: IDLE")

init(convert=True)
init()
colorama.init()

def pinger():
    pings = 0
    for i in range (9999999):
        ping(Target)
        pings += 1
        ctypes.windll.kernel32.SetConsoleTitleW("DEMON PING ; VERSION 1.2 ; STATUS: RUNNING ; PINGS: " + str(pings))

time.sleep(0.02)
print(Fore.LIGHTRED_EX + "   ,    ,    /\   /\          ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "  /( /\ )\  _\ \_/ /_         ")    
time.sleep(0.02)          
print(Fore.LIGHTRED_EX + "  |\_||_/| < \_   _/ >        ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "  \______/  \|0   0|/         ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "    _\/_   _(_  ^  _)_        ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "   ( () ) /`\|V'""V|/`\       ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "     {}   \  \_____/  /       ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "     ()   /\   )=(   /\       ")
time.sleep(0.02)
print(Fore.LIGHTRED_EX + "     {}  /  \_/\=/\_/  \      ")
time.sleep(0.02)

print(Fore.WHITE + "\n[" + Fore.LIGHTRED_EX + "DEMONPING" + Fore.WHITE + "] SELECT TARGET.")
print(Fore.WHITE + "╔══[user" + Fore.LIGHTRED_EX + "@" + Fore.WHITE + "DEMONPING]")
print(Fore.LIGHTRED_EX + "╚═" + Fore.WHITE + "═════" + Fore.LIGHTRED_EX + "> " , end='')
Target = input()
print(Fore.WHITE + "\n[" + Fore.LIGHTRED_EX + "DEMONPING" + Fore.WHITE + "] START NOW? y/n")
print(Fore.WHITE + "╔══[user" + Fore.LIGHTRED_EX + "@" + Fore.WHITE + "DEMONPING]")
print(Fore.LIGHTRED_EX + "╚═" + Fore.WHITE + "═════" + Fore.LIGHTRED_EX + "> " , end='')
Start = input()
if Start == ("y"):
    running = Fore.WHITE + "\n[" + Fore.LIGHTRED_EX + "DEMONPING" + Fore.WHITE + "] RUNNING.\n"
    for char in running:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    titlecheck = Fore.WHITE + "[" + Fore.LIGHTRED_EX + "DEMONPING" + Fore.WHITE + "] CHECK TITLE BAR FOR INFO."
    for char in titlecheck:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    pinger()
elif Start == ("n"):
    print("Closing...")
    exit()
else:
    print("Wrong answer. Closing...")
    exit()

