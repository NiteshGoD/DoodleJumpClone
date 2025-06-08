import pygame
import random
from typing import Callable, Optional
from Configurations import JUMP_STRENGTH, HEIGHT, WIDTH
from Sprites import Player, Platform, Ruler


class GamePlay():
    def __init__(self, player, platforms, all_sprites: pygame.sprite.Group, change_game_state: Optional[Callable] = None):
        self.player = player
        self.platforms = platforms
        self.all_sprites = all_sprites
        self.change_game_state = change_game_state
        self.player.has_player_fallen_off = False
        self.ruler = pygame.sprite.Group()
        self.distance_travelled = 0
        self.score = None

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
            self.distance_travelled += 1
            self.player.rect.y += abs(self.player.vel_y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel_y)
                if plat.rect.top > HEIGHT:
                    plat.kill()
                    new_plat = Platform(random.randint(
                        0, WIDTH - 80), random.randint(-20, 0))
                    self.all_sprites.add(new_plat)
                    self.platforms.add(new_plat)
            for scale in self.ruler:
                scale.rect.y += abs(self.player.vel_y)
                if scale.rect.top > HEIGHT:
                    scale.kill()
                    new_scale = Ruler(WIDTH-20,10,str(HEIGHT + self.distance_travelled))
                    self.all_sprites.add(new_scale)
                    self.ruler.add(new_scale)
        self.all_sprites.update()
        self.player.update()

    def scale_on_the_right(self):
        # scale = Ruler(WIDTH-20,HEIGHT)
        for unit in range(1,HEIGHT,50):
            # self.distance_travelled += 1
            scale = Ruler(WIDTH-20, unit, str((HEIGHT-unit)))
            # scale = Ruler(WIDTH-20, unit, str(HEIGHT- self.distance_travelled))
            self.all_sprites.add(scale)
            self.ruler.add(scale)

    def game_start_setup(self):
        """setting up sprites when game starts"""
        self.scale_on_the_right()
        self.all_sprites.add(self.player)
        # Create initial platforms
        initial_plat = Platform(WIDTH//2, HEIGHT - 10)
        self.all_sprites.add(initial_plat)
        self.platforms.add(initial_plat)
        for i in range(7):
            plat = Platform(random.randint(0, WIDTH - 80), i * 80)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
