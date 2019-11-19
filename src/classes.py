# Classes module
from random import seed
from random import randint
seed(1)

def random_id():
    return randint(1,10) * randint(0, 1000000000)

class Genes:
    def __init__(self, a, b, c, d, e, f):
        self.female = a
        self.mother_id = b
        self.father_id = c
        self.food_skill = d
        self.attractiveness = e
        self.libido = f

class Sim:
    def __init__(self, name, genes, age):
        self.id = random_id()
        self.name = name
        self.genes = genes
        self.partner_id = 0
        self.age = age
        self.alive = True
        self.starvation = 0
        self.grieving = False
        self.pregnant = False
        self.death_cause = 0

    def find_food(self, difficulty):
        if self.age < 69:
            food = 0.0
        elif self.age < 201:
            food = self.genes.food_skill / difficulty * ((self.age - 69) / 132)
        else:
            food = self.genes.food_skill / difficulty
        return food

    def hunger(self):
        if self.age < 201:
            hunger = 0.1 + self.age * 0.0045
        else:
            hunger = 1.0
        return hunger

    def mother_hunger(self, child):
        return 1.0 + child.hunger()

    def father(self, sims):
        return next(filter(lambda x: x.id == self.genes.father_id, sims), None)

    def mother(self, sims):
        return next(filter(lambda x: x.id == self.genes.mother_id, sims), None)

    def kill(self, cause):
        self.alive = False
        self.death_cause = cause

class Tribe:
    def __init__(self, name, sims):
        self.id = random_id()
        self.name = name
        self.sims = sims
        self.dead_sims = []
        self.food_store = 0.0
    
    def add_dead_sims(self, sims):
        self.dead_sims += sims

    def access_food_store(self, food):
        self.food_store += food
    
class Biome:
  def __init__(self, capacity):
    self.capacity = capacity
