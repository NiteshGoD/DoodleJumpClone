"""Reads values for some constants for the game from 'config.ini'"""
from configparser import ConfigParser
import ast


def convert_to_tuple(value_string: str):
    """Converts the color RGB extracted from .ini file to tuple"""
    try:
        converted_value = ast.literal_eval(value_string)
    except ValueError as v_e:
        print(v_e)
        return
    return tuple(converted_value)


config = ConfigParser()
config.sections()
config.read("config.ini")

# print(type(ast.literal_eval(config['screen']['width'])))


WIDTH, HEIGHT = ast.literal_eval(config["screen"]["width"].strip(
)), ast.literal_eval(config["screen"]["height"].strip())

# Colors
WHITE = convert_to_tuple(ast.literal_eval(config["color"]["white"].strip()))
GREEN = convert_to_tuple(ast.literal_eval(config["color"]["green"].strip()))
BLUE = convert_to_tuple(ast.literal_eval(config["color"]["blue"].strip()))
SKY_BLUE = convert_to_tuple(ast.literal_eval(config["color"]["sky_blue"]))
DARK_GRAY = convert_to_tuple(ast.literal_eval(config["color"]["dark_gray"]))
GRAY = convert_to_tuple(ast.literal_eval(config["color"]["gray"]))
DARK_PURPLE = convert_to_tuple(
    ast.literal_eval(config["color"]["dark_purple"]))
RAINY_COLOR = convert_to_tuple(
    ast.literal_eval(config["color"]["rainy_color"])
)

FPS = ast.literal_eval(config["constants"]["fps"].strip())
GRAVITY = ast.literal_eval(config["constants"]["gravity"].strip())
JUMP_STRENGTH = ast.literal_eval(config["constants"]["jump_strength"].strip())

if __name__ == "__main__":
    print("WIDTH of the screen is ", WIDTH)
    print("CURRENT FPS IS ", FPS)
    print("THE RGB value for BLUE is ", BLUE)
