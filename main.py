import random
import os
import time
from colorama import Fore

// Erstellt denn Banner quasi
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
green = Fore.LIGHTGREEN_EX //Gibt die Farbe magenta an eine Variable
cyan = Fore.CYAN // Das gleiche wie oben nur mit Cyan
top = [] // Zero-Pointer um später dinge rein zu schreiben
print(Fore.LIGHTMAGENTA_EX + banner) // gibt denn banner in der farbe Magenta aus
cho1 = input("Gedanke 1 > ") // Fragt dich nach deinen Gedanken zum entscheiden
cho2 = input("Gedanke 2 > ")
cho3 = input("Gedanke 3 (Enter zum Skippen)> ")
top = [cho1, cho2, cho3] // Schreibt deine entscheidungen in denn oben angegebenen Zero-Ponter welcher hier die Variable "top" hat
print("Entscheidet für dich...")
time.sleep(7)
asw = random.choice(top) // Entscheidet zufällig zwischen denn oben eingegebenen Gedanken
print(f"{green}Deine Entscheidung ist:{cyan} {asw}") // Gibt die antwort aus



