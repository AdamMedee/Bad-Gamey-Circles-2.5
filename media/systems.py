#for buttons and convenience stuff

from pygame import *
from math import *
from random import *

class button:
    def __init__(self, rect, disp1, disp2):
        self.rect = rect
        self.disp1 = disp1
        self.disp2 = disp2
        self.clicked = False
        self.mouseover = False

    def getClick(self, mouse, click):
        self.mouseover = mouse.colliderect(self.rect)
        self.clicked = click and self.mouseover

    def update(self):
        if self.mouseover:
            self.disp1()
        else:
            self.disp2()

