"""Score handling"""
# import pygame
import pickle


class ScoreManager():
    """Score Crude"""

    def __init__(self, score=0, kills=0, score_file_name="score.dat"):
        """Calculates SCore"""
        self.score = score
        self.kills = kills
        self.high_kills = 0
        self.high_score = 0
        self.score_file_name = score_file_name
        self.score_data = {}

    def update_score(self, new_score):
        """update the score if high score"""
        if new_score > self.high_score:
            self.high_score = new_score

    def update_kills(self):
        """Update the kills"""
        self.kills += 1

    def update_high_kills(self, new_kills = 0):
        """Update the high kills"""
        if new_kills == 0:
            new_kills = self.kills
        if new_kills > self.high_kills:
            self.high_kills = new_kills

    def get_high(self):
        """High score getter"""
        return self.high_score

    def get_high_kills(self):
        """High kills getter"""
        return self.high_kills

    def get_kills(self):
        """Kills getter"""
        return self.kills

    def reset_kills(self):
        """Set the kills to 0"""
        self.kills = 0

    def save_high_score(self, score_file_path: str):
        """Save high score in a file"""
        with open(score_file_path, "wb") as score_file:
            # score_file.write((str(self.high_score)).encode())
            pickle.dump({"high_score": self.high_score,
                        "high_kills": self.high_kills}, score_file)

    def get_high_score(self, score_file_path: str):
        """Read high score from a file"""
        try:
            with open(score_file_path, "rb") as score_file:
                self.score_data = pickle.load(score_file)
                high_score = self.score_data.get("high_score")
                high_kills = self.score_data.get("high_kills")
            # return high_score
            if high_score == b'0':
                self.high_score = 0
            else:
                self.high_score = int(high_score)
                self.high_kills = int(high_kills)
            return self.high_score
        except FileNotFoundError as file_not_found:
            print(file_not_found)
