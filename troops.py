# diifferent things that can be summoned

from pygame import *
from math import *
from random import *


class TTriangle:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 10
        self.maxhp = 10
        self.dmg = 4
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.maxCooldown = 100
        self.invinc = []
        self.bulls = []
        self.cost = 2
        self.speed = 4
        self.team = team
        self.range = 200
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, col, [(self.x - 25, self.y + 25), (self.x + 25, self.y + 25), (self.x, self.y - 25)],0)
        draw.polygon(screen, self.col, [(self.x - 25, self.y + 25), (self.x + 25, self.y + 25), (self.x, self.y - 25)], 4)


    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)
        self.rect = Rect(self.x - 25, self.y - 25, 50, 50)

    def attack(self, target):
        if self.cooldown <= 0:
            dx = target.x - self.x
            dy = target.y - self.y
            ang = atan2(dy, dx)
            self.bulls.append([self.x, self.y, 6*cos(ang), 6*sin(ang), 120])
            self.cooldown = self.maxCooldown

    def update(self, screen, empty, enemyList):
        self.cooldown = max(0, self.cooldown-1)
        tx, ty = 0, 0
        m = 999999
        target = None
        for b in range(len(self.bulls) - 1, -1, -1):
            self.bulls[b][0] += self.bulls[b][2]
            self.bulls[b][1] += self.bulls[b][3]
            self.bulls[b][4] -= 1
            draw.circle(screen, self.col, (int(self.bulls[b][0]), int(self.bulls[b][1])), 4, 0)
            if not Rect(0, 0, 1440, 720).collidepoint(self.bulls[b][0], self.bulls[b][1]) or self.bulls[b][4] <= 0:
                del self.bulls[b]
        for enemy in enemyList:
            for b in range(len(self.bulls)-1, -1, -1):
                if hypot(self.bulls[b][0]-enemy.x, self.bulls[b][1]-enemy.y) < 4:
                    del self.bulls[b]
                    enemy.hp -= self.dmg
            if hypot(enemy.x - self.x, enemy.y - self.y) < m:
                m = hypot(enemy.x - self.x, enemy.y - self.y)
                tx, ty = (enemy.x, enemy.y)
                if hypot(enemy.x - self.x, enemy.y - self.y) < self.range:
                    target = enemy
        if target is not None:
            self.attack(target)
        if empty:
            if self.team == "A" and self.x < 700:
                if self.y > 360:
                    tx, ty = 705, 480
                else:
                    tx, ty = 705, 240
        if target is None:
            self.move(tx, ty)
        self.draw(screen)


class TSquare:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 15
        self.maxhp = 15
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.maxCooldown = 120
        self.dmg = 6
        self.invinc = 0
        self.cost = 3
        self.speed = 3
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.rect(screen, col, self.rect, 0)
        draw.rect(screen, self.col, self.rect, 3)

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)
        self.rect = Rect(self.x - 25, self.y - 25, 50, 50)

    def attack(self, target):
        if self.cooldown <= 0:
            target.hp -= self.dmg
            self.cooldown = self.maxCooldown

    def update(self, screen, empty, enemyList):
        tx, ty = 0, 0
        m = 999999
        self.cooldown = max(0, self.cooldown - 1)
        target = None
        for enemy in enemyList:
            if hypot(enemy.x - self.x, enemy.y - self.y) < m:
                m = hypot(enemy.x - self.x, enemy.y - self.y)
                tx, ty = (enemy.x, enemy.y)
                if enemy.rect.colliderect(self.rect):
                    target = enemy
        if target is not None:
            self.attack(target)
        if empty:
            if self.team == "A" and self.x < 700:
                if self.y > 360:
                    tx, ty = 705, 480
                else:
                    tx, ty = 705, 240
            elif self.team == "B" and self.x > 740:
                if self.y > 360:
                    tx, ty = 735, 480
                else:
                    tx, ty = 735, 240

        if target is None:
            self.move(tx, ty)
        self.draw(screen)

class TRectangle:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 70
        self.rect = Rect(x - 50, y - 25, 50, 100)
        self.cooldown = 0
        self.invinc = 0
        self.cost = 5
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        draw.rect(screen, self.col, self.rect, 3)

    def update(self, screen, empty, enemyList):
        self.draw(screen)


