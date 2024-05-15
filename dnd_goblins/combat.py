import random


def combat(player,monster):
    
    distance = 100
    while player.hp > 0 or monster.hp > 0:
            
        act = input("What do you want to do? (move,attack,feats,nothing) ")
        
        if act == "move":

            direc = input("foward or backward?")

            if direc == "forward":
                if distance - 40 > 0:
                    distance -= 40
                    print(f"You are now {distance} feet far away from your enemy.")
                elif distance - 40 <= 0:
                    distance = 0
            elif direc == "backward":
                distance += 30
                print(f"You are now {distance} feet far away from your enemy.")
            else:
                print("What???????????")

        elif act == "attack":
            if distance <= player.range:
                damage = player.attack()
                monster.hp -= damage
                print(f"You just deal {damage} damage to the goblin!!")
            else:
                print("Sorry, you can\'t reach it.")
        elif act == "feats":
            if distance <= player.range:
                damage = player.feats()
                monster.hp -= damage
                print(f"You just deal {damage} damage to the goblin!!")
            else:
                print("Sorry, you can\'t reach it.")
        elif act == "nothing":
            pass
        else:
            print("What???????????")
        
        if distance <= monster.range:
            damage = random.randrange(10,100)
            player.hp -= damage
            if player.hp > 0 :print(f"You get hit! You are now at {player.hp} hit points!")
        elif distance < 0:
            distance += 20
            print(f"They moved! You are now {distance} feet far away from your enemy.")
        else:
            distance -= 20
            print(f"They moved! You are now {distance} feet far away from your enemy.")
        
        win = "win"
        lose = "lose"
        if player.hp <= 0:
            return lose
        elif monster.hp <= 0:
            return win
        else:
            pass