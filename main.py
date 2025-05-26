import tomllib
import ast
import pygame

with open("config.toml", "rb") as f:
    DATA = tomllib.load(f)
#SCREEN
WIDTH, HEIGHT = DATA["screen"]["width"], DATA["screen"]["height"]

# Colors
WHITE = ast.literal_eval(DATA["color"]["white"])
GREEN = ast.literal_eval(DATA["color"]["green"])
BLUE = ast.literal_eval(DATA["color"]["blue"])



class DoodleJumpGame():
    """Main Game Blueprint"""
    def __init__(self):
        """initialize pygame and set necessary game parameters"""
        pygame.init()
        self.running = True
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Nitesh's Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('fonts/DepartureMonoNerdFont-Regular.otf', 22)
        
    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.running =  False

    def on_loop(self):
        """Updates"""
        pass
    
    def on_render(self):
        """Drawing on Screen"""
        self.screen.fill(WHITE)
        self.text = self.font.render("Work in progress", True, GREEN, WHITE)
        self.text_rect =self.text.get_rect()
        self.text_rect.center = (self.width//2, self.height//6)
        self.screen.blit(self.text,self.text_rect)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def start(self):
        """Main game loop"""
        while self.running:
            self.clock.tick(DATA["constants"]["fps"])
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()


if __name__ == "__main__":
    game = DoodleJumpGame()
    game.start()
    game.on_cleanup()