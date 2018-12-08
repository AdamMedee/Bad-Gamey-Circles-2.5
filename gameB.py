#diifferent things that can be summoned

from pygame import *
from math import *
from random import *
from systems import *

WIDTH, HEIGHT = 1080, 720

screen = display.set_mode((WIDTH, HEIGHT))


init()


def drawBack(screen, r):
    draw.rect(screen, (200, 200, 200), r, 0)


def drawBack2(screen, r):
    draw.rect(screen, (50, 50, 50), r, 0)




def dispGameB():
    # Screen info
    WIDTH, HEIGHT = 1080, 720
    screen = display.set_mode((WIDTH, HEIGHT))
    running = True

    # Buttons
    BRect = Rect(50, 50, 100, 75)
    BBack = Button(BRect, drawBack, drawBack2, screen)
    bList = [BBack]

    #Game actuall starts
    while running:
        leftClick, middleClick, rightClick = False, False, False
        scroll = 0
        mousePos = mouse.get_pos()
        for action in event.get():
            if action.type == QUIT:
                running = False
                break
            elif action.type == MOUSEBUTTONDOWN:
                if action.button == 1:
                    leftClick = True

        #Event loop finished, check if button was pressed to end file
        if BBack.clicked:
            return "menu"

        #update stuff
        for b in bList:
            b.getClick(mousePos, leftClick)
            b.update()

        display.flip()

    quit()