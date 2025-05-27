"""Platforms definition"""
import pygame
from configuration import GREEN

class Platform(pygame.sprite.Sprite):
    """Platform blueprint"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
