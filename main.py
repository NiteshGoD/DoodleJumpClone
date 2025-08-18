"""Main Game Entry point"""
import pygame
from Configurations import WIDTH, HEIGHT, FPS
from Service import ScreenManager, MusicPlayer, ScoreManager
from Utilities import resource_pathway


class DoodleJumpGame():
    """Main Game Blueprint"""

    def __init__(self):
        """Initializes the pygame"""
        # pylint: disable=no-member
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("To the Heavens")
        icon_img = pygame.image.load(resource_pathway("assets/images/icon/game_icon.png"))
        pygame.display.set_icon(icon_img)
        self.clock = pygame.time.Clock()
        self.music_player = MusicPlayer()
        self.score_handler = ScoreManager()
        self.screen_manager = ScreenManager(
            self.screen, self.music_player, self.score_handler)

    def on_event(self, event):
        """checks the events here"""
        # pylint: disable=no-member
        if event.type == pygame.QUIT:
            self.running = False
        # for button in self.buttons:
        #     button.check_click(event)
        for button in self.screen_manager.buttons:
            button.check_click(event)
        if event.type == pygame.KEYDOWN:
            self.screen_manager.on_event(event)

    def on_loop(self):
        """Runs on every loop, required mostly for updates"""
        self.screen_manager.on_loop()

    def on_cleanup(self):
        """After the main game loop is finished execute this"""
        # pylint: disable=no-member
        self.score_handler.save_high_score(self.score_handler.score_file_name)
        pygame.quit()

    def start(self):
        """Main game loop"""
        print(self.score_handler.get_high_score(
            self.score_handler.score_file_name))
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.screen_manager.render()


if __name__ == "__main__":
    game = DoodleJumpGame()
    game.start()
    game.on_cleanup()
