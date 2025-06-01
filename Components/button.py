from typing import Callable
import pygame
from Configurations import DARK_GRAY, GRAY


class Button():
    """Blue Print for making buttons"""
    def __init__(self, text: str, x: int, y: int, width: int, height: int, font: pygame.font.Font, callback: Callable):
        self.text = text
        # self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.font = font

    def draw(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            color = DARK_GRAY
        else:
            color = GRAY
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, event):
        # pylint: disable=no-member
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
