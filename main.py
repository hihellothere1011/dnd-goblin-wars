import random

from dnd_goblins.player import player
from dnd_goblins.goblins import goblin
import dnd_goblins.strings as strings

start = input("Start a new game? (Answer 'Yes' or 'No)")
if start == "Yes":
    strings.intro()
    goblin1 = goblin()
    job = input("Which one do you want?(fighter,archer,or wizard)")
    
    if job == "fighter":
        player1 = player("fighter", 200, 10)
        print(player1)
    elif job == "archer":
        player1 = player("archer", 150, 50)
        print(player1)
    elif job == "wizard":
        player1 = player("wizard", 80, 100)
        print(player1)
    else:
        pass
    while player1.hp > 0 or goblin1.hp > 0:
        distance = 100
        act = input("What do you want to do?(move,attack,feats,nothing)")
        
        if act == "move":
            direc = input("foward or backward?")
            if direc == "forward":
                distance -= 40
                print(f"You are now {distance} feet far away from your enemy.")
            elif direc == "backward":
                distance += 30
                print(f"You are now {distance} feet far away from your enemy.")
            else:
                print("What???????????")
        elif act == "attack":
            if distance <= player1.range:
                damage = random.randrange(10,60)
                goblin1.hp -= damage
                print(f"You just deal {damage} damage to the goblin!!")
            else:
                print("Sorry, you can\'t reach it.")
        elif act == "feats":
            if distance <= player1.range:
                if job == "fighter":
                    damage = random.randrange(100,210,10)
                    goblin1.hp -= damage
                    print(f"You just deal {damage} damage to the goblin!!")
            else:
                print("Sorry, you can\'t reach it.")
        elif act == "nothing":
            pass
        else:
            print("What???????????")
        if distance <= goblin1.range:
            damage = random.randrange(10,100)
            player1.hp -= damage
            print(f"You get hit! You are now at {player1.hp} hit points!")
        else:
            distance -= 20
            print(f"They moved! You are now {distance} feet far away from your enemy.")