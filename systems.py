#for buttons and convenience stuff

from pygame import *
from math import *
from random import *

class Button:
    def __init__(self, rect, disp1, disp2, screen):
        self.rect = rect
        self.disp1 = disp1
        self.disp2 = disp2
        self.clicked = False
        self.mouseover = False
        self.screen = screen

    def getClick(self, mouse, click):
        self.mouseover = self.rect.collidepoint(mouse)
        self.clicked = click and self.mouseover

    def update(self):
        if self.mouseover:
            self.disp1(self.screen, self.rect)
        else:
            self.disp2(self.screen, self.rect)

