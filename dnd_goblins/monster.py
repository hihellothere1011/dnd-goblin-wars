import random
class monster:
    def __init__(gob,type):
        gob.hp = random.randrange(50,1010,10)
        gob.range = random.randrange(10,40,10)
        gob.type = type