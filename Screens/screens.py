"""Screens"""
import sys
import random
import pygame

# import textwrap


from Configurations import GRAY, WIDTH, HEIGHT, SKY_BLUE, RAINY_COLOR
from Utilities import render_text_drop_shadow, get_game_font
from Components import Button
from Sprites import Player
from GameLogic import GamePlay
# from Service import MusicPlayer

ABOUT_DESC = """
My first game using python and pygame.
        'A work in progress'
----------------------------------------
CONTROLS:
    1. To move Left ----> Left Key
    2. To move right ----> Right Key
    3. To Shoot ----> SpaceBar Key
    4. To pause game ----> Esc Key
    5. Go back to main menu ----> ESC key
-----------------------------------------
"""


class Screen():
    """Main Parent Screen"""
    # pylint:disable=c-extension-no-member

    def __init__(self, main_screen: pygame.surface.Surface):
        self.main_screen = main_screen
        self.text = None
        self.heading_font = get_game_font(size=22)
        self.description_font = get_game_font(size=12)
        self.buttons = []
        self.is_game_pause = False
        self.background_color = random.choice([SKY_BLUE, RAINY_COLOR])

    def on_event(self, event):
        """Handles keyboard events"""
        # pylint: disable=no-member
        if event.type == pygame.QUIT:
            # sys.exit()
            pass

    def on_loop(self):
        """Updates on every loop"""
        pass

    def render(self, callback=None):
        """Renders"""
        pass


