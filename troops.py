# diifferent things that can be summoned

from pygame import *
from math import *
from random import *


class Triangle:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 5
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.invinc = 100
        self.cost = 2
        self.speed = 5
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (0, 0, 255),
                     [(self.x - 25, self.y + 25), (self.x + 25, self.y + 25), (self.x, self.y - 25)])

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Square:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 10
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.invinc = 0
        self.cost = 3
        self.speed = 4
        self.team = team

    def draw(self, screen):
        draw.rect(screen, (0, 255, 0), self.rect)

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, enemyList):
        pass


class TRectangle:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 100
        self.rect = Rect(x - 50, y - 25, 100, 50)
        self.cooldown = 0
        self.invinc = 0
        self.cost = 5
        self.team = team

    def draw(self, screen):
        draw.rect(screen, (255, 0, 0), self.rect)

    def update(self, screen):
        pass


class Hexagon:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 50
        self.rect = Rect(x - 50, y - 50, 100, 100)
        self.cooldown = 0
        self.invinc = 0
        self.cost = 15
        self.speed = 1
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (255, 255, 255),
                     [(self.x - 25, self.y - 50), (self.x + 25, self.y - 50), (self.x + 50, self.y),
                      (self.x + 25, self.y + 50), (self.x - 25, self.y + 50), (self.x - 50, self.y)])

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, enemyList):
        pass


class Circle:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 5
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.invinc = 100
        self.cost = 15
        self.speed = 6
        self.team = team

    def draw(self, screen):
        draw.circle(screen, (100, 100, 100), (self.x, self.y), 25)

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Plus:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 5
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.invinc = 100
        self.cost = 10
        self.speed = 8
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (100, 35, 200),
                     [(self.x - 8, self.y - 25), (self.x + 8, self.y - 25), (self.x + 8, self.y - 8),
                      (self.x + 25, self.y - 8), (self.x + 25, self.y + 8), (self.x + 8, self.y + 8),
                      (self.x + 8, self.y + 25), (self.x - 8, self.y + 25), (self.x - 8, self.y + 8),
                      (self.x - 25, self.y + 8), (self.x - 25, self.y - 8), (self.x - 8, self.y - 8)])

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def heal(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Kite:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 5
        self.rect = Rect(x - 25, y - 75, 50, 100)
        self.cooldown = 0
        self.invinc = 100
        self.cost = 18
        self.speed = 4
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (50, 200, 150),
                     [(self.x - 25, self.y), (self.x, self.y - 75), (self.x + 25, self.y), (self.x, self.y + 25)])

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Spinner:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 6
        self.rect = Rect(x - 30, y - 30, 60, 60)
        self.cooldown = 0
        self.invinc = 100
        self.cost = 6
        self.speed = 14
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (0, 0, 255), [(self.x - 10, self.y - 10), (self.x, self.y - 50),
                                           (self.x + 10, self.y - 10), (self.x + 50, self.y),
                                           (self.x + 10, self.y + 10), (self.x, self.y + 50),
                                           (self.x - 10, self.y + 10), (self.x - 50, self.y)])

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Pentagon:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x - 50, y - 50, 100, 100)
        self.duration = 100
        self.cost = 12
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (0, 0, 255), [(self.x - 50, self.y), (self.x, self.y - 50),
                                           (self.x + 50, self.y), (self.x + 25, self.y + 50), (self.x - 25, self.y + 50)])

    def effect(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Line:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x, y-50, 1, 100)
        self.cost = 3
        self.speed = 8
        self.team = team

    def draw(self, screen):
        draw.line(screen, (200, 50, 200), (self.x, self.y - 50), (self.x, self.y + 50))

    def move(self):
        self.x += self.speed

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class Star:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x - 50, y - 50, 100, 100)
        self.duration = 100
        self.cost = 8
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (0, 0, 255), [(self.x, self.y - 38), (self.x + 13, self.y - 13),
                                           (self.x + 38, self.y - 13), (self.x + 23, self.y + 13),
                                           (self.x + 29, self.y + 38), (self.x, self.y + 23),
                                           (self.x - 29, self.y + 38), (self.x - 23, self.y + 13),
                                           (self.x - 38, self.y - 13), (self.x - 13, self.y - 13)])

    def effect(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class House:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x - 50, y - 100, 100, 150)
        self.cost = 18
        self.team = team

    def draw(self, screen):
        draw.polygon(screen, (0, 0, 255), [(self.x - 50, self.y - 50), (self.x, self.y - 100),
                                           (self.x + 50, self.y - 50), (self.x + 50, self.y + 50),
                                           (self.x - 50, self.y + 50)])

    def effect(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)

class base:
    def __init__(self, team):
        if team == "A":
            self.x = 440
            self.y = 600
            self.col = (0, 0, 255)
        elif team == "B":
            self.x = 440
            self.y = 20
            self.col = (255, 0, 0)
        self.rect = (self.x, self.y, 200, 100)
        self.health = 500
        self.maxHealth = 500
        self.healthRect = (self.x + 20, self.y + 40, 160, 20)

    def draw(self, screen):
        draw.rect(screen, self.col, self.rect, 0)
        draw.rect(screen, (0, 255, 0), (self.x + 20, self.y + 40, int(160 * (self.health / self.maxHealth)), 20), 0)
        draw.rect(screen, (50, 100, 50), (self.x + 20, self.y + 40, 160, 20), 0)

    def update(self, screen):
        self.draw(screen)













