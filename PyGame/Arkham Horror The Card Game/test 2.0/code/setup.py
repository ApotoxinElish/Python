import pygame

pygame.init()
pygame.mixer.init()

bg_size = width, height = 1152, 649  # 1280, 657 # 1280, 720
screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
pygame.display.set_caption("诡镇奇谈LCG")

# background = pygame.image.load("images/background.png").convert()

# 载入游戏音乐
pygame.mixer.music.load("../sound/game_music.mp3")
pygame.mixer.music.set_volume(0.2)


def main():
    english_font = pygame.font.Font("../font/font.ttf", 48)
    chinese_font = pygame.font.Font("../font/font2.ttf", 48)
    # chinese_font = pygame.font.SysFont('SIMHEI', 48)
    # english_font = pygame.font.SysFont('TIMES', 48)

    white = (255, 255, 255)
    game_text2 = english_font.render(
        "And the oldest and strongest fear is fear of unknown", True, white)
    rect2 = game_text2.get_rect()
    rect2.midbottom = screen.get_rect().center
    screen.blit(game_text2, rect2)

    game_text1 = english_font.render(
        "The oldest and strongest emotion of mankind is fear", True, white)
    rect1 = game_text1.get_rect()
    rect1.midbottom = rect2.midtop
    screen.blit(game_text1, rect1)

    game_text1 = chinese_font.render(
        "人类最古老而强烈的情绪，便是恐惧；", True, white)
    rect1 = game_text1.get_rect()
    rect1.midtop = screen.get_rect().center
    screen.blit(game_text1, rect1)

    game_text2 = chinese_font.render(
        "而最古老最强烈的恐惧，便是对未知的恐惧。", True, white)
    rect2 = game_text2.get_rect()
    rect2.midtop = rect1.midbottom
    screen.blit(game_text2, rect2)

    pygame.display.flip()


main()


def select_scenario():
    pass


def select_investigators():
    pass
