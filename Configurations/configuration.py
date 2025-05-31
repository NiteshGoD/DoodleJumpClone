import tomllib
import ast

with open("config.toml","rb") as f:
    DATA = tomllib.load(f)

#SCREEN
WIDTH, HEIGHT = DATA["screen"]["width"], DATA["screen"]["height"]

# Colors
WHITE = ast.literal_eval(DATA["color"]["white"])
GREEN = ast.literal_eval(DATA["color"]["green"])
BLUE = ast.literal_eval(DATA["color"]["blue"])
SKY_BLUE = ast.literal_eval(DATA["color"]["sky_blue"])
DARK_GRAY = ast.literal_eval(DATA["color"]["dark_gray"])
GRAY = ast.literal_eval(DATA["color"]["gray"])

FPS = DATA["constants"]["fps"]
GRAVITY = DATA["constants"]["gravity"]
JUMP_STRENGTH = DATA["constants"]["jump_strength"]
