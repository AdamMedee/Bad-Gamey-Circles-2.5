#diifferent things that can be summoned

from pygame import *
from math import *
from random import *
from systems import *
from troops import *

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Bad Gamey Circles 25-9664c3ab308c.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Bad Gamey Circle 2.5").sheet1
nGames=int(sheet.cell(1,1).value)                    #Number of games that are currently running
nGames+=1
sheet.update_cell(1,1,str(nGames))                 #Update the numnber of games that are currently playing




WIDTH, HEIGHT = 1080, 720

screen = display.set_mode((WIDTH, HEIGHT))


init()
font.init()
f = font.SysFont("consolas", 60, True)
one = f.render("1", True, (255, 0, 0))
two = f.render("2", True, (255, 0, 0))
three = f.render("3", True, (255, 0, 0))
four = f.render("4", True, (255, 0, 0))
five = f.render("5", True, (255, 0, 0))
six = f.render("6", True, (255, 0, 0))
seven = f.render("7", True, (255, 0, 0))
eight = f.render("8", True, (255, 0, 0))
nine = f.render("9", True, (255, 0, 0))
ten = f.render("10", True, (255, 0, 0))
eleven = f.render("11", True, (255, 0, 0))
twelve = f.render("12", True, (255, 0, 0))
thirteen = f.render("13", True, (255, 0, 0))
fourteen = f.render("14", True, (255, 0, 0))
fifteen = f.render("15", True, (255, 0, 0))
sixteen = f.render("16", True, (255, 0, 0))
seventeen = f.render("17", True,(255, 0, 0))
eighteen = f.render("18", True, (255, 0, 0))
nineteen = f.render("19", True, (255, 0, 0))
twenty = f.render("20", True, (255, 0, 0))

