from player import Player
from random import choice

class Ai(player):
    def __init__(self, name):
        super().__init__()

    def choose_gesture(self):
        self.current_gesture = choice(self.gesture_list)
        pass


