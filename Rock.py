import random 

#created the weapon choice
weapon_choice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
print (weapon_choice)

ai_weapon = random.choice(weapon_choice)
print (ai_weapon)

#defined two functions for both human player and a.i
def func1(x,y):
    x = int(input("how many human players?"))
    y = input('What is your weapon choice?')


def robot():
    t = ai_weapon
    return t

human_player = func1


#created a list/variable for the rules to the game
rules_gmae = ('scissors > paper', 'paper > rock', 'lizard > spock', 'rock > lizard', 'rock > scissors', 'spock > scissors', 'scissors > lizard', 'lizard > paper', 'paper > spock', 'spock > rock') 
