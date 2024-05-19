import random
import sys

jobs = {
    "fighter" : {
        "damage" : {
            "start" : 100,
            "end" : 210
        },
        "feats" : {
            "start" : 130,
            "end" : 400
        },
        "range" : 10,
        "hp" : 500
    },
    "archer" : {
        "damage" : {
            "start" : 70,
            "end" : 160
        },
        "feats" : {
            "start" : 70,
            "end" : 360
        },
        "range" : 50,
        "hp" : 200
    },
    "wizard" : {
        "damage" : {
            "start" : 130,
            "end" : 250
        },
        "feats" : {
            "start" : 150,
            "end" : 510
        },
        "range" : 70,
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
        start = jobs[self.job]["damage"]["start"]
        end = jobs[self.job]["damage"]["end"]
        damage = random.randrange(start, end, 10)
        return damage        
    
    def feats(self):
        start = jobs[self.job]["feats"]["start"]
        end = jobs[self.job]["feats"]["end"]
        damage = random.randrange(start, end, 10)
        return damage