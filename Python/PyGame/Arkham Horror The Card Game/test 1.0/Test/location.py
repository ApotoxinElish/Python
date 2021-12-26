import pygame
import main

locations = []
out_of_play = []


class Location():  # 300, 419
    def findImage(self):
        # 查找图片
        self.oimage = pygame.image.load(self.content['image'][1])
        self.oimageb = pygame.image.load(self.content['image'][0])
        self.orect = self.oimage.get_rect()
        self.rect = self.orect.copy()

    def convertImage(self):
        # 图片减半
        self.rect.height //= 2
        self.image = self.oimage.subsurface(self.rect)
        self.imageb = self.oimageb.subsurface(self.rect)

        # 图片缩小
        self.rect.width //= 1.5
        self.rect.height //= 1.5
        self.image = pygame.transform.smoothscale(
            self.image, (self.rect.width, self.rect.height))
        self.imageb = pygame.transform.smoothscale(
            self.imageb, (self.rect.width, self.rect.height))

    def locateImage(self):
        # 图片定位
        self.area = pygame.rect.Rect(0, 0, main.width // 4, main.height // 4)
        self.area.centerx = main.width * self.content['position'][0] // 4
        self.area.centery = main.height * self.content['position'][1] // 4
        self.rect.center = self.area.center
        self.orect.center = main.width // 2, main.height // 2

    def __init__(self, content):
        self.content = content
        self.revealed = False
        self.shroud = content['shroud']
        self.clue_value = content['clueValue']
        # 操作图片
        self.findImage()
        self.convertImage()
        self.locateImage()


def revealLoction(location):
    location.revealed = not location.revealed
    location.image, location.imageb = location.imageb, location.image
    location.oimage, location.oimageb = location.oimageb, location.oimage


def showLocations():
    for each in locations:
        main.screen.blit(each.image, each.rect)
        if each.revealed:
            nums = [each.shroud, each.clue_value]
            for i in range(2):
                num = main.font.render('%d' % nums[i], True,
                                       (0, 255, 0) if i else (255, 255, 255))
                num_rect = num.get_rect()
                if i:
                    num_rect.right = each.rect.right
                else:
                    num_rect.left = each.rect.left
                num_rect.bottom = each.rect.bottom
                main.screen.blit(num, num_rect)


# 生成地点
def getLocations():
    content = {'image': ('core/01111.png', 'core/01111b.png'),
               'position': (1, 1),
               'shroud': 2,
               'clueValue': 4}
    locations.append(Location(content))

    content = {'image': ('core/01112.jpg', 'core/01112b.png'),
               'position': (2, 2),
               'shroud': 1,
               'clueValue': 0}
    locations.append(Location(content))

    content = {'image': ('core/01113.jpg', 'core/01113b.png'),
               'position': (2, 1),
               'shroud': 1,
               'clueValue': 4}
    locations.append(Location(content))

    content = {'image': ('core/01114.jpg', 'core/01114b.png'),
               'position': (2, 3),
               'shroud': 4,
               'clueValue': 4}
    locations.append(Location(content))

    content = {'image': ('core/01115.jpg', 'core/01115b.png'),
               'position': (3, 2),
               'shroud': 2,
               'clueValue': 0}
    locations.append(Location(content))