class THexagon:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 40
        self.rect = Rect(x - 50, y - 50, 100, 100)
        self.cooldown = 0
        self.maxCooldown = 200
        self.dmg = 75
        self.invinc = 0
        self.cost = 10
        self.range = 250
        self.speed = 1
        self.team = team
        self.bulls = []
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, col,
                     [(self.x - 25, self.y - 50), (self.x + 25, self.y - 50), (self.x + 50, self.y),
                      (self.x + 25, self.y + 50), (self.x - 25, self.y + 50), (self.x - 50, self.y)], 0)
        draw.polygon(screen, self.col,
                     [(self.x - 25, self.y - 50), (self.x + 25, self.y - 50), (self.x + 50, self.y),
                      (self.x + 25, self.y + 50), (self.x - 25, self.y + 50), (self.x - 50, self.y)], 3)

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        self.speed = self.cooldown/300
        if self.cooldown <= 0:
            dx = target.x - self.x
            dy = target.y - self.y
            ang = atan2(dy, dx)
            self.bulls.append([self.x+5*sin(ang), self.y, 6*cos(ang)+5*cos(ang), 6*sin(ang), 120])
            self.bulls.append([self.x - 5 * sin(ang), self.y, 6 * cos(ang) + 5 - cos(ang), 6 * sin(ang), 120])
            self.cooldown = self.maxCooldown

    def update(self, screen, empty, enemyList):
        self.cooldown = max(0, self.cooldown - 1)
        tx, ty = 0, 0
        m = 999999
        target = None
        for b in range(len(self.bulls) - 1, -1, -1):
            self.bulls[b][0] += self.bulls[b][2]
            self.bulls[b][1] += self.bulls[b][3]
            self.bulls[b][4] -= 1
            draw.circle(screen, self.col, (int(self.bulls[b][0]), int(self.bulls[b][1])), 4, 0)
            if not Rect(0, 0, 1440, 720).collidepoint(self.bulls[b][0], self.bulls[b][1]) or self.bulls[b][4] <= 0:
                del self.bulls[b]
        for enemy in enemyList:
            for b in range(len(self.bulls)-1, -1, -1):
                if enemy.rect.collidepoint(self.bulls[b][0], self.bulls[b][1]):
                    del self.bulls[b]
                    enemy.hp -= self.dmg
            if hypot(enemy.x - self.x, enemy.y - self.y) < m:
                m = hypot(enemy.x - self.x, enemy.y - self.y)
                tx, ty = (enemy.x, enemy.y)
                if hypot(enemy.x - self.x, enemy.y - self.y) < self.range:
                    target = enemy
        if target is not None:
            self.attack(target)
        if empty:
            if self.team == "A" and self.x < 700:
                if self.y > 360:
                    tx, ty = 705, 480
                else:
                    tx, ty = 705, 240
            elif self.team == "B" and self.x > 740:
                if self.y > 360:
                    tx, ty = 735, 480
                else:
                    tx, ty = 735, 240
        if target is None:
            self.move(tx, ty)
        self.draw(screen)


class TCircle:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 30
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.cooldown = 0
        self.maxCooldown = 300
        self.dmg = 10
        self.range = 100
        self.invinc = []
        self.bulls=[]
        self.cost = 10
        self.speed = 0.7
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.circle(screen, col, (int(self.x), int(self.y)), 25, 0)
        draw.circle(screen, self.col, (int(self.x), int(self.y)), 25, 3)

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        if self.cooldown <= 0:
            #target.hp -= self.dmg
            self.cooldown = self.maxCooldown
            for i in range(1,50):
                self.bulls.append([self.x, self.y, 4*cos(360/i), 4*sin(360/i), 30])

    def update(self, screen, empty, enemyList):
        tx, ty = 0, 0
        m = 999999
        self.cooldown = max(0, self.cooldown - 1)
        for b in range(len(self.bulls) - 1, -1, -1):
            self.bulls[b][0] += self.bulls[b][2]
            self.bulls[b][1] += self.bulls[b][3]
            self.bulls[b][4] -= 1
            draw.circle(screen, self.col, (int(self.bulls[b][0]), int(self.bulls[b][1])), 2, 0)
            if not Rect(0, 0, 1440, 720).collidepoint(self.bulls[b][0], self.bulls[b][1]) or self.bulls[b][4] <= 0:
                del self.bulls[b]
        target = None
        for enemy in enemyList:
            if hypot(enemy.x - self.x, enemy.y - self.y) < m:
                m = hypot(enemy.x - self.x, enemy.y - self.y)
                tx, ty = (enemy.x, enemy.y)
                if hypot(enemy.x - self.x, enemy.y - self.y) < self.range:
                    self.attack(enemy)
                    target = enemy
        for enemy in enemyList:
            for b in range(len(self.bulls)-1, -1, -1):
                if enemy.rect.collidepoint(self.bulls[b][0], self.bulls[b][1]):
                    del self.bulls[b]
                    enemy.hp -= self.dmg
        if empty:
            if self.team == "A" and self.x < 700:
                if self.y > 360:
                    tx, ty = 705, 480
                else:
                    tx, ty = 705, 240
            elif self.team == "B" and self.x > 740:
                if self.y > 360:
                    tx, ty = 735, 480
                else:
                    tx, ty = 735, 240
        if target is None:
            self.move(tx, ty)
        self.draw(screen)


class TPlus:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 6
        self.maxhp = 6
        self.rect = Rect(x - 25, y - 25, 50, 50)
        self.dmg = -5
        self.cooldown = 0
        self.invinc = []
        self.cost = 10
        self.speed = 8
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, self.col,
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


