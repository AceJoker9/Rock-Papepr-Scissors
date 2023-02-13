class Gesture:
    def __init__(self, name, w1, w2, l1, l2,):
        self.name = name
        self.wins_against = [w1, w2]
        self.loses_against = [l1, l2]
        pass


class Rock(Gesture):
    def __init__(self, name, w1, w2, l1, l2):
        super().__init__('rock', 'lizard', 'scissors', 'paper', 'spock')

class Scissors(Gesture):
    def __init__(self, name, w1, w2, l1, l2):
        super().__init__('scissors', 'paper', 'lizard', 'rock', 'spock')

class Paper(Gesture):
    def __init__(self, name, w1, w2, l1, l2):
        super().__init__('paper', 'rock', 'spock', 'lizard', 'scissors')

class Lizard(Gesture):
    def __init__(self, name, w1, w2, l1, l2):
        super().__init__('lizard', 'spock', 'paper', 'rock', 'scissors')

class Spock(Gesture):
    def __init__(self, name, w1, w2, l1, l2):
        super().__init__('spock', 'scissors', 'rock', 'paper', 'lizard')

def compare(self, owner, opponent):
    if opponent.current_gesture.name == self.name:
        print ("tie!!")
    elif opponent.current_gesture.name in self.wins_against: 
        owner.score += 1
    elif opponent.current_gesture.name in self.loses_against: 
        opponent.score += 1


