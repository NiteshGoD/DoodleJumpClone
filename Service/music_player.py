"""Handles music play and pause and sound control"""
import pygame


class MusicPlayer():
    def __init__(self):
        pygame.mixer.init()
        self.now_playing = False
        self.is_music_loaded = False

    def load_music(self, music_path):
        pygame.mixer.music.load(music_path)
        self.is_music_loaded = True

    def play_music(self):
        pygame.mixer.music.play(-1)
        self.now_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.now_playing = False

    def unload_music(self):
        pygame.mixer.music.unload()
        self.is_music_loaded = False

        
