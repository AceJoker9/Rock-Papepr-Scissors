import Human from human
import Player from player
from interface from interface

class Game: 
    def __init__(self):
        self.player_one = none 
        self.player_two = none
        pass

def player_rolls(self):
    self.player_one.choose_gesture()
    pass 

def round_check(self, _int_1, int_2):
    if(self.player_two.current_gesture == self.player_one.gesture_list [_int_1] or self.player_two.current_gesture == self.player_one.gesture_list[int_2]):
        self.player_one.score += 1



def compare_gests(Self):
    if self.player_one.current_gesture == self.player_two.current_gesture:
    
        elif self.player_one.current_gesture == self.player_one.gesture_list [0]:
        self.round_check(3,1)
    
    def winner_check(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            return self.player_one
        return self.player_two
    
    