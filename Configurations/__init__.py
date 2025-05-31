from Utilities.check_python_version import is_python_version_greater_than_3_11
if is_python_version_greater_than_3_11():
    from .configuration import WIDTH, HEIGHT, BLUE, GRAVITY, FPS, WHITE, JUMP_STRENGTH, GREEN, SKY_BLUE, DARK_GRAY, GRAY
else:
    from .using_config_parser import WIDTH, HEIGHT, BLUE, GRAVITY, FPS, WHITE, JUMP_STRENGTH, GREEN,SKY_BLUE, DARK_GRAY, GRAY
