import pygame


class Card():  # 300, 419
    enlarge = None

    def findImage(self, path):
        # 查找图片
        self.oimage = pygame.image.load(path).convert_alpha()
        self.rect = self.oimage.get_rect()

    def convertImage(self):
        # 图片减半
        self.rect.height = int(self.rect.height / 2)
        self.image = self.oimage.subsurface(self.rect)

        # 图片缩小
        self.rect.width = int(self.rect.width / 1.5)
        self.rect.height = int(self.rect.height / 1.5)
        self.image = pygame.transform.smoothscale(
            self.image, (self.rect.width, self.rect.height))

    def locateImage(self, bg_size, position, location):
        # 图片定位
        self.area = position[location[0]][location[1]]
        self.rect.center = self.area.center

        self.orect = self.oimage.get_rect()
        self.orect.left = int(bg_size[0] / 16)
        self.orect.top = int(bg_size[1] / 16)

    def __init__(self, bg_size, position, content):
        # 操作图片
        self.findImage(content['image'])
        self.convertImage()
        self.locateImage(bg_size, position, content['position'])

        self.content = content