class TKite:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 55
        self.rect = Rect(x - 25, y - 75, 50, 100)
        self.dmg = 200
        self.maxCooldown = 350
        self.cooldown = 0
        self.invinc = 0
        self.cost = 14
        self.range = 500
        self.speed = 1
        self.team = team
        self.bulls = []
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, self.col,
                     [(self.x - 25, self.y), (self.x, self.y - 75), (self.x + 25, self.y), (self.x, self.y + 25)])

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)

    def attack(self, target):
        self.speed = self.cooldown/500
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class TSpinner:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.hp = 20
        self.rect = Rect(x - 30, y - 30, 60, 60)
        self.invinc = []
        self.dmg = 10
        self.cost = 6
        self.speed = 5
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        draw.polygon(screen, self.col, [(self.x - 10, self.y - 10), (self.x, self.y - 50),
                                           (self.x + 10, self.y - 10), (self.x + 50, self.y),
                                           (self.x + 10, self.y + 10), (self.x, self.y + 50),
                                           (self.x - 10, self.y + 10), (self.x - 50, self.y)], 3)

    def move(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        ang = atan2(dy, dx)
        self.x += self.speed * cos(ang)
        self.y += self.speed * sin(ang)
        self.rect = Rect(self.x - 30, self.y - 30, 60, 60)

    def attack(self, target):
        if self.rect.colliderect(target.rect):
            target.hp -= self.dmg
            self.hp = 0

    def update(self, screen, empty, enemyList):
        if self.team == "A":
            if self.x < 700:
                if self.y > 360:
                    tx, ty = 705, 480
                else:
                    tx, ty = 705, 240
            else:
                tx, ty = 1370, 310
                self.attack(enemyList[0])
        if self.team == "B":
            if self.x > 740:
                if self.y > 360:
                    tx, ty = 735, 480
                else:
                    tx, ty = 735, 240
            else:
                tx, ty = enemyList[0].x, enemyList[0].y

        self.draw(screen)
        self.move(tx, ty)



class TPentagon:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x - 50, y - 50, 100, 100)
        self.duration = 100
        self.cost = 12
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, self.col, [(self.x - 50, self.y), (self.x, self.y - 50),
                                           (self.x + 50, self.y), (self.x + 25, self.y + 50), (self.x - 25, self.y + 50)], 3)

    def effect(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, empty, enemyList):
        self.draw(screen)


class TLine:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x, y-50, 1, 100)
        self.cost = 3
        self.speed = 8
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        draw.line(screen, self.col, (self.x, self.y - 50), (self.x, self.y + 50))

    def move(self):
        self.x += self.speed

    def attack(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class TStar:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x - 50, y - 50, 100, 100)
        self.duration = 100
        self.cost = 8
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, self.col, [(self.x, self.y - 38), (self.x + 13, self.y - 13),
                                           (self.x + 38, self.y - 13), (self.x + 23, self.y + 13),
                                           (self.x + 29, self.y + 38), (self.x, self.y + 23),
                                           (self.x - 29, self.y + 38), (self.x - 23, self.y + 13),
                                           (self.x - 38, self.y - 13), (self.x - 13, self.y - 13)])

    def effect(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)


class THouse:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.rect = Rect(x - 50, y - 100, 100, 150)
        self.cost = 18
        self.team = team
        self.col = (0, 0, 255) if team == "A" else (255, 0, 0)

    def draw(self, screen):
        col = (self.col[0] * (self.cooldown / self.maxCooldown), self.col[1] * (self.cooldown / self.maxCooldown),
               self.col[2] * (self.cooldown / self.maxCooldown))
        draw.polygon(screen, self.col, [(self.x - 50, self.y - 50), (self.x, self.y - 100),
                                           (self.x + 50, self.y - 50), (self.x + 50, self.y + 50),
                                           (self.x - 50, self.y + 50)])

    def effect(self, target):
        if self.cooldown == 0:
            pass

    def update(self, screen, tx, ty, enemyList):
        self.move(tx, ty)

class Base:
    def __init__(self, team):
        if team == "A":
            self.x = 70
            self.y = 310
            self.col = (0, 0, 255)
        elif team == "B":
            self.x = 1370
            self.y = 310
            self.col = (255, 0, 0)
        self.rect = Rect(self.x-50, self.y-100, 100, 200)
        self.hp = 500
        self.maxhp = 500
        self.healthRect = (self.x - 10, self.y - 30, 20, 160)

    def draw(self, screen):
        draw.rect(screen, self.col, self.rect, 0)
        draw.rect(screen, (0, 255, 0), (self.x - 10, self.y - 80, 20, int(160 * (self.hp / self.maxhp))), 0)
        draw.rect(screen, (50, 100, 50), (self.x - 10, self.y - 80, 20, 160), 2)

    def update(self, screen, empty, enemyList):
        self.draw(screen)













