import pygame

from setup import screen
from models import card

locations = []


class Location(card.Card):
    def __init__(self, image, image_back):
        card.Card.__init__(self, image, image_back)
        self.show = card.convert(card.cut(image), 4.5)
        self.show_back = card.convert(card.cut(image_back), 4.5)
        self.rect = self.show.get_rect()
        width, height = screen.get_size()
        self.area = pygame.rect.Rect(0, 0, width / 4, height / 4)
        self.unrevealed = False


def get_position(num):
    width, height = screen.get_size()
    return (num % 3 + 1) * width / 4, (num // 3 / 4 + 1 / 6) * height


def get_positions():
    positions = [("Study", 3), ("Hallway", 4), ("Attic", 1),
                 ("Cellar", 7), ("Parlor", 5)]
    for index in range(len(positions)):
        name, num = positions[index]
        locations[index].name = name
        locations[index].area.center = locations[index].rect.center \
            = get_position(num)


def get_locations():
    locations.clear()
    for i in range(111, 116):
        image = pygame.image.load(
            "../images/CN/AHC01/01%d.jpg" % i).convert_alpha()
        image_back = pygame.image.load(
            "../images/CN/AHC01/01%db.jpg" % i).convert_alpha()
        locations.append(Location(image, image_back))

    get_positions()
