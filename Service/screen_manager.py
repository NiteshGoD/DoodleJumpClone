"""Screen Manager"""
from typing import Literal, Union
from Screens import MenuScreen, AboutScreen, GameScreen, GameOverScreen
from .music_player import MusicPlayer

StateType = Literal["pause", "play", "game_over", "about", "menu","restart"]
# screen_type = Literal["menu", "about", "screen"]


class ScreenManager():
    """Manages the Screen in the game window"""

    def __init__(self, main_screen, music_player : MusicPlayer= MusicPlayer()):
        self.main_screen = main_screen
        self.current_state: StateType = "menu"
        self.music_player = music_player
        self.menu_screen = MenuScreen(self.main_screen,self.music_player)
        self.about_screen = AboutScreen(self.main_screen)
        self.game_screen = GameScreen(self.main_screen, music_player)
        self.game_over_screen = GameOverScreen(self.main_screen)
        self.current_screen: Union[MenuScreen, AboutScreen,
                                   GameScreen, GameOverScreen] = self.menu_screen
        self.buttons = self.current_screen.buttons
        self.count=0

    def set_state(self, state: StateType):
        """statest the current"""
        if self.current_state != state:
            self.current_state = state
            self.count += 1
            print(self.count)
            print("setting state: ", self.current_state)
            self.__set_current_screen()
            print("current_screen: ", self.current_screen)

    def on_loop(self):
        """Runs every loop"""
        if self.current_state == "play":
            self.current_screen.on_loop()
        if self.current_state == "restart":
            self.current_screen.on_loop()

    def on_event(self, event):
        if event.key == 27 and self.current_state == "play":
            self.set_state("pause")
        elif event.key == 27 and self.current_state == "about":
            self.set_state("menu")
        elif event.key == 27 and self.current_state == "restart":
            self.set_state("pause")
        self.current_screen.on_event(event)

    def __set_current_screen(self):
        if self.current_state == "pause":
            self.current_screen = self.menu_screen
            self.buttons = self.current_screen.buttons
        elif self.current_state == "play":
            self.current_screen = self.game_screen
            self.buttons = self.current_screen.buttons
        elif self.current_state == "game_over":
            self.current_screen = self.game_over_screen
            self.buttons = self.current_screen.buttons
        elif self.current_state == "about":
            self.current_screen = self.about_screen
            self.buttons = self.current_screen.buttons
        elif self.current_state == "menu":
            self.current_screen = self.menu_screen
            self.buttons = self.current_screen.buttons
        elif self.current_state == "restart":
            self.game_screen = GameScreen(self.main_screen,self.music_player)
            self.current_screen = self.game_screen
            self.buttons = self.current_screen.buttons
        else:
            self.current_screen = self.game_screen

    def render(self):
        self.current_screen.render(self.set_state)
