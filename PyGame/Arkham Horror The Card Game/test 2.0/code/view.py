import pygame

from setup import screen
from model import players, locations, scenarios
from controller import enlarge

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

game_font = pygame.font.Font("../font/font.TTF", 36)
number_font = pygame.font.Font("../font/font.TTF", screen.get_height() // 20)
# number_font = pygame.font.SysFont('SIMHEI', height // 24)


def set_font():
    global number_font
    number_font = pygame.font.Font(
        "../font/font.TTF", screen.get_height() // 20)


def draw(image, position):
    rect = image.get_rect()
    rect.center = position
    screen.blit(image, rect)


def draw_frame(image, position):
    rect = image.get_rect()
    rect.center = position
    pygame.draw.rect(screen, GREEN, rect, 2)


def draw_counters(counters, rects):
    for index in range(4):
        number = number_font.render("%d" % (index), True, WHITE)
        rect = number.get_rect()
        rect.center = rects[index].center
        screen.blit(counters[index], rects[index])
        screen.blit(number, rect)


def draw_curtain(rect):
    curtain = pygame.Surface(rect[2:])
    curtain.set_alpha(128)
    curtain.fill(BLACK)
    screen.blit(curtain, rect)


def main():
    set_font()
    screen.fill(BLACK)
    for each in locations:
        if not each.out_of_play:
            screen.blit(each.show_back if each.unrevealed
                        else each.show, each.rect)
            # draw_frame(each.show, each.rect.center)
    for each in players:
        each.set_location(locations[0])
        screen.blit(each.investigator.photo, each.investigator.photo_rect)
        screen.blit(each.investigator.show, each.investigator.rect)
        draw_counters(each.counters, each.rects)

    for each in scenarios:
        if not each.out_of_play:
            screen.blit(each.show, each.rect)
            if each.type_mark:
                screen.blit(each.counter[0], each.counter[1])
                number = number_font.render("%d" % each.num, True, WHITE)
                rect = number.get_rect()
                rect.center = each.counter[1].center
                screen.blit(number, rect)

    '''
    number = number_font.render("%d" % 77, True, WHITE)
    rect = number.get_rect()
    rect.centerx = width / 2
    screen.blit(number, rect)
    '''

    if enlarge:
        draw_curtain(screen.get_rect())
        rect = enlarge[0].image.get_rect()
        width, height = screen.get_size()
        rect.midright = width / 2, height / 2
        screen.blit(enlarge[0].image, rect)

    pygame.display.flip()
