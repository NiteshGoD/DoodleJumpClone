import pygame


class ScoreCalculator():
    def __init__(self, score):
        """Calculates SCore"""
        self.score = score


    def calculate_score(self, ruler_value):
        self.score = ruler_value