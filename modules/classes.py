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
        self.dexterity = genes["dexterity"]
        self.constitution = genes["constitution"]
        self.ambition = genes["ambition"]

def list_of_genes():
    return ["food_skill", "attractiveness", "libido", "strength", "dexterity", "constitution", "ambition"]

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

class Family:
    def __init__(self, name, man=None, woman=None):
        self.id = random_id()
        self.name = name
        self.man = man
        self.woman = woman
        self.children = []
        self.food_store = 0.0
    
    def member_count(self):
        return len(self.members())

    def members(self):
        members = []
        if self.man is not None:
            members.append(self.man)
        if self.woman is not None:
            members.append(self.woman)
        members += self.children
        return members
    
    def live_members(self):
        live_sims = []
        for sim in self.members():
            if sim.alive:
                live_sims.append(sim)
        return live_sims
    
    def live_member_count(self):
        return len(self.live_members())

    def set_members(self, sims):
        self.children = []
        for sim in sims:
            if sim.age >= 201:
                if sim.genes.female:
                    self.woman = sim
                else:
                    self.man = sim
            else:
                self.children.append(sim)
        
class Tribe:
    def __init__(self, name, families):
        self.id = random_id()
        self.name = name
        self.families = families
        self.food_store = 0.0
        self.chief_id = 0

    def live_sim_count(self):
        return len(self.live_sims())

    def dead_sims(self):
        return list(filter(lambda x: not x.alive, self.sims()))

    def dead_sim_count(self):
        return len(self.dead_sims())

    def sims(self):
        all_sims = []
        for family in self.families:
            all_sims += family.members()
        return all_sims

    def live_sims(self):
        all_sims = []
        for family in self.families:
            all_sims += family.live_members()
        return all_sims

    
class Biome:
  def __init__(self, capacity):
    self.capacity = capacity
