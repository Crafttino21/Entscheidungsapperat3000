import random
import os
import time
from colorama import Fore

banner = '''

██╗    ██╗███████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗██╗     
██║    ██║██╔════╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     
██║ █╗ ██║█████╗  █████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗███████║██╔██╗ ██║██║  ███╗█████╗  ██║     
██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     
╚███╔███╔╝███████╗███████╗██║     ██║██║ ╚████║╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                                   
        * Zufalls generator | Nimmt dir deine Entscheidungen ab lol *
    Amino hat mich auf die idee Gebracht also joa | GitHub: https://github.com/Crafttino21


'''
green = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
top = []
print(Fore.LIGHTMAGENTA_EX + banner)
cho1 = input("Gedanke 1 > ")
cho2 = input("Gedanke 2 > ")
cho3 = input("Gedanke 3 (Enter zum Skippen)> ")
top = [cho1, cho2, cho3]
print("Entscheidet für dich...")
time.sleep(7)
asw = random.choice(top)
print(f"{green}Deine Entscheidung ist:{cyan} {asw}")



