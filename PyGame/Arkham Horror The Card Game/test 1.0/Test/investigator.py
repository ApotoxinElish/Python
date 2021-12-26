import pygame
import main
import location
import hand

investigators = []


class Investigator():
    num = 0

    def findImage(self):
        # 查找图片
        self.oimage = pygame.image.load(self.content['image'][0])
        self.oimageb = pygame.image.load(self.content['image'][1])
        self.orect = self.oimage.get_rect()
        # 正面
        self.rect = self.orect.copy()

    def convertImage(self):
        # 图片减半
        self.rect.width //= 2

        # 图片缩小 (135, 162)
        self.brect = self.rect.copy()
        self.bimage = self.oimage.subsurface(self.brect)

        self.brect.width //= 2
        self.brect.height //= 2
        self.bimage = pygame.transform.smoothscale(
            self.bimage, (self.brect.width, self.brect.height))

        # 图片减半
        self.rect.height //= 2
        self.image = self.oimage.subsurface(self.rect)

        # 图片缩小 (90, 54)
        self.rect.width //= 3
        self.rect.height //= 3
        self.image = pygame.transform.smoothscale(
            self.image, (self.rect.width, self.rect.height))

    def locateMini(self):
        if self.id:
            self.rect.right = self.location.area.right
        else:
            self.rect.left = self.location.area.left
        self.rect.centery = self.location.rect.centery

    def locateImage(self):
        # 图片定位
        # 迷你图片
        self.location = location.locations[0]
        self.locateMini()

        # 状态栏图片
        self.brect.centerx = main.width * (15 if self.id else 1) // 16
        self.brect.centery = main.height // 8

        # 原图片
        self.orect.center = main.width // 2, main.height // 2

    def setArea(self):
        self.assets_area = pygame.rect.Rect(
            0, main.height * 3 // 8, main.width // 8, main.height // 4)
        self.assets_area.left = main.width * 7 // 8 if self.id else 0

        self.threat_area = self.assets_area.copy()
        self.threat_area.top = self.assets_area.bottom

        self.hands_area = pygame.rect.Rect(
            0, main.height * 7 // 8, main.width * 13 // 32, main.height // 8)
        self.hands_area.left = main.width * (17 if self.id else 2) // 32

    def buildDeck(self):
        self.deck = []
        self.deck_image = pygame.image.load('image/deck.jpg')
        self.deck_rect = self.deck_image.get_rect()
        self.deck_rect.height //= 1.5
        self.deck_rect.width //= 1.5
        self.deck_image = pygame.transform.smoothscale(
            self.deck_image, (self.deck_rect.width, self.deck_rect.height))
        self.deck_rect.center = main.width * \
            (31 if self.id else 1) // 32, main.height * 15 // 16

    def __init__(self, content):
        self.content = content
        self.id = Investigator.num
        Investigator.num += 1

        self.setArea()
        self.buildDeck()

        self.health = content['health']
        self.sanity = content['sanity']
        self.resource = 5
        self.clue = 0
        self.num_center = []
        for i in range(4):
            self.num_center.append((main.width * ((3 if i % 2 else 1) + self.id * 28) // 32,
                                    main.height * (11 if i // 2 else 9) // 32))

        self.findImage()
        self.convertImage()
        self.locateImage()
        hand.getHands(self)


def showInvestigators():
    for each in investigators:
        main.screen.blit(each.bimage, each.brect)
        main.screen.blit(each.image, each.rect)
        hand.showHands(each)

        states = [each.health, each.sanity, each.resource, each.clue]
        color = [(255, 0, 0), (0, 255, 255), (255, 255, 0), (0, 255, 0)]
        for i in range(4):
            num = main.font.render("%d" % states[i], True, color[i])
            num_rect = num.get_rect()
            num_rect.center = each.num_center[i]
            main.screen.blit(num, num_rect)


def click(pos):
    for each in investigators:
        if each.rect.collidepoint(pos):
            return each, None
        elif each.brect.collidepoint(pos):
            return None, each
    return None, None


def move(investigator):
    for each in location.locations:
        if each.rect.collidepoint(investigator.rect.center):
            investigator.location = each
            break
    investigator.locateMini()


# 生成调查员
def getInvestigators(bg_size, location):
    content = {'image': ('core/01001.png', 'core/01001b.png'),
               'health': 9,
               'sanity': 5}
    investigators.append(Investigator(content))

    content = {'image': ['core/01005.png', 'core/01005b.png'],
               'health': 7,
               'sanity': 7}
    investigators.append(Investigator(content))
