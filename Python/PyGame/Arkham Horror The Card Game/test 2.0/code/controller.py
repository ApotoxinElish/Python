import pygame
import sys
from setup import screen
import model

enlarge = []
move = []

fullscreen = False
bg_size = screen.get_size()


def find_enlarge(pos):
    for each in model.investigators:
        if each.photo_rect.collidepoint(pos):
            return each
    for each in model.locations + model.scenarios:
        if each.rect.collidepoint(pos):
            return each
    return None


def main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            # print(bg_size)
            model.main()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                global fullscreen
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(
                        (1280, 720), pygame.FULLSCREEN | pygame.HWSURFACE)
                else:
                    global bg_size
                    screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
                model.main()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and not enlarge:
                selection = find_enlarge(event.pos)
                if selection:
                    enlarge.append(selection)
            else:
                enlarge.clear()
