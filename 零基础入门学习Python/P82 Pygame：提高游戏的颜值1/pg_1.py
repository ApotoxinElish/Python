import pygame
import sys
from pygame.locals import *

# 初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)  # RGB

fullscreen =

# 创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 加在图片
turtle = pygame.image.load("turtle.png")
# 获得图像的位置矩形
position = turtle.get_rect()

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)
