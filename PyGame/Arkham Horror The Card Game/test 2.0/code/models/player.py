import pygame

from setup import screen
from models.investigator import investigators
from models.counter import get_counters

players = []


class Player:
    def __init__(self, id):
        self.id = id
        width, height = screen.get_size()
        l = id * width * 7 / 8
        w = width / 8
        h = height / 4
        self.photo_area = pygame.rect.Rect(l, 0, w, h)
        self.counters_area = pygame.rect.Rect(l, h, w, h / 2)
        self.assets_area = pygame.rect.Rect(l, h * 1.5, w, h)
        self.threat_area = pygame.rect.Rect(l, h * 2.5, w, h)
        self.hand_area = pygame.rect.Rect(l, h * 3.5, w * 3, h / 2)

    def select_investigators(self, index):
        self.investigator = investigators[index]
        self.investigator.photo_rect.center = self.photo_area.center
        self.set_counters()

    def set_counters(self):
        self.counters, self.rects = get_counters(self.investigator.photo_rect)
        self.rects[1].centery = self.rects[0].centery
        self.rects[2].centery = self.rects[3].centery

    def set_location(self, location):
        self.location = location
        if self.id:
            self.investigator.rect.midright = location.area.midright
        else:
            self.investigator.rect.midleft = location.area.midleft


def get_players(amount):
    players.clear()
    for id in range(amount):
        player = Player(id)
        player.select_investigators(id)
        players.append(player)
