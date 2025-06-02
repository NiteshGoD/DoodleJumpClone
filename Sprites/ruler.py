import pygame
from Configurations import GRAY, WHITE
from Utilities import get_game_font


class Ruler(pygame.sprite.Sprite):
    """Platform blueprint"""

    def __init__(self, x, y, text = "0"):
        super().__init__()
        self.image = pygame.Surface((20, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = get_game_font(10)
        self.textSurf = self.font.render(text,True, (0,0,0) , WHITE)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf,[20//2 - W/2, 10/2 - H/2])
