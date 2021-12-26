import pygame
import main

agendas = []
acts = []
scenarios = []


class Scenario():
    def findImage(self):
        # 查找图片
        self.oimage = pygame.image.load(self.content['image'][0])
        self.orect = self.oimage.get_rect()
        self.oimageb = pygame.image.load(self.content['image'][1])
        self.orectb = self.oimageb.get_rect()
        # 正面
        self.rect = self.orect.copy()

    def convertImage(self):
        # 图片缩小 81
        self.rect.width //= 3.5
        self.rect.height //= 3.5
        self.image = pygame.transform.smoothscale(
            self.oimage, (self.rect.width, self.rect.height))

    def locateImage(self):
        # 图片定位
        self.orect.center = main.width // 2, main.height // 2
        self.orectb.center = main.width // 2, main.height // 2

    def __init__(self, content):
        self.content = content
        self.num = 0

        self.findImage()
        self.convertImage()
        self.locateImage()


class Agenda(Scenario):  # 419 * 300
    def locateImage(self):
        Scenario.locateImage(self)
        # 迷你图片
        self.rect.centerx = main.width // 3

    def __init__(self, content):
        Scenario.__init__(self, content)


class Act(Scenario):  # 419 * 300
    def locateImage(self):
        Scenario.locateImage(self)
        # 迷你图片
        self.rect.centerx = main.width * 7 // 12

    def __init__(self, content):
        Scenario.__init__(self, content)


def showScenario():
    for each in scenarios:
        main.screen.blit(each.image, each.rect)
        num = main.font.render('%d/%d' % (each.num, each.content['threshold']), True,
                               (0, 255, 0) if type(each) is Act else (255, 0, 255))
        num_rect = num.get_rect()
        num_rect.left = each.rect.right
        num_rect.centery = each.rect.centery
        main.screen.blit(num, num_rect)


def getAgenda():
    content = {'image': ('core/01105.jpg', 'core/01105b.jpg'),
               'threshold': 3}
    agendas.append(Agenda(content))


def getAct():
    content = {'image': ('core/01108.jpg', 'core/01108b.jpg'),
               'threshold': 4}
    acts.append(Act(content))


def getScenario():
    getAgenda()
    getAct()
    global scenarios
    scenarios = [agendas[0], acts[0]]
