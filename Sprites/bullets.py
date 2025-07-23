"""Bullet Definition"""
import pygame
from Configurations import WIDTH, HEIGHT, BLUE, GRAVITY


class Bullets(pygame.sprite.Sprite):
    """Player Blueprint"""

    def __init__(self, player_pos):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        # self.image = pygame.image.load("assests/images/player/player.png").convert_alpha()
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = player_pos
        self.vel_y = -10
        # self.has_player_fallen_off = False

    def update(self):
        self.rect.y += self.vel_y