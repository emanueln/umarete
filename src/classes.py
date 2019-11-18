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
        
    def kill(self, cause):
        self.alive = False
        print("%s has tragically died of %s!" % (self.name, cause))

class Biome:
  def __init__(self, capacity):
    self.capacity = capacity
