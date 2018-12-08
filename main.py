#layout of actual game and things run
from __future__ import print_function
from menu import *
from math import *
from random import *
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

running = True

curScreen = "menu" #menu, help, game, and end


while running:

    if curScreen == "menu":
        dispMenu()

    elif curScreen == "help":
        pass

    elif curScreen == "game":
        pass

    elif curScreen == "end":
        pass

    else:
        print("???")

    display.flip()
quit()







