"""Enemy Definition"""
import random
import pygame
from Configurations import WIDTH, HEIGHT, BLUE, GRAVITY


class Enemy(pygame.sprite.Sprite):
    """Player Blueprint"""

    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load("assests/images/player/player.png").convert_alpha()
        # self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10,WIDTH -32), 0)
        self.vel_y = 0
        self.has_player_fallen_off = False
        self.enemy_health = 3

    def update(self):
        
        if not(self.rect.y >= HEIGHT//3):
            self.vel_y += 1
            self.rect.y = self.vel_y

    def damage(self):
        if self.enemy_health > 0:
            self.enemy_health -= 1

    def draw(self, screen):
        if self.enemy_health > 0:
            screen.blit(self.image,(self.rect.x,self.rect.y))
