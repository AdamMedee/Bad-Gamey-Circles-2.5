#main menu screen

from pygame import *
from math import *
from random import *
from systems import *

init()

def drawOpt(screen, r):
    draw.rect(screen, (200, 200, 200), r, 0)
def drawOpt2(screen, r):
    draw.rect(screen, (50, 50, 50), r, 0)

def drawPlay(screen, r):
    pass
def drawPlay2(screen, r):
    pass


def dispMenu():
    #Screen info
    WIDTH, HEIGHT = 1080, 720
    screen = display.set_mode((WIDTH, HEIGHT))
    running = True

    #Buttons
    BOptRect = Rect(440, 500, 200, 140)
    BOptions = Button(BOptRect, drawOpt, drawOpt2, screen)
    BPlayRect = Rect(440, 250, 200, 140)
    BPlay = Button(BPlayRect, drawOpt, drawOpt2, screen)
    bList = [BOptions]


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

        if BOptions.clicked:
            return "help"

        for b in bList:
            b.getClick(mousePos, leftClick)
            b.update()

        display.flip()
    quit()








