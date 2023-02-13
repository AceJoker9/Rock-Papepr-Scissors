from player import player
from interface import red
class Human(player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(Self):
        user_selection = red(f"""
        Please select from the options below:
        Press 1 for {self.gesture_list[0]}
        Press 2 for {self.gesture_list[1]}
        Press 3 for {self.gesture_list[2]}
        Press 4 for {self.gesture_list[3]}
        Press 5 for {self.gesture_list[4]}""")
        self.current_gesture = self.gesture_list[user_selection]
        print (f"{self.name} chose {self.current_gesture}!)")
        pass