class AboutScreen(Screen):
    """This screen is a render of game info and developers info"""
    # pylint:disable=c-extension-no-member

    def __init__(self, main_screen: pygame.surface.Surface):
        super().__init__(main_screen)
        self.buttons = []
        self.msg = "WIP, Press Esc to go back"

    def on_event(self, event):
        """Handle events"""
        return super().on_event(event)

    def write_desc(self, screen):
        """Writes Descriptions on screen"""
        # y = 200
        # wrapped_text = textwrap.wrap(ABOUT_DESC, width=WIDTH//3)
        # lines = []
        lines = ABOUT_DESC.splitlines()
        # for line in wrapped_text:
        #     text_surface = self.description_font.render(line, True, (0, 0, 0),GRAY)  # black text
        #     # text_rect = text_surface.get_rect()
        #     # text_rect.center = (WIDTH//2 - 6, HEIGHT//3)
        #     screen.blit(text_surface, (0, y))
        #     y += self.description_font.get_height() + 5
        # pygame.display.flip()
        for i, line in enumerate(lines):
            text = self.description_font.render(line, True, (0, 0, 0), GRAY)
            screen.blit(text, (50, 130 + i * 20))

    def render(self, callback=None):
        """Renders the about page on the screen"""
        self.main_screen.fill(GRAY if GRAY else (0, 0, 0))
        text_surf = render_text_drop_shadow(
            self.heading_font, "About Game", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH//2, HEIGHT//6)
        # text_2 = self.description_font.render(
        #     f"{self.msg}", True, (0, 0, 0), GRAY)
        # text_2_rect = text_2.get_rect()
        # text_2_rect.center = (WIDTH//2 - 6, HEIGHT//3)
        self.write_desc(self.main_screen)
        text_3 = self.description_font.render(
            "Author: Nitesh Ranjitkar", True, (0, 0, 0), GRAY)
        text_3_rect = text_3.get_rect()
        text_3_rect.center = (WIDTH // 2 - 11, 9 / 10 * HEIGHT)
        self.main_screen.blit(text_surf, text_rect)
        # self.main_screen.blit(text_2, text_2_rect)
        self.main_screen.blit(text_3, text_3_rect)
        pygame.display.flip()


class MenuScreen(Screen):
    """Menu Screen"""

    def __init__(self, main_screen, music_player):
        """Construtor"""
        super().__init__(main_screen)
        self.music_player = music_player
        self.buttons: list[Button] = []
        self.start_button_txt = "Start Game"
        self.font = self.font = pygame.font.Font(
            'fonts/DepartureMonoNerdFont-Regular.otf', 22)

    def get_music_button_label(self):
        """To change the music label on the button, either play or stop"""
        if self.music_player.now_playing is True:
            return ("Stop Music", self.music_player.stop_music)
        else:
            return ("Play Music", self.music_player.play_music)

    def on_event(self, event):
        for button in self.buttons:
            button.check_click(event)

    def render(self, callback=None):
        """Draws the screen item to the screen"""
        self.main_screen.fill(SKY_BLUE if SKY_BLUE else (0, 0, 254))
        text_surf = render_text_drop_shadow(
            self.heading_font, "Main Menu", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH//2, HEIGHT//6)
        self.main_screen.blit(text_surf, text_rect)
        if self.is_game_pause:
            self.start_button_txt = "Resume"
        start_button = Button(self.start_button_txt,
                              self.main_screen.get_width()//2 - 100,
                              self.main_screen.get_height() //
                              2, 200, 60,
                              self.font, lambda: callback("play") if callback else lambda: "play")
        about_button = Button("About Game",
                              self.main_screen.get_width() // 2 -
                              100,
                              self.main_screen.get_height() // 2 - 100, 200, 60,
                              self.font,
                              lambda: callback("about") if callback else lambda: "about")

        stop_music = Button(self.get_music_button_label()[0],
                            self.main_screen.get_width()//2 - 100,
                            self.main_screen.get_height() //
                            2 - 200, 200, 60, self.font,
                            self.get_music_button_label()[1])
        self.buttons.append(about_button)
        self.buttons.append(start_button)
        self.buttons.append(stop_music)
        for button in self.buttons:
            button.draw(self.main_screen)
        # self.all_sprites.draw(self.screen)
        pygame.display.flip()


class GameScreen(Screen):
    """Screen for game"""

    def __init__(self, main_screen, music_player, score_handler):
        super().__init__(main_screen)
        self.buttons = []
        self.music_player = music_player
        self.player = Player(self.music_player)
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.callback = None
        self.score_handler = score_handler
        self.game_play = GamePlay(
            self.player, self.platforms, score_handler, self.all_sprites, self.callback)
        self.game_play.game_start_setup(self.music_player)

        # self.right_after_game_start()

    def on_event(self, event):
        # return super().on_event(event)
        if event.key == 32:
            self.game_play.fire_bullets()
            self.music_player.play_shoot_sound()

    def on_loop(self):
        self.game_play.during_loop()

    def show_score(self):
        """Displays score on screen"""
        text_surf = render_text_drop_shadow(
            self.description_font, f"Score: {self.game_play.distance_travelled}", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        # score_rect = self.score.get_rect()
        text_rect.center = (WIDTH//4, 15)
        self.main_screen.blit(text_surf, text_rect)

    def show_high_score(self):
        """Displays high score on screen"""
        text_surf = render_text_drop_shadow(
            self.description_font, f"H-score: {self.score_handler.get_high()}", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH-WIDTH//4, 15)
        self.main_screen.blit(text_surf, text_rect)

    def show_kills(self):
        """Displays the number of kills"""
        text_surf = render_text_drop_shadow(
            self.description_font, f"Kills: {self.score_handler.get_kills()}", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        # score_rect = self.score.get_rect()
        text_rect.center = (WIDTH//4, 30)
        self.main_screen.blit(text_surf, text_rect)

    def show_high_kills(self):
        """Displays number of high kills"""
        text_surf = render_text_drop_shadow(
            self.description_font,
            f"H-Kills: {self.score_handler.get_high_kills()}",
            (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        text_rect.center = (WIDTH-WIDTH//4, 30)
        self.main_screen.blit(text_surf, text_rect)

    def draw_score_bar(self):
        """Makes a Score bar on top of the game screen"""
        # pylint:disable=no-member
        translucent_surface = pygame.Surface((WIDTH, 50), pygame.SRCALPHA)
        translucent_surface.fill((255, 255, 255, 160))
        self.main_screen.blit(translucent_surface, (0, 0))
        self.show_score()
        self.show_high_score()
        self.show_kills()
        self.show_high_kills()

    def render(self, callback=None):
        self.callback = callback
        if self.player.has_player_fallen_off:
            if callback:
                callback("game_over")
                self.player.has_player_fallen_off = False
        self.main_screen.fill(
            self.background_color if self.background_color else (5, 5, 254))

        self.all_sprites.remove(self.player)
        self.all_sprites.draw(self.main_screen)
        if self.game_play.enemy:
            self.game_play.enemy.draw(self.main_screen)
        self.player.draw(self.main_screen, 20)
        # pygame.draw.rect(self.main_screen,(255,0,0),self.player.rect,2)
        self.draw_score_bar()

        pygame.display.flip()


class GameOverScreen(Screen):
    """Game over Screen definition"""
    # pylint:disable=c-extension-no-member

    def __init__(self, main_screen: pygame.surface.Surface, score_handler):
        super().__init__(main_screen)
        self.callback = None
        self.buttons = []
        self.score_handler = score_handler

    def on_event(self, event):
        # return super().on_event(event)
        if event.key == 27:
            if self.callback:
                # TODO go back to main menu
                # self.callback("menu")
                # pylint: disable=no-member

                pygame.quit()
                sys.exit()

    # @staticmethod
    def exit_game(self):
        """Exits the game"""
        # pylint: disable=no-member
        self.score_handler.save_high_score(self.score_handler.score_file_name)
        pygame.quit()
        sys.exit()

    def render(self, callback=None):
        """Renders the about page on the screen"""
        # def to_restart():
        #     if callback:
        #         print("Calling callback in gameover_screen to restart")
        #         callback("restart")
        self.callback = callback
        self.main_screen.fill(
            self.background_color if self.background_color else (5, 5, 254))
        text_surf = render_text_drop_shadow(
            self.heading_font, "Game Over", (0, 0, 0), -5, 3)
        text_rect = text_surf.get_rect()
        restart_button = Button("Restart",
                                self.main_screen.get_width()//2 - 100,
                                self.main_screen.get_height(
                                ) // 2 - 100, 200, 60,
                                self.heading_font,
                                lambda: callback("restart") if callback else "restart")
        text_rect.center = (WIDTH//2, HEIGHT//6)
        exit_button = Button("Exit",
                             self.main_screen.get_width()//2 - 100,
                             self.main_screen.get_height(
                             ) // 2 - 200, 200, 60, self.heading_font, self.exit_game)
        self.main_screen.blit(text_surf, text_rect)
        self.buttons.append(restart_button)
        self.buttons.append(exit_button)
        for button in self.buttons:
            button.draw(self.main_screen)
        pygame.display.flip()
