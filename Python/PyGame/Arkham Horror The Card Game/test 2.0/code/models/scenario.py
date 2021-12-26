import pygame

from setup import screen
from models import card, token

scenarios = []


class Scenario(card.Card):
    def __init__(self, image, image_back, type_mark):
        card.Card.__init__(self, image, image_back)
        self.show = card.convert(image, 2.5)
        self.show_back = card.convert(image_back, 2.5)
        self.type_mark = type_mark
        if type_mark:
            self.image = pygame.transform.rotate(self.image, 90)
            self.image_back = pygame.transform.rotate(self.image_back, 90)
            self.show = pygame.transform.rotate(self.show, 90)
            self.show_back = pygame.transform.rotate(self.show_back, 90)
            self.num = 0
            self.counter = token.get_token(type_mark)
            self.counter[1].midtop = (
                4 + type_mark) * screen.get_width() / 8, 0
        self.rect = self.show.get_rect()
        self.rect.midbottom = get_position(type_mark)


def get_position(num):
    width, height = screen.get_size()
    return (2 + num) * width / 4,  height / 24


def get_scenarios():
    scenarios.clear()
    positions = [0, -1, -1, -1, 1, 1, 1]

    for i in range(104, 111):
        image = pygame.image.load(
            "../images/CN/AHC01/01%d.jpg" % i).convert_alpha()
        image_back = pygame.image.load(
            "../images/CN/AHC01/01%db.jpg" % i).convert_alpha()
        index = i - 104
        scenarios.append(Scenario(image, image_back, positions[index]))
        if index in [2, 3, 5, 6]:
            scenarios[index].out_of_play = True
