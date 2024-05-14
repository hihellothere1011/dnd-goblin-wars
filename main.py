import random
import sys

import dnd_goblins.combat as combat
from dnd_goblins.player import player
from dnd_goblins.monster import monster
import dnd_goblins.strings as strings

def job_choice():
    job = input("Which one do you want?(fighter,archer,or wizard)")
    
    if job == "fighter":
        player1 = player(job, 200, 10)
        print(player1)
    elif job == "archer":
        player1 = player(job, 150, 50)
        print(player1)
    elif job == "wizard":
        player1 = player(job, 80, 100)
        print(player1)
    else:
        pass
        
    return player1



def main():
    start = input("Start a new game? (Answer 'Yes' or 'No)")
    if not start:sys.exit()
    strings.intro()
    goblin1 = monster("goblin")
    player1 = job_choice()
    combat.combat(player1,goblin1)
    
        
if __name__ == "__main__":
    main()