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
    BOptRect = Rect(440, 490, 220, 145)
    BOptions = Button(BOptRect, drawOpt, drawOpt2, screen)
    BPlayRect = Rect(440, 240, 220, 140)
    BPlay = Button(BPlayRect, drawOpt, drawOpt2, screen)
    bList = [BOptions, BPlay]
    
    playPic = image.load("play.png")
    helpPic = image.load("help.png")
    titlePic = image.load("title.png")
    s1 = image.load("1.png")
    s2 = image.load("2.png")
    s3 = image.load("3.png")
    s4 = image.load("4.png")

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
        elif BPlay.clicked:
            return "game"

        for b in bList:
            b.getClick(mousePos, leftClick)
            b.update()
        screen.blit(playPic,(450,240))
        screen.blit(helpPic,(450,490))
        screen.blit(titlePic,(10,10))
        
        screen.blit(s2,(0,400))
        screen.blit(s1,(50,100))
        
        screen.blit(s3,(700,100))
        screen.blit(s4,(700,400))
        
        display.flip()
    quit()








