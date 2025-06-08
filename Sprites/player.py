"""Player Definition"""
import pygame
from Configurations import WIDTH, HEIGHT, BLUE, GRAVITY, JUMP_STRENGTH


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


class SpriteSheet:
    def __init__(self, sprite_sheet):
        self.sheet = pygame.image.load(sprite_sheet)

    def get_sprites(self, x, y, width, height, direction=False):
        all_sprites = {}
        sprites = []
        for i in range(self.sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(self.sheet, (0, 0), rect)
            sprites.append(surface)

        if direction:
            all_sprites["character_right"] = sprites
            all_sprites["character_left"] = flip(sprites)
        else:
            all_sprites["character"] = sprites
        return all_sprites


class Player(pygame.sprite.Sprite):
    """Player Blueprint"""

    def __init__(self):
        super().__init__()
        self.spritesheet = SpriteSheet("assests/images/player/character.png")
        self.sprites = self.spritesheet.get_sprites(0, 0, 32, 32, True)
        self.bigger_sprites = {}
        for key, values in self.sprites.items():
            self.bigger_sprites[key] = []
            for value in values:
                self.bigger_sprites[key].append(pygame.transform.scale2x(value))
        # self.rect = pygame.Rect(WIDTH//2, HEIGHT-200,32,32)
        self.image = self.bigger_sprites["character_right"][0]
        original_rect = self.image.get_rect()
        original_rect.center = (WIDTH//2, HEIGHT-200)
        # self.player_rect.center = (WIDTH // 2, HEIGHT - 200)
        # player_rect_center = self.player_rect.center
        # self.rect = pygame.Rect(self.player_rect.x,0,32,32)
        self.rect = original_rect.inflate(-35, -16)
        self.rect.center = original_rect.center

        # self.hitbox = (self.player_rect.x -19, self.player_rect.y-5, 32,32)
        self.vel_y = 0
        self.direction = "right"
        self.has_player_fallen_off = False
        self.jumping_status = "jumping"
        self.reference = self.rect.y

    def change_sprite_image(self):
        if self.jumping_status == "jumping":
            self.image = self.bigger_sprites["character_"+self.direction][5]
        if self.jumping_status == "falling":
            self.image = self.bigger_sprites["character_"+self.direction][8]
        if self.jumping_status == "landed":
            self.image = self.bigger_sprites["character_"+self.direction][11]
        if self.jumping_status == "maximum_height":
            self.image = self.bigger_sprites["character_"+self.direction][6]

    def update(self):
        """Run this every game loop iteration"""
        self.vel_y += GRAVITY
        if self.vel_y > 0:
            self.jumping_status = "falling"
        elif self.vel_y == 0:
            self.jumping_status = "maximum_height"
        elif self.vel_y == JUMP_STRENGTH:
            self.jumping_status = "landed"
        else:
            self.jumping_status = "jumping"
        self.rect.y += self.vel_y

        keys = pygame.key.get_pressed()
        # pylint: disable=no-member
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.direction = "left"
            # if self.rect.y > self.reference:
            #     self.image = self.sprites["character_left"][8]
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.direction = "right"
            # if self.rect.y > self.reference:
            #     self.image = self.sprites["character_left"][8]

        # Wrap around screen
        if self.rect.right > WIDTH:
            self.rect.left = 0
        elif self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.has_player_fallen_off = True
            print("player has fallen off ", self.has_player_fallen_off)

        # self.reference = self.rect.y
        self.change_sprite_image()

    def draw(self, win, offset_x):
        # self.sprite = self.sprites["character"]
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y-16))
