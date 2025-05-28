from configparser import ConfigParser
import ast

config = ConfigParser()
config.sections()
config.read('config.ini')

# print(type(ast.literal_eval(config['screen']['width'])))


WIDTH, HEIGHT = ast.literal_eval(config["screen"]["width"].strip(
)), ast.literal_eval(config["screen"]["height"].strip())

# Colors
WHITE = eval(ast.literal_eval(config["color"]["white"].strip()))
GREEN = eval(ast.literal_eval(config["color"]["green"].strip()))
BLUE = eval(ast.literal_eval(config["color"]["blue"].strip()))

FPS = ast.literal_eval(config["constants"]["fps"].strip())
GRAVITY = ast.literal_eval(config["constants"]["gravity"].strip())
JUMP_STRENGTH = ast.literal_eval(config["constants"]["jump_strength"].strip())

if __name__ == "__main__":
    print("WIDTH of the screen is ", WIDTH)
    print("CURRENT FPS IS ", FPS)
    print("THE RGB value for BLUE is ", BLUE)
