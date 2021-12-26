import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
bg = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

turtle = pygame.image.load("D:/Code/Python/PyGame/Arkham Horror The Card Game/Arkham/role/01001.png").convert()
background = pygame.image.load("D:/Code/Python/PyGame/Arkham Horror The Card Game/Arkham/role/01001.png").convert()
position = turtle.get_rect()
position.center = width // 2, height // 2

turtle.set_colorkey((255, 255, 255))
turtle.set_alpha(200)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(background, (0,0))
    screen.blit(turtle, position)

    pygame.display.flip()
    
    clock.tick(30)