#button graphics
def drawTRect(screen, r):
    screen.blit(five, (r[0]+20, r[1]+10))
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTRect2(screen, r):
    draw.rect(screen, (255, 0, 0), (r[0]+15, r[1]+25, r[2]-30, r[3]-50), 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTTri2(screen, r):
    draw.polygon(screen, (255, 0, 0), [(r[0] + r[2]//2, r[1]+10), (r[0]+10, r[1]+65), (r[0]+70, r[1]+65)], 3)
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTTri(screen, r):
    screen.blit(two, (r[0]+25, r[1]+15))
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTSquare(screen, r):
    screen.blit(three, (r[0] + 25, r[1] + 15))
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTSquare2(screen, r):
    draw.rect(screen, (255, 0, 0), (r[0] + 15, r[1] + 15, r[2] - 30, r[3] - 30), 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTHex(screen, r):
    screen.blit(twelve, (r[0]+10, r[1]+15))
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTHex2(screen, r):
    draw.polygon(screen, (255, 0, 0), [(r[0] + 20, r[1] + 5), (r[0] + 60, r[1] + 5), (r[0] + 75, r[1] + 40), (r[0] + 60, r[1] + 75), (r[0] + 20, r[1] + 75), (r[0] + 5, r[1] + 40)], 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTCircle(screen, r):
    screen.blit(ten, (r[0] + 5, r[1] + 10))
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTCircle2(screen, r):
    draw.circle(screen, (255, 0, 0), (r[0] + 40, r[1] + 40), 30, 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def drawTSpin(screen, r):
    screen.blit(eight, (r[0] + 25, r[1] + 15))
    draw.rect(screen, (150, 150, 150), r, 3)
def drawTSpin2(screen, r):
    draw.polygon(screen, (255, 0, 0), [(r[0] + 5, r[1] + 40), (r[0]+30, r[1] + 30),
                    (r[0] + 40, r[1] + 5), (r[0] + 50, r[1]+30),
                    (r[0] + 75, r[1] + 40), (r[0]+50, r[1] + 50),
                    (r[0] +40, r[1] + 75), (r[0] + 30, r[1]+50)], 3)
    draw.rect(screen, (200, 200, 200), r, 3)

def dispGameB():
    global nGames
    # Screen info
    WIDTH, HEIGHT = 1440, 720
    screen = display.set_mode((WIDTH, HEIGHT))
    running = True

    #Buttons
    TRectR = Rect(10, 10, 80, 80)
    BRect = Button(TRectR, drawTRect, drawTRect2, screen)
    TTriR = Rect(100, 10, 80, 80)
    BTri = Button(TTriR, drawTTri, drawTTri2, screen)
    TSquareR = Rect(190, 10, 80, 80)
    BSquare = Button(TSquareR, drawTSquare, drawTSquare2, screen)
    THexR = Rect(280, 10, 80, 80)
    BHex = Button(THexR, drawTHex, drawTHex2, screen)
    TSpinR = Rect(370, 10, 80, 80)
    BSpin = Button(TSpinR, drawTSpin, drawTSpin2, screen)
    TCircleR = Rect(460, 10, 80, 80)
    BCircle = Button(TCircleR, drawTCircle, drawTCircle2, screen)




    bList = [BRect, BTri, BSquare, BHex, BCircle, BSpin]
    curSelected = None
    curSRect = None

    allyList = [Base("B")]
    enemyList = [Base("A"), TTriangle(300, 200, "A")]

    energy = 12
    maxAmb = 12
    maxEnergy = 20

    emptyField = True #Whether any enemies are on your side of the field

    FPS = 60
    clock = time.Clock()
    nextEng = 100
    while running:
        leftClick, middleClick, rightClick = False, False, False
        scroll = 0
        mousePos = mouse.get_pos()
        for action in event.get():
            if action.type == QUIT:
                running = False
                nGames -=1
                sheet.update_cell(1, 1, str(nGames))
                break
            elif action.type == MOUSEBUTTONDOWN:
                if action.button == 1:
                    leftClick = True

        #"buying" troops
        if not any([b.mouseover for b in bList]):
            if leftClick:
                curSRect = None
                if curSelected is not None and mousePos[0] > 720 and energy >= curSelected(0, 0, "B").cost:
                    curSelected = curSelected(mousePos[0], mousePos[1], "B")
                    allyList.append(curSelected)
                    energy -= curSelected.cost
                    curSelected = None

        # ACCESS SPREADSHEET IN SOMEWAY TO FIND IF ENEMY SUMMONED TROOPS
        # ALSO PUT OWN TROOPS INTO SHEET FOR ENEMY TO ACCESS
        # AT THIS SPOT

        emptyField = not any(enemy.x > 720 for enemy in enemyList)

        #Delete dead enemies
        # Update energy
        if energy < maxAmb and nextEng <= 0:
            nextEng = 100
            energy += 1
        elif energy < maxAmb:
            nextEng -= 1

        for i in range(len(allyList)-1, -1, -1):
            if allyList[i].hp <= 0:
                del allyList[i]
        for i in range(len(enemyList)-1, -1, -1):
            if enemyList[i].hp <= 0:
                del enemyList[i]







        #Updates which troop is currently selected
        if BRect.clicked:
            curSRect = TRectR
            curSelected = TRectangle
        elif BTri.clicked:
            curSRect = TTriR
            curSelected = TTriangle
        elif BSquare.clicked:
            curSRect = TSquareR
            curSelected = TSquare
        elif BHex.clicked:
            curSRect = THexR
            curSelected = THexagon
        elif BCircle.clicked:
            curSRect = TCircleR
            curSelected = TCircle
        elif BSpin.clicked:
            curSRect = TSpinR
            curSelected = TSpinner

        #This is where all graphics are displayed and run
        screen.fill((0, 0, 0))
        draw.rect(screen, (0, 255, 0), (700, 0, 40, 200), 0)
        draw.rect(screen, (0, 255, 0), (700, 280, 40, 180), 0)
        draw.rect(screen, (0, 255, 0), (700, 520, 40, 220), 0)

        for a in allyList:
            a.update(screen, emptyField, enemyList)
        for e in enemyList:
            e.update(screen, emptyField, allyList)
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