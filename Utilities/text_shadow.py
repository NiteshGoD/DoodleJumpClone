import pygame


def render_text_drop_shadow(font, text, color, dx, dy, shadow_color=(127, 127, 127), shadowAlpha=127):
    """Adds some shadow to the text"""
    text_size = font.size(text)
    # pylint: disable=no-member
    surf = pygame.Surface(
        (text_size[0] + abs(dx), text_size[1] + abs(dy)), pygame.SRCALPHA)
    shadow_surf = font.render(text, True, shadow_color)
    shadow_surf.set_alpha(shadowAlpha)
    text_surf = font.render(text, True, color)
    surf.blit(shadow_surf, (max(0, dx), max(0, dy)))
    surf.blit(text_surf, (max(0, -dx), max(0, -dy)))
    return surf
