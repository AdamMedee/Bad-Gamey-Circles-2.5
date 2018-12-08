#layout of actual game and things run
from __future__ import print_function
from menu import *
from help import *
from math import *
from random import *
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

running = True

curScreen = "menu" #menu, help, game, and end


while running:

    if curScreen == "menu":
        curScreen = dispMenu()

    elif curScreen == "help":
        curScreen = dispOptions()

    elif curScreen == "game":
        pass

    elif curScreen == "end":
        pass

    else:
        running = False


quit()







