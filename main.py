import random
import sys

import dnd_goblins.combat as combat
from dnd_goblins.player import player
from dnd_goblins.monster import monster
import dnd_goblins.strings as strings

def job_choice():
    job = input("Which one do you want?(fighter,archer,or wizard)")
    player1 = player(job)    
    return player1



def main():
    start = input("Start a new game? (Answer 'Yes' or 'No)")
    if not start:sys.exit()
    strings.intro()
    goblin1 = monster("goblin")
    player1 = job_choice()
    res = combat.combat(player1,goblin1)
    if res == "win":
        print("You win!!!!!!!!")
        sys.exit()
    elif res == "lose":
        print("Oh no! You lose!!!!!")
        print("Try again next life!")        
        sys.exit()
if __name__ == "__main__":
    main()