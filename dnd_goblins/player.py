class player:
    def __init__(self, job, hp, range):
        self.job = job
        self.hp = hp
        self.range = range

    def __str__(self):
        return f"A {self.job} with {self.hp} hp "
    
    def damage(self, damage):
        self.hp -= damage
        return self.hp
    
    def feat(self):
        ""
        
    
    