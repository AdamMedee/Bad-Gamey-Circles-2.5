#diifferent things that can be summoned

from pygame import *
from math import *
from random import *


class Base:
    def __init__(self, team):
        if team == "A":
            self.x = 20
            self.y = 260
            self.col = (0, 0, 255)
        elif team == "B":
            self.x = 1320
            self.y = 260
            self.col = (255, 0, 0)
        self.rect = (self.x, self.y, 100, 200)
        self.health = 500
        self.maxHealth = 500
        self.healthRect = (self.x + 40, self.y + 20, 20, 160)

    def draw(self, screen):
        draw.rect(screen, self.col, self.rect, 0)
        draw.rect(screen, (0, 255, 0), (self.x + 40, self.y + 20, 20, int(160 * (self.health/self.maxHealth))), 0)
        draw.rect(screen, (50, 100, 50), (self.x + 40, self.y + 20, 20, 160), 4)

    def update(self, screen):
        self.draw(screen)













