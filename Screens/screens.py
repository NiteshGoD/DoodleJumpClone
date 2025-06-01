"""Screens"""
import pygame
import sys

from Utilities import get_game_font
from Configurations import GRAY, WIDTH, HEIGHT, SKY_BLUE, JUMP_STRENGTH
from Utilities import render_text_drop_shadow
from Components import Button
from Sprites import Player
from GameLogic import GamePlay


class Screen():
    """Main Parent Screen"""

    def __init__(self, main_screen: pygame.surface.Surface):
        self.main_screen = main_screen
        self.text = None
        self.heading_font = get_game_font(size=22)
        self.description_font = get_game_font(size=18)
        self.buttons = []

    def on_event(self, event):
        # pylint: disable=no-member
        if event.type == pygame.QUIT:
            sys.exit()

    def on_loop(self):
        pass

    def render(self, callback=None):
        pass


class AboutScreen(Screen):
    """This screen is a render of game info and developers info"""

    def __init__(self, main_screen: pygame.surface.Surface):
        super().__init__(main_screen)
        self.buttons = []

    def on_event(self, event):
        return super().on_event(event)

    def render(self, callback=None):
        """Renders the about page on the screen"""
        self.main_screen.fill(GRAY)
        text_surf = render_text_drop_shadow(
            self.heading_font, "About Game", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH//2, HEIGHT//6)
        text_2 = self.description_font.render(
            "Work in progress", True, (0, 0, 0), GRAY)
        text_2_rect = text_2.get_rect()
        text_2_rect.center = (WIDTH//2 - 6, HEIGHT//3)
        text_3 = self.description_font.render(
            "Author: Nitesh Ranjitkar", True, (0, 0, 0), GRAY)
        text_3_rect = text_3.get_rect()
        text_3_rect.center = (WIDTH // 2 - 11, 9 / 10 * HEIGHT)
        self.main_screen.blit(text_surf, text_rect)
        self.main_screen.blit(text_2, text_2_rect)
        self.main_screen.blit(text_3, text_3_rect)
        pygame.display.flip()


class MenuScreen(Screen):
    """Menu Screen"""

    def __init__(self, main_screen):
        """Construtor"""
        super().__init__(main_screen)
        self.buttons: list[Button] = []
        self.start_button_txt = "Start Game"
        self.font = self.font = pygame.font.Font(
            'fonts/DepartureMonoNerdFont-Regular.otf', 22)

    def on_event(self, event):
        for button in self.buttons:
            button.check_click(event)

    def render(self, callback=None):
        """Draws the screen item to the screen"""
        self.main_screen.fill(SKY_BLUE)
        text_surf = render_text_drop_shadow(
            self.heading_font, "Main Menu", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH//2, HEIGHT//6)
        self.main_screen.blit(text_surf, text_rect)
        start_button = Button(self.start_button_txt, self.main_screen.get_width()//2 - 100, self.main_screen.get_height() //
                              2, 200, 60, self.font, lambda: callback("play") if callback else lambda: "play")
        about_button = Button("About Game", self.main_screen.get_width() // 2 -
                              100, self.main_screen.get_height() // 2 - 100, 200, 60, self.font, lambda: callback("about") if callback else lambda: "about")
        self.buttons.append(about_button)
        self.buttons.append(start_button)
        for button in self.buttons:
            button.draw(self.main_screen)
        # self.all_sprites.draw(self.screen)
        pygame.display.flip()


class GameScreen(Screen):
    """Screen for game"""

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.buttons = []
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.callback = None
        self.game_play = GamePlay(
            self.player, self.platforms, self.all_sprites, self.callback)
        self.game_play.game_start_setup()
        # self.right_after_game_start()

    def on_event(self, event):
        return super().on_event(event)

    def on_loop(self):
        self.game_play.during_loop()

    def render(self, callback=None):
        self.callback = callback
        if self.player.has_player_fallen_off:
            if callback:
                callback("game_over")
                self.player.has_player_fallen_off = False
        self.main_screen.fill(SKY_BLUE)
        text_surf = render_text_drop_shadow(
            self.heading_font, "GAME WINDOW", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH//2, HEIGHT//6)
        self.main_screen.blit(text_surf, text_rect)
        self.all_sprites.draw(self.main_screen)
        pygame.display.flip()


class GameOverScreen(Screen):
    def __init__(self, main_screen: pygame.surface.Surface):
        super().__init__(main_screen)
        self.callback = None
        self.buttons = []

    def on_event(self, event):
        # return super().on_event(event)
        if event.key == 27:
            if self.callback:
                # TODO go back to main menu
                self.callback("menu")
                # pylint: disable=no-member
                # pygame.quit()
                # sys.exit()

    @staticmethod
    def exit_game():
        pygame.quit()
        sys.exit()

    def render(self, callback=None):
        """Renders the about page on the screen"""
        # def to_restart():
        #     if callback:
        #         print("Calling callback in gameover_screen to restart")
        #         callback("restart")
        self.callback = callback
        self.main_screen.fill(SKY_BLUE)
        text_surf = render_text_drop_shadow(
            self.heading_font, "Game Over", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        restart_button = Button("Restart", self.main_screen.get_width()//2 - 100, self.main_screen.get_height(
        ) // 2 - 100, 200, 60, self.heading_font, lambda: callback("restart") if callback else "restart")
        text_rect.center = (WIDTH//2, HEIGHT//6)
        exit_button = Button("Exit", self.main_screen.get_width()//2 - 100, self.main_screen.get_height(
        ) // 2 - 200, 200, 60, self.heading_font, GameOverScreen.exit_game)
        self.main_screen.blit(text_surf, text_rect)
        self.buttons.append(restart_button)
        self.buttons.append(exit_button)
        for button in self.buttons:
            button.draw(self.main_screen)
        pygame.display.flip()
