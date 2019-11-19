# Classes module

class Genes:
    def __init__(self, a, b, c, d, e, f):
        self.food_skill = a
        self.attractiveness = b
        self.female = c
        self.libido = d
        self.mother_id = e
        self.father_id = f

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
    
    def hunger(self):
        if self.age < 201:
            hunger = 0.1 + self.age * 0.0045
        else:
            hunger = 1.0
        return hunger

    def mother_hunger(self, child):
        return 1.0 + child.hunger()

    def kill(self, cause):
        self.alive = False
        #print("%s has tragically died of %s!" % (self.name, cause))

class Biome:
  def __init__(self, capacity):
    self.capacity = capacity
