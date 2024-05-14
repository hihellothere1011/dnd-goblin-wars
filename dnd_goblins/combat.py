import random


def combat(player,monster):

    while player.hp > 0 or monster.hp > 0:
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
                if distance <= player.range:
                    damage = random.randrange(10,60)
                    monster.hp -= damage
                    print(f"You just deal {damage} damage to the goblin!!")
                else:
                    print("Sorry, you can\'t reach it.")
            elif act == "feats":
                if distance <= player.range:
                    if player.job == "fighter":
                        damage = random.randrange(100,210,10)
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
                print(f"You get hit! You are now at {player.hp} hit points!")
            else:
                distance -= 20
                print(f"They moved! You are now {distance} feet far away from your enemy.")