import pygame
import sys
import traceback
import setup
import model
import view
import controller


def main():
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    model.main()

    running = True
    while running:
        controller.main()
        view.main()
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
