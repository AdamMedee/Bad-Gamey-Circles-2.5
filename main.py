#layout of actual game and things run
from __future__ import print_function
from menu import *
from help import *
from gameA import *
#from gameB import *
from math import *
from random import *


running = True

curScreen = "menu" #menu, help, game, and end


while running:

    if curScreen == "menu":
        curScreen = dispMenu()

    elif curScreen == "help":
        curScreen = dispOptions()

    elif curScreen == "game":
        curScreen = dispGameA() and dispGameB()

    elif curScreen == "end":
        pass

    else:
        running = False


quit()







