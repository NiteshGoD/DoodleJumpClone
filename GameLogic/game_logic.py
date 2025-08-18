"""Game Play Logic"""
import math
import random
from typing import Callable, Optional
import pygame
from Configurations import JUMP_STRENGTH, HEIGHT, WIDTH
from Sprites import Platform, Ruler, Enemy, Bullets


class GamePlay():
    """Main Gameplay"""

    def __init__(self, player, platforms,
                 score_handler,
                 all_sprites: pygame.sprite.Group,
                 change_game_state: Optional[Callable] = None):
        self.player = player
        self.platforms = platforms
        self.all_sprites = all_sprites
        self.score_handler = score_handler
        self.change_game_state = change_game_state
        self.player.has_player_fallen_off = False
        self.ruler = pygame.sprite.Group()
        self.distance_travelled = 0
        self.score = 0
        self.enemy = None
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_spawn_interval = 0
        self.interval = 300

    def did_land(self):
        """when player lands on the platform"""
        raise NotImplementedError

    def change_enemy_spawn_interval(self, decrease_by):
        """Enemy must spawn after less"""
        if self.interval >= 95:
            self.interval = math.ceil(
                self.interval - ((decrease_by/100) * self.interval))
        print(self.interval)

    def spawn_enemy(self):
        """Creates new enemy"""
        enemy = Enemy()
        self.enemy = enemy
        self.all_sprites.add(enemy)
        self.enemies.add(self.enemy)
        # self.all_sprites.add(self.enemy)

    def fire_bullets(self):
        """Creates new bullets"""
        bullet = Bullets(self.player.rect.center)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
        # print("Bullet should be fired now")

    def game_over_setup(self, music_player=None):
        self.score_handler.reset_kills()
        if music_player:
            music_player.stop_music()

    def during_loop(self):
        """This block runs in every frame"""
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits and self.player.vel_y > 0:
            self.player.music_player.play_jump_sound()
            self.player.vel_y = JUMP_STRENGTH
        if self.player.has_player_fallen_off:
            # print("Game Over")
            if self.change_game_state:
                self.change_game_state("game_over")
                # self.game_over_setup()
        # spawn enemy after some time
        # if self.distance_travelled == 100:
        if self.enemy_spawn_interval == self.interval:
            self.spawn_enemy()
            self.change_enemy_spawn_interval(5)
            self.enemy_spawn_interval = 0
        if self.enemy and self.enemy.rect.bottom > HEIGHT:
            self.enemy.kill()
        # Scroll the screen if player reaches upper third
        if self.player.rect.top <= HEIGHT // 3:
            self.distance_travelled += 1
            self.enemy_spawn_interval += 1
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
                    new_scale = Ruler(
                        WIDTH-20, 10, str(HEIGHT + self.distance_travelled))
                    self.all_sprites.add(new_scale)
                    self.ruler.add(new_scale)
            # shifting enemy too
        if self.enemy:
            enemy_player_collision = pygame.sprite.spritecollide(
                self.player, self.enemies, False)
            if enemy_player_collision:
                print("Player touched the enemy")
                # self.player.has_player_fallen_off =
                self.player.damage()
            self.enemy.rect.y += abs(self.player.vel_y)
            for enemies in self.enemies:
                if enemies.rect.bottom > HEIGHT:
                    print("Enemy off screen killed")
                    enemies.kill()
                    self.enemies.remove(enemies)

            if self.enemy.rect.bottom > HEIGHT:
                self.enemy.kill()
                # print("Enemy killed because out of screen")
                self.enemies.remove(self.enemy)
                # self.enemy=None
            target_hit = pygame.sprite.spritecollide(
                self.enemy, self.bullets, False)
            if target_hit:
                self.enemy.damage()
                self.player.music_player.play_hit_sound()
                if self.enemy.enemy_health <= 0:
                    self.score_handler.update_kills()
                    self.enemy.kill()
                # self.enemy = None
                    print("Enemy killed")
                    self.enemies.remove(self.enemy)
            # if self.distance_travelled > 200 and self.distance_travelled %  == 0:
            #             self.spawn_enemy()
        for bullet in self.bullets:
            # print(bullet)
            if bullet.rect.bottom <= 0:
                print("bullet killed")
                bullet.kill()
                self.bullets.remove(bullet)
        self.all_sprites.update()
        self.enemies.update()
        self.player.update()
        self.score_handler.update_score(self.distance_travelled)
        self.score_handler.update_high_kills()

    # def scale_on_the_right(self):
    #     """scaling"""
    #     # scale = Ruler(WIDTH-20,HEIGHT)
    #     for unit in range(1, HEIGHT, 50):
    #         # self.distance_travelled += 1
    #         scale = Ruler(WIDTH-20, unit, str((HEIGHT-unit)))
    #         # scale = Ruler(WIDTH-20, unit, str(HEIGHT- self.distance_travelled))
    #         self.all_sprites.add(scale)
    #         self.ruler.add(scale)

    def game_start_setup(self, music_player):
        """setting up sprites when game starts"""
        music_player.ready_music()
        # self.scale_on_the_right()
        self.all_sprites.add(self.player)
        # Create initial platforms
        initial_plat = Platform(WIDTH//2, HEIGHT - 10)
        self.all_sprites.add(initial_plat)
        self.platforms.add(initial_plat)
        for i in range(7):
            plat = Platform(random.randint(0, WIDTH - 80), i * 80)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
