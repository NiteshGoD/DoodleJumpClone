import pygame
import random
from typing import Callable, Optional
from Configurations import JUMP_STRENGTH, HEIGHT, WIDTH
from Sprites import Player, Platform


class GamePlay():
    def __init__(self, player, platforms, all_sprites: pygame.sprite.Group, change_game_state: Optional[Callable] = None):
        self.player = player
        self.platforms = platforms
        self.all_sprites = all_sprites
        self.change_game_state = change_game_state
        self.player.has_player_fallen_off = False

    def did_land(self):
        pass

    def during_loop(self):
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits and self.player.vel_y > 0:
            self.player.vel_y = JUMP_STRENGTH
        if self.player.has_player_fallen_off:
            # print("Game Over")
            if self.change_game_state:
                self.change_game_state("game_over")
        # Scroll the screen if player reaches upper third
        if self.player.rect.top <= HEIGHT // 3:
            self.player.rect.y += abs(self.player.vel_y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel_y)
                if plat.rect.top > HEIGHT:
                    plat.kill()
                    new_plat = Platform(random.randint(
                        0, WIDTH - 80), random.randint(-20, 0))
                    self.all_sprites.add(new_plat)
                    self.platforms.add(new_plat)
        self.all_sprites.update()

    def game_start_setup(self):
        """setting up sprites when game starts"""
        self.all_sprites.add(self.player)
        # Create initial platforms
        initial_plat = Platform(WIDTH//2, HEIGHT - 10)
        self.all_sprites.add(initial_plat)
        self.platforms.add(initial_plat)
        for i in range(7):
            plat = Platform(random.randint(0, WIDTH - 80), i * 80)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
