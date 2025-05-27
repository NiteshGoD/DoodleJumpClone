"""Main Game entry file"""
import random
import pygame
from configuration import WIDTH, HEIGHT, GREEN, WHITE, FPS, JUMP_STRENGTH
from player import Player
from platforms import Platform


class DoodleJumpGame():
    """Main Game Blueprint"""

    def __init__(self):
        """initialize pygame and set necessary game parameters"""
        # pylint: disable=no-member
        pygame.init()
        self.running = True
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Nitesh's Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(
            'fonts/DepartureMonoNerdFont-Regular.otf', 22)
        self.text = None
        self.text_rect = None
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

    def on_event(self, event):
        """checks the events here"""
        # pylint: disable=no-member
        if event.type == pygame.QUIT:
            self.running = False

    def right_after_game_start(self):
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

    def on_loop(self):
        """Updates"""
        # Jumping
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits and self.player.vel_y > 0:
            # SCORE += 1
            self.player.vel_y = JUMP_STRENGTH
        # Stop the game if player has fallen off
        if self.player.has_player_fallen_off:
            print("GAME OVER!!!")
            self.running = False

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

    def on_render(self):
        """Drawing on Screen"""
        self.screen.fill(WHITE)
        self.text = self.font.render("Work in progress", True, GREEN, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.width//2, self.height//6)
        self.screen.blit(self.text, self.text_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def on_cleanup(self):
        """After the main game loop is finished execute this"""
        # pylint: disable=no-member
        pygame.quit()

    def start(self):
        """Main game loop"""
        # Create sprite groups
        self.right_after_game_start()
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()


if __name__ == "__main__":
    game = DoodleJumpGame()
    game.start()
    game.on_cleanup()
