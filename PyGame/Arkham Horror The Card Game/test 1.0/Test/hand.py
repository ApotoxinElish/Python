import pygame
import random
import main
import investigator

hands = []


class Hand():
    def findImage(self):
        # 查找图片
        self.oimage = pygame.image.load(self.content['image'])
        self.orect = self.oimage.get_rect()
        self.rect = self.orect.copy()

    def convertImage(self):
        # 图片减半
        self.rect.height //= 2
        self.image = self.oimage.subsurface(self.rect)

        # 图片缩小 85 * 59 (3.5)  100 * 69 (3)
        self.rect.width //= 3.5
        self.rect.height //= 3.5
        self.image = pygame.transform.smoothscale(
            self.image, (self.rect.width, self.rect.height))

    def locateImage(self):
        # 图片定位
        # 迷你图片
        self.rect.left = random.randint(
            self.belongs.hands_area.left, self.belongs.hands_area.right - self.rect.width)
        self.rect.top = random.randint(
            self.belongs.hands_area.top, self.belongs.hands_area.bottom - self.rect.height)

        # 原图片
        self.orect.center = main.width // 2, main.height // 2

    def __init__(self, investigator, content):
        self.belongs = investigator
        self.content = content
        self.cost = content['cost']

        self.findImage()
        self.convertImage()
        self.locateImage()
        hands.append(self)


class Asset(Hand):
    def __init__(self, investigator, content):
        Hand.__init__(self, investigator, content)
        self.using = False


class Event(Hand):
    def __init__(self, content):
        Hand.__init__(self, content)


class Skill(Hand):
    def __init__(self, content):
        Hand.__init__(self, content)


def checkArea(asset, investigators):
    '''for i in investigators:
        if i.barea.height * 3 // 8 < asset.rect.centery < i.barea.height * 5 // 8:
            asset.using = i
            break

    if asset.using:
        if asset.rect.left < asset.using.barea.left:
            asset.rect.left = asset.using.barea.left
        elif asset.rect.right > asset.using.barea.right:
            asset.rect.right = asset.using.barea.right
        if asset.rect.top < int(asset.using.barea.height * 3 / 8):
            asset.rect.top = int(asset.using.barea.height * 3 / 8)
        elif asset.rect.bottom > int(asset.using.barea.height * 5 / 8):
            asset.rect.bottom = int(asset.using.barea.height * 5 / 8)
    else:'''
    if asset.rect.left < asset.belongs.hands_area.left:
        asset.rect.left = asset.belongs.hands_area.left
    elif asset.rect.right > asset.belongs.hands_area.right:
        asset.rect.right = asset.belongs.hands_area.right
    if asset.rect.top < asset.belongs.hands_area.top:
        asset.rect.top = asset.belongs.hands_area.top
    elif asset.rect.bottom > asset.belongs.hands_area.bottom:
        asset.rect.bottom = asset.belongs.hands_area.bottom


def showHands(investigator):
    main.screen.blit(investigator.deck_image, investigator.deck_rect)
    num = main.font.render("%d" % len(
        investigator.deck), True, (255, 255, 255))
    num_rect = num.get_rect()
    num_rect.center = investigator.deck_rect.center
    main.screen.blit(num, num_rect)

    for each in investigator.deck:
        main.screen.blit(each.image, each.rect)

        cost = main.font.render("%d" % each.cost, True, (255, 255, 0))
        cost_rect = cost.get_rect()
        cost_rect.right = each.rect.right
        cost_rect.bottom = each.rect.bottom
        main.screen.blit(cost, cost_rect)


# 生成敌人
def getHands(investigator):
    content = {'image': 'core/01016.png',
               'cost': 10}
    investigator.deck.append(Asset(investigator, content))

    content = {'image': 'core/01017.png',
               'cost': 4}
    investigator.deck.append(Asset(investigator, content))

    return hands
