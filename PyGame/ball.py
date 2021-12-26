import pygame
import sys

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (0,0,0)

ball = pygame.image.load('Arkham Horror The Card Game/test 2.0/images/chaos_token1.png')
ballrect = ball.get_rect()

speed=[5,5]
clock = pygame.time.Clock()# 设置时钟，需要使用pygame下的time模块

while True:
    clock.tick(60) # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(color)
    screen.blit(ball,ballrect)
    pygame.display.flip()

pygame.quit()
