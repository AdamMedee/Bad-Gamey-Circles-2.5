#layout of actual game and things run

from pygame import *
from math import *
from random import *

init()

WIDTH, HEIGHT = 1080, 720

screen = display.set_mode((WIDTH, HEIGHT))

running = True

leftClick, middleClick, rightClick = False, False, False
scroll = 0
mousePos = (0, 0)
menu = "menu" #menu, help, game, and end


while running:
    leftClick, middleClick, rightClick = False, False, False
    scroll = 0
    for action in event.get():
        if action.type == QUIT:
            running = False
            break

    if menu == "menu":
        pass

    elif menu == "help":
        pass

    elif menu == "game":
        pass

    elif menu == "end":
        pass

    else:
        print("???")

    display.flip()
quit()







