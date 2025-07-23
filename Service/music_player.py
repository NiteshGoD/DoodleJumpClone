"""Handles music play and pause and sound control"""
import pygame


class MusicPlayer():
    def __init__(self):
        pygame.mixer.init()
        self.now_playing = False
        self.is_music_loaded = False
        self.jump_sound = pygame.mixer.Sound("assests/sound/jump_new_1.wav")
        self.game_over_sound = pygame.mixer.Sound(
            "assests/sound/game_over.wav")
        self.shoot_sound = pygame.mixer.Sound("assests/sound/shoot.wav")
        self.hit_sound = pygame.mixer.Sound("assests/sound/hit.wav")
        self.checkpoint_sound = pygame.mixer.Sound("assests/sound/checkpoint.wav")
        self.game_over_sound.set_volume(0.5)
        self.jump_sound.set_volume(0.5)
        self.shoot_sound.set_volume(0.3)
        self.hit_sound.set_volume(0.3)

    def load_music(self, music_path):
        """Loads music"""
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.3)
        self.is_music_loaded = True

    def play_music(self):
        """Plays music"""
        pygame.mixer.music.play(-1)
        self.now_playing = True

    def stop_music(self):
        """Stop the music"""
        pygame.mixer.music.stop()
        self.now_playing = False

    def unload_music(self):
        """Unloads the music"""
        pygame.mixer.music.unload()
        self.is_music_loaded = False

    def play_jump_sound(self):
        """play jump sound effect"""
        pygame.mixer.Sound.play(self.jump_sound)

    def play_game_over_sound(self):
        """play game_over sound"""
        pygame.mixer.Sound.play(self.game_over_sound)

    def play_shoot_sound(self):
        pygame.mixer.Sound.play(self.shoot_sound)

    def play_hit_sound(self):
        pygame.mixer.Sound.play(self.hit_sound)

    def control_volume(self, volumen_param):
        pass
