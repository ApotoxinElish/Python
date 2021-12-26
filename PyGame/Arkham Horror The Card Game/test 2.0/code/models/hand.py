import pygame

from models import card

hands = []


class Hand:
    pass


def get_hands():
    amount = [67, 62, 61, 63, 63, 62, 29]
    card_back = pygame.image.load(
        "../images/player_card_back.jpg").convert_alpha()

    images_back = pygame.image.load(
        "../images/player_card_back.jpg").convert_alpha()

    for index in range(7):
        player_cards = pygame.image.load(
            "../images/player_cards%s.jpg" % index).convert_alpha()
        images = card.divide(player_cards, amount[index])

        classes = []
        for image in images:
            classes.append()
        hands.append(classes)


def main():
    pygame.init()
    bg_size = width, height = 1152, 648
    screen = pygame.display.set_mode(bg_size)


if __name__ == "__main__":
    main()
