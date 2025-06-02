"""Player Definition"""
import pygame
from Configurations import WIDTH, HEIGHT, BLUE, GRAVITY


class Player(pygame.sprite.Sprite):
    """Player Blueprint"""

    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load("assests/images/player/player.png").convert_alpha()
        # self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 200)
        self.vel_y = 0
        self.has_player_fallen_off = False

    def update(self):
        """Run this every game loop iteration"""
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        keys = pygame.key.get_pressed()
        # pylint: disable=no-member
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Wrap around screen
        if self.rect.right > WIDTH:
            self.rect.left = 0
        elif self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.has_player_fallen_off = True
            print("player has fallen off ", self.has_player_fallen_off)
