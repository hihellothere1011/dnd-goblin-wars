import random
import sys

jobs = {
    "fighter" : {
        "damage" : random.randrange(100, 210, 10),
        "range" : 10,
        "hp" : 500
    },
    "archer" : {
        "damage" : random.randrange(100, 210, 10),
        "range" : 10,
        "hp" : 200
    },
    "wizard" : {
        "damage" : random.randrange(100, 210, 10),
        "range" : 10,
        "hp" : 100
    },
}

class player:
    
    def __init__(self, job):
        self.job = self.job_choice(job)
        self.hp = jobs[job]["hp"]
        self.range = jobs[job]["range"]

    def __str__(self):
        return f"A {self.job} with {self.hp} hp "
    
    def job_choice(self, job):
        if job in jobs:
            return job
        else:
            print(f"Hey! There\'s no {job} class!")
            sys.exit()

    def attack(self):
        damage = jobs[self.job]["damage"]
        return damage        
    
    def feats(self):
        damage = jobs[self.job]["damage"]
        return damage