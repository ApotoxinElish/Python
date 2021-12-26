import pygame


def get_image(name):
    return pygame.image.load("../images/counter/%s_counter.png" % name).convert_alpha()


def convert(image, width):
    rect = image.get_rect()
    ratio = width / rect.width / 2
    rect.width *= ratio
    rect.height *= ratio
    return pygame.transform.smoothscale(image, (rect.width, rect.height)), rect


def get_position(photo_rect, rect, index):
    if index // 2:
        rect.top = photo_rect.bottom
    else:
        rect.bottom = photo_rect.bottom
    rect.left = photo_rect.left + index % 2 * rect.width
    return rect


def get_counters(photo_rect):
    counters = []
    rects = []
    names = ["damage", "horror", "scenario", "resource"]
    for index in range(4):
        image, rect = convert(get_image(names[index]), photo_rect.width)
        rect = get_position(photo_rect, rect, index)
        counters.append(image)
        rects.append(rect)
    return counters, rects
