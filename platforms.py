"""Platforms definition"""
import pygame
# from configuration import GREEN
# from using_config_parser import GREEN
from check_python_version import is_python_version_greater_than_3_11
#from configuration import WIDTH, HEIGHT, GREEN, WHITE, FPS, JUMP_STRENGTH
if is_python_version_greater_than_3_11():
    from configuration import  GREEN
else:
    from using_config_parser import GREEN

class Platform(pygame.sprite.Sprite):
    """Platform blueprint"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
