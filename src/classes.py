# Classes module
from random import seed
from random import randint
seed(1)

def random_id():
    return randint(1,10) * randint(0, 1000000000)

def random_genes():
    genes = dict()
    for gene in list_of_genes():
        genes[gene] = randint(1,100)
    gender = randint(1,100) > 51
    return Genes(gender, 0, 0, genes)

class Genes:
    def __init__(self, a, b, c, genes):
        self.female = a
        self.mother_id = b
        self.father_id = c
        self.food_skill = genes["food_skill"]
        self.attractiveness = genes["attractiveness"]
        self.libido = genes["libido"]
        self.strength = genes["strength"]
        self.agility = genes["agility"]
        self.endurance = genes["endurance"]
        self.ambition = genes["ambition"]

def list_of_genes():
    return ["food_skill", "attractiveness", "libido", "strength", "agility", "endurance", "ambition"]

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
        self.chief_id = 0
    
class Biome:
  def __init__(self, capacity):
    self.capacity = capacity
