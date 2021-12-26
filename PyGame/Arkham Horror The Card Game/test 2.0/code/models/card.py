import pygame

from setup import screen


class Card:
    def __init__(self, image, image_back):
        self.image = convert(image)
        self.image_back = convert(image_back)
        self.out_of_play = False


def put_into_play(obj):
    obj.out_of_play = False


def set_aside(obj):
    obj.out_of_play = True


def divide(image, amount, section=(10, 7)):
    rect = image.get_rect()
    rect.width /= section[0]
    rect.height /= section[1]
    images = []
    for index in range(amount):
        rect.left = index % section[0] * rect.width
        rect.top = index // section[0] * rect.height
        new_image = image.subsurface(rect).copy()
        images.append(new_image)
    return images


def cut(image, part="top"):
    rect = image.get_rect()
    if part == "top":
        rect.height /= 2
        image = image.subsurface(rect).copy()
    elif part == "bottom":
        rect.height /= 2
        rect.top = rect.bottom
        image = image.subsurface(rect).copy()
    elif part == "left":
        rect.width /= 2
        image = image.subsurface(rect).copy()
    elif part == "right":
        rect.width /= 2
        rect.left = rect.right
        image = image.subsurface(rect).copy()
    return image


def convert(image, scale=1.2):
    rect = image.get_rect()
    ratio = screen.get_height() / scale / rect.height
    rect.width *= ratio
    rect.height *= ratio
    return pygame.transform.smoothscale(image, (rect.width, rect.height))
