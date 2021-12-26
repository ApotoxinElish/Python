import pygame
import random
import main

reference = []
bag = []
token = None


class Reference():
    def findImage(self):
        # (300, 419)
        self.oimage = pygame.image.load(self.content['image'][self.level])
        self.orect = self.oimage.get_rect()
        self.rect = self.orect.copy()

    def convertImage(self):
        # (135, 81)
        self.rect.width //= 3.5
        self.rect.height //= 3.5
        self.image = pygame.transform.smoothscale(
            self.oimage, (self.rect.width, self.rect.height))

    def locateImage(self):
        self.rect.center = main.width * 13 // 16, main.height // 16
        self.orect.center = main.width // 2, main.height // 2

    def __init__(self, content):
        self.content = content
        self.level = 0

        self.findImage()
        self.convertImage()
        self.locateImage()


class Token():
    def __init__(self, num):
        self.num = num
        if num > 1:
            self.image = pygame.image.load('image/chaos' + str(num) + '.jpg')
        else:
            self.image = main.font.render('%+d' % num, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = main.width * 3 // 4, main.height // 16


def revealToken():
    random.shuffle(bag)
    global token
    token = bag[random.randint(0, len(bag) - 1)]


def showChaos():
    main.screen.blit(reference[0].image, reference[0].rect)
    if token:
        main.screen.blit(token.image, token.rect)


def getBag():
    tokens = [1, 0, 0, -1, -1, -1, -2, -2, -3, -4, 4, 4, 5, 6, 2, 3]
    for i in tokens:
        bag.append(Token(i))


def getChaos():
    content = {'image': ('core/01104.jpg', 'core/01104b.jpg')}
    reference.append(Reference(content))
    getBag()
