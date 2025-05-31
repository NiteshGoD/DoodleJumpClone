"""Main Game Entry point"""
import pygame
from Configurations import WIDTH, HEIGHT, FPS
from Service import ScreenManager


class DoodleJumpGame():
    """Main Game Blueprint"""

    def __init__(self):
        """Initializes the pygame"""
        # pylint: disable=no-member
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TESTING SCREEN")
        self.clock = pygame.time.Clock()
        self.screen_manager = ScreenManager(self.screen)

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
        pygame.quit()

    def start(self):
        """Main game loop"""
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
