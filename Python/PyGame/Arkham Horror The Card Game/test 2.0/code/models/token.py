import pygame

from setup import screen


class Token:
    def __init__(self, image):
        self.image = convert(image)
        self.rect = image.get_rect()
        self.num = 0


def convert(image, scale=22):
    rect = image.get_rect()
    ratio = screen.get_width() / scale / rect.width
    rect.width *= ratio
    rect.height *= ratio
    return pygame.transform.smoothscale(image, (rect.width, rect.height))


def get_damage(num):
    damage_tokens = []
    for i in range():
        damage_tokens.append(pygame.image.load(
            "../images/damage_token%d.png" % i + 1).convert_alpha())


def get_token(type_mark):
    if type_mark > 0:
        image = pygame.image.load(
            "../images/counter/scenario_counter.png").convert_alpha()
    elif type_mark < 0:
        image = pygame.image.load(
            "../images/counter/scenario_token_back.png").convert_alpha()
    else:
        image = pygame.image.load(
            "../images/counter/resource_token.png").convert_alpha()
    token = convert(image)
    return token, token.get_rect()
