"""Platforms definition"""
import pygame
# from configuration import GREEN
# from using_config_parser import GREEN
from Utilities.check_python_version import is_python_version_greater_than_3_11
# from configuration import WIDTH, HEIGHT, GREEN, WHITE, FPS, JUMP_STRENGTH
if is_python_version_greater_than_3_11():
    from Configurations.configuration import GREEN, WHITE
else:
    from Configurations.using_config_parser import GREEN, WHITE


class Platform(pygame.sprite.Sprite):
    """Platform blueprint"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
