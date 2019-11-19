# Classes module

class Genes:
    def __init__(self, a, b, c, d, e, f):
        self.female = a
        self.mother_id = b
        self.father_id = c
        self.food_skill = d
        self.attractiveness = e
        self.libido = f

class Sim:
    def __init__(self, id, name, genes, age):
        self.id = id + 1
        self.name = name
        self.genes = genes
        self.partner_id = 0
        self.age = age
        self.alive = True
        self.starvation = 0
        self.grieving = False
        self.pregnant = False
        self.death_cause = 0

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

class Biome:
  def __init__(self, capacity):
    self.capacity = capacity
