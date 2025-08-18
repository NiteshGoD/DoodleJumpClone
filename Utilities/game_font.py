import pygame
from .resource_path import resource_pathway

def get_game_font(size : int):
    font = pygame.font.Font(resource_pathway('assets/fonts/DepartureMonoNerdFont-Regular.otf'), size)
    return font