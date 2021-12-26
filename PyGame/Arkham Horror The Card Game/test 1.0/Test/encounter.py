import pygame
import random
import main
import location
import investigator

deck = []
discard_pile = []
enemies = []


class Encounter():
    deck = pygame.image.load('image/encounter.jpg')
    deck_rect = deck.get_rect()
    deck_rect.centerx = main.width * 3 // 16

    def findImage(self):
        # 查找图片
        self.oimage = pygame.image.load(self.content['image'])
        self.orect = self.oimage.get_rect()
        self.rect = self.orect.copy()

    def convertImage(self):
        # 图片减半
        self.rect.top = self.rect.centery if type(self) == Enemy else 0
        self.rect.height = self.rect.height // 2
        self.image = self.oimage.subsurface(self.rect)

        # 图片缩小 85 * 59 (3.5)  100 * 69 (3)
        self.rect.width //= 3.5
        self.rect.height //= 3.5
        self.image = pygame.transform.smoothscale(
            self.image, (self.rect.width, self.rect.height))

    def locateImage(self):
        # 图片定位
        # 迷你图片
        self.location = location.locations[0]
        self.rect.left = random.randint(
            self.location.area.left, self.location.area.right - self.rect.width)
        self.rect.top = random.randint(
            self.location.area.top, self.location.area.bottom - self.rect.height)

        # 原图片
        self.orect.center = main.width // 2, main.height // 2

    def __init__(self, content):
        self.content = content

        self.findImage()
        self.convertImage()
        self.locateImage()


class Enemy(Encounter):
    def __init__(self, content):
        Encounter.__init__(self, content)
        self.health = content['health']
        self.engaged = None


class Treachery(Encounter):
    def __init__(self, content):
        Encounter.__init__(self, content)


def checkArea(enemy):
    for each in investigator.investigators:
        if each.threat_area.left < enemy.rect.centerx < each.threat_area.right:
            enemy.engaged = each
            break

    if enemy.engaged:
        if enemy.rect.left < enemy.engaged.threat_area.left:
            enemy.rect.left = enemy.engaged.threat_area.left
        elif enemy.rect.right > enemy.engaged.threat_area.right:
            enemy.rect.right = enemy.engaged.threat_area.right
        if enemy.rect.top < enemy.engaged.threat_area.top:
            enemy.rect.top = enemy.engaged.threat_area.top
        elif enemy.rect.bottom > enemy.engaged.threat_area.bottom:
            enemy.rect.bottom = enemy.engaged.threat_area.bottom
    else:
        if enemy.rect.left < enemy.location.area.left:
            enemy.rect.left = enemy.location.area.left
        elif enemy.rect.right > enemy.location.area.right:
            enemy.rect.right = enemy.location.area.right
        if enemy.rect.top < enemy.location.area.top:
            enemy.rect.top = enemy.location.area.top
        elif enemy.rect.bottom > enemy.location.area.bottom:
            enemy.rect.bottom = enemy.location.area.bottom


def showEnemies():
    main.screen.blit(Encounter.deck, Encounter.deck_rect)
    num = main.font.render("%s" % str(len(deck)), True, (255, 255, 255))
    num_rect = num.get_rect()
    num_rect.centerx = Encounter.deck_rect.centerx
    num_rect.bottom = Encounter.deck_rect.bottom
    main.screen.blit(num, num_rect)

    location.showLocations()

    for each in enemies:
        main.screen.blit(each.image, each.rect)

        health = main.font.render("%s" % str(each.health), True, (255, 0, 0))
        health_rect = health.get_rect()
        health_rect.left = each.rect.left
        health_rect.bottom = each.rect.bottom
        main.screen.blit(health, health_rect)


# 生成敌人
def getEnemies():
    content = {'image': 'core/01116.png',
               'health': 10}
    enemies.append(Enemy(content))

    content = {'image': 'core/01118.jpg',
               'health': 4}
    enemies.append(Enemy(content))

    return enemies
