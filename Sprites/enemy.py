"""Enemy Definition"""
import random
import pygame
from Configurations import WIDTH, HEIGHT
from Utilities import resource_pathway


class Enemy(pygame.sprite.Sprite):
    """Player Blueprint"""

    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load(resource_pathway("assets/images/player/player.png")).convert_alpha()
        # self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10,WIDTH -32), 0)
        self.vel_y = 0
        self.has_player_fallen_off = False
        self.enemy_health = 3

    def update(self):
        """enemy moves slowly down"""
        if not self.rect.y >= HEIGHT//3:
            self.vel_y += 1
            self.rect.y = self.vel_y
        else:
            self.vel_y += 5
            self.rect.y = self.vel_y

    def damage(self):
        """Decrease health of the enemy"""
        if self.enemy_health > 0:
            self.enemy_health -= 1

    def draw(self, screen):
        """Draw enemy on screen if enemy has health"""
        if self.enemy_health > 0:
            screen.blit(self.image,(self.rect.x,self.rect.y))
