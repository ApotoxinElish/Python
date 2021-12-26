import pygame
import sys
import traceback

pygame.init()
# pygame.mixer.init()
bg_size = width, height = 1152, 648
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Arkham Test")
font = pygame.font.Font("font/font.ttf", int(height / 16))

import chaos
import scenario
import location
import investigator
import encounter
import hand

background = pygame.image.load("background/rules_reference.jpg").convert()
background_rect = background.get_rect()
background_rect.center = width // 2, height * 5 // 16

# 载入游戏音乐


def initialize():
    chaos.getChaos()
    # 生成地点
    scenario.getScenario()
    # 生成地点
    location.getLocations()
    # 生成调查员
    investigator.getInvestigators(bg_size, location.locations[0])
    # 生成敌人
    encounter.getEnemies()


def click(pos, cards):
    for each in cards:
        if each.rect.collidepoint(pos):
            return each
    return None


def mouseDown(button, pos):
    if button - 1:  # right click
        special = click(pos, chaos.reference + location.locations)
        if not special:
            return None, click(pos, hand.hands + encounter.enemies)
        elif type(special) is chaos.Reference:
            chaos.revealToken()
        elif type(special) is location.Location:
            location.revealLoction(special)
        return None, None

    else:  # left click
        chaos.token = None
        move, enlarge = investigator.click(pos)
        if move or enlarge:
            return move, enlarge

        move = click(pos, hand.hands + encounter.enemies)
        if move:
            return move, None

        return None, click(pos, chaos.reference + scenario.scenarios + location.locations)


def mouseEvent(move, enlarge):
    # 检测突发事件
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type is pygame.MOUSEBUTTONDOWN and not move:
            if not enlarge:
                move, enlarge = mouseDown(event.button, event.pos)

            elif not enlarge.orect.collidepoint(event.pos):
                enlarge = None

        elif event.type is pygame.MOUSEBUTTONUP and move:
            if type(move) is investigator.Investigator:
                investigator.move(move)
            elif type(move) is hand.Asset:
                hand.checkArea(move, investigator.investigators)
            elif type(move) is encounter.Enemy:
                encounter.checkArea(move)
            move = None
    return move, enlarge


def show(move, enlarge):
    screen.fill((0, 0, 0))
    screen.blit(background, background_rect)

    chaos.showChaos()
    scenario.showScenario()

    # screen.blit(hand_deck, hand_deck_rect)

    # 绘制调查员
    if move:
        move.rect.center = pygame.mouse.get_pos()

    encounter.showEnemies()
    investigator.showInvestigators()

    if enlarge:
        screen.blit(enlarge.oimage, enlarge.orect)
    elif move:
        screen.blit(move.image, move.rect)

    # screen.blit(damage_image, damage_image_rect)


def main():
    initialize()
    # 用于移动图片
    move = None
    # 用于放大图片
    enlarge = None
    # damage_image = pygame.image.load('images/other/Damage.jpg').convert()
    # damage_image.set_colorkey((255, 255, 255))
    # damage_image_rect = damage_image.get_rect()
    clock = pygame.time.Clock()
    running = True

    while running:
        move, enlarge = mouseEvent(move, enlarge)
        show(move, enlarge)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
