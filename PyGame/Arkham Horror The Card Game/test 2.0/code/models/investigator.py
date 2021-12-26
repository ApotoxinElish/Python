import pygame

from models import card

investigators = []


class Investigator(card.Card):
    def __init__(self, image, image_back, mini_image, mini_image_back):
        card.Card.__init__(self, image, image_back)
        self.image = pygame.transform.rotate(self.image, 90)
        self.image_back = pygame.transform.rotate(self.image_back, 90)
        self.show = card.convert(mini_image, 8)
        self.show_back = card.convert(mini_image_back, 8)
        self.photo = card.convert(mini_image, 4)
        self.rect = self.show.get_rect()
        self.photo_rect = self.photo.get_rect()


def get_investigators():
    investigators.clear()
    for i in range(1, 6):
        mini = pygame.image.load(
            "../images/mini/%d.jpg" % i).convert_alpha()
        mini_back = pygame.image.load(
            "../images/mini/%db.jpg" % i).convert_alpha()
        image = pygame.image.load(
            "../images/CN/AHC01/0100%d.jpg" % i).convert_alpha()
        image_back = pygame.image.load(
            "../images/CN/AHC01/0100%db.jpg" % i).convert_alpha()
        investigators.append(Investigator(image, image_back, mini, mini_back))
