"""Platforms definition"""
import pygame
from Configurations import WHITE


class Platform(pygame.sprite.Sprite):
    """Platform blueprint"""

    def __init__(self, x, y):
        super().__init__()
        # self.image = pygame.Surface((80, 10))
        self.image = pygame.image.load("assests/images/platforms/cloud_.png").convert_alpha()
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
