#diifferent things that can be summoned

from pygame import *
from math import *
from random import *
from systems import *
from troops import *

WIDTH, HEIGHT = 1080, 720

screen = display.set_mode((WIDTH, HEIGHT))


init()

#button graphics
def drawTRect(screen, r):
    draw.rect(screen, (0, 0, 255), (r[0]+15, r[1]+15, r[2]-30, r[3]-30), 3)
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTRect2(screen, r):
    draw.rect(screen, (0, 0, 255), (r[0]+15, r[1]+15, r[2]-30, r[3]-30), 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTTri(screen, r):
    draw.rect(screen, (0, 0, 255), (r[0]+15, r[1]+15, r[2]-30, r[3]-30), 3)
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTTri2(screen, r):
    draw.rect(screen, (0, 0, 255), (r[0]+15, r[1]+15, r[2]-30, r[3]-30), 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTPent(screen, r):
    draw.rect(screen, (0, 0, 255), (r[0]+15, r[1]+15, r[2]-30, r[3]-30), 3)
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTPent2(screen, r):
    draw.rect(screen, (0, 0, 255), (r[0]+15, r[1]+15, r[2]-30, r[3]-30), 3)
    draw.rect(screen, (200, 200, 200), r, 3)


def dispGameA():
    # Screen info
    WIDTH, HEIGHT = 1080, 720
    screen = display.set_mode((WIDTH, HEIGHT))
    running = True

    #Buttons
    TRectR = Rect(10, 270, 80, 80)
    BRect = Button(TRectR, drawTRect, drawTRect2, screen)
    TTriR = Rect(10, 360, 80, 80)
    BTri = Button(TTriR, drawTTri, drawTTri2, screen)
    TPentR = Rect(10, 450, 80, 80)
    BPent = Button(TPentR, drawTPent, drawTPent2, screen)

    bList = [BRect, BTri, BPent]
    curSelected = None
    curSRect = None

    allyList = []
    enemyList = []

    energy = 20
    maxAmb = 12
    maxEnergy = 20

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

        for b in bList:
            if b.mouseover:
                break
        else:
            if leftClick:
                curSRect = None
                if curSelected is not None and energy >= curSelected.cost:
                    allyList.append(curSelected)
                    energy -= curSelected.cost
                    curSelected = None



        if BRect.clicked:
            curSRect = TRectR
            #curSelected = RectangleT()
        elif BTri.clicked:
            curSRect = TTriR
        elif BPent.clicked:
            curSRect = TPentR

        screen.fill((0, 0, 0))
        if curSRect is not None:
            draw.rect(screen, (0, 200, 0), curSRect, 5)
        for b in bList:
            b.getClick(mousePos, leftClick)
            b.update()
        draw.rect(screen, (255, 255, 255), (1040, -10, 50, 1200), 3)
        for c in range(energy):
            draw.circle(screen, (150, 55, 250), (1060, 700 - 35*c), 15, 4)

        display.flip()
    quit()