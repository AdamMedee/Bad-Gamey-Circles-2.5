#diifferent things that can be summoned

from pygame import *
from math import *
from random import *
from systems import *
from troops import *

WIDTH, HEIGHT = 1440, 720

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
    WIDTH, HEIGHT = 1440, 720
    screen = display.set_mode((WIDTH, HEIGHT))
    running = True

    #Buttons
    TRectR = Rect(270, 10, 80, 80)
    BRect = Button(TRectR, drawTRect, drawTRect2, screen)
    TTriR = Rect(360, 10, 80, 80)
    BTri = Button(TTriR, drawTTri, drawTTri2, screen)
    TPentR = Rect(450, 10, 80, 80)
    BPent = Button(TPentR, drawTPent, drawTPent2, screen)

    bList = [BRect, BTri, BPent]
    curSelected = None
    curSRect = None

    allyList = [Base("A")]
    enemyList = [Base("B")]

    energy = 20
    maxAmb = 12
    maxEnergy = 20

    emptyField = True #Whether any enemies are on your side of the field

    FPS = 60
    clock = time.Clock()

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

        #"buying" troops
        if not any([b.mouseover for b in bList]):
            if leftClick:
                curSRect = None
                if curSelected is not None and mousePos[0] < 720 and energy >= curSelected.cost:
                    allyList.append(curSelected)
                    energy -= curSelected.cost
                    curSelected = None

        emptyField = not any(enemy.y < 720 for enemy in enemyList)

        #ACCESS SPREADSHEET IN SOMEWAY TO FIND IF ENEMY SUMMONED TROOPS
        #ALSO PUT OWN TROOPS INTO SHEET FOR ENEMY TO ACCESS
        #AT THIS SPOT



        #Updates which troop is currently selected
        if BRect.clicked:
            curSRect = TRectR
            #curSelected = RectangleT()
        elif BTri.clicked:
            curSRect = TTriR
            #curSelected = RectangleT()
        elif BPent.clicked:
            curSRect = TPentR
            #curSelected = RectangleT()

        #This is where all graphics are displayed and run
        screen.fill((0, 0, 0))
        for a in allyList:
            a.draw(screen)
        for e in enemyList:
            e.draw(screen)
        if curSRect is not None:
            draw.rect(screen, (0, 200, 0), curSRect, 5)
        for b in bList:
            b.getClick(mousePos, leftClick)
            b.update()
        draw.rect(screen, (255, 255, 255), (-10, 670, 840, 80), 3)
        for c in range(energy):
            draw.circle(screen, (150, 55, 250), (30 + 40*c, 700), 15, 4)

        display.flip()
        clock.tick(FPS)

    quit()