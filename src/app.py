# Classes and objects
class Genes:
    def __init__(self, a, b, c, d):
        self.food_skill = a
        self.attractiveness = b
        self.female = c
        self.libido = d

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

# Food Functions
def total_food_desired(sims):
    total_food = 0.0
    for sim in sims:
        if sim.alive: 
            total_food += individual_food_desired(sim)
            
    return total_food

def individual_food_desired(sim):
    if sim.age < 180:
        food_desired = 0.1 + sim.age * 0.05
    else:
        food_desired = 1.0
    return food_desired

def starved_to_death(sim, difficulty):
    dead = False
    food = sim.genes.food_skill / difficulty
    if food < 0.5:
        sim.starvation += food / 0.2
    else:
        sim.starvation -= food / 0.2
    if sim.starvation > 5:
        dead = True
    return dead
    
def get_food(sim, difficulty):
    if sim.age >= 180:
        dead = starved_to_death(sim, difficulty)
    else:
        # children method for getting food here
        dead = False
    if dead:
        sim.kill("starvation")
    return sim
    
# Everyone looks for food

def food_stage(sims, difficulty):
    new_sims = []
    for sim in sims:
        if sim.alive:
            sim = get_food(sim, difficulty)
        new_sims.append(sim)
    return new_sims

# Mating

def consider_for_approach(man, woman):
    if woman.partner_id == 0 and (woman.genes.attractiveness >= man.genes.attractiveness - man.genes.libido):
        return True
    else:
        return False
        
def seduce(man, woman):
    print("%s attempts to seduce %s." % (man.name, woman.name))
    if man.genes.attractiveness >= woman.genes.attractiveness - woman.genes.libido:
        print("She accepts! They are now a couple.")
        return True
    else:
        print("She turns him away. Better luck next time.")
        return False

def man_looks_for_mate(man, women):
    print("%s is looking for a potential mate." % man.name)
    tried = False
    for woman in women:
        if not tried and consider_for_approach(man, woman):
            tried = True
            if seduce(man, woman):
                woman.partner_id = man.id
                man.partner_id = woman.id
    if tried == False:
        print("He doesn't find any women desirable enough.")
    return man, women

# Everyone looks for a mate

def mating_stage(sims):
    new_sims = []
    singles = list(filter(lambda x: (x.alive and x.partner_id == 0 and x.age >= 180 and not x.grieving), sims))
    single_women = list(filter(lambda x: x.genes.female, singles))
    single_men = list(filter(lambda x: not x.genes.female, singles))
    for sim in sims:
        if sim not in singles:
            new_sims.append(sim)
    for man in single_men:
        man, single_women = man_looks_for_mate(man, single_women)
        new_sims.append(man)
    new_sims = new_sims + single_women
    return new_sims

# Handling death

def handle_deaths(sims):
    return_sims = []
    for sim in sims:
        if sim.alive and sim.partner_id > 0 and not next(filter(lambda x: x.id == sim.partner_id, sims), None).alive:
            print("%s's partner died. They are grieving." % sim.name)
            sim.grieving = True
            sim.partner_id = 0
        elif sim.grieving:
            print("%s is no longer grieving. They will start looking for a partner." % sim.name)
            sim.grieving = False
        return_sims.append(sim)
    return return_sims   

# Spend time

def spend_a_month(sims, biome):
    food_difficulty = total_food_desired(sims) / biome.capacity * 100
    sims = food_stage(sims, food_difficulty)
    sims = mating_stage(sims)
    sims = handle_deaths(sims)
    return sims
    
def spend_a_year(sims, biome, date):
    for _ in range(12):
        print("Month %s of Year %s" % (date[0] + 1, date[1] + 1))
        print("------------------------------")
        sims = spend_a_month(sims, biome) 
        date[0] += 1
    
    return sims
    
# Logging

def log_status(sims):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("End of Simulation Status Log")
    for sim in sims:
        print("------------------------------")
        if sim.alive:
            print("%s is alive!" % sim.name)
            if sim.partner_id > 0:
                print("Their partner is %s" % next(filter(lambda x: x.id == sim.partner_id, sims), None).name)
            else:
                print("So lonely...")
        else:
            print("%s is dead." % sim.name)

# Creating the world
date = [0, 0]
tundra = Biome(capacity=12)
sims = []
sims.append(Sim(id = len(sims), name= "Alice", genes=Genes(10, 30, True, 50), age=180))
sims.append(Sim(id = len(sims), name= "Bobby", genes=Genes(20, 20, False, 60), age=180))
sims.append(Sim(id = len(sims), name= "Connor", genes=Genes(30, 10, False, 70), age=180))
sims.append(Sim(id = len(sims), name= "David", genes=Genes(60, 20, False, 80), age=180))
sims.append(Sim(id = len(sims), name= "Emily", genes=Genes(50, 30, True, 90), age=180))
sims.append(Sim(id = len(sims), name= "Felicity", genes=Genes(40, 40, True, 100), age=180))
sims.append(Sim(id = len(sims), name= "George", genes=Genes(70, 50, False, 90), age=180))
sims.append(Sim(id = len(sims), name= "Harry", genes=Genes(80, 60, False, 80), age=180))
sims.append(Sim(id = len(sims), name= "Isabelle", genes=Genes(90, 70, True, 70), age=180))
sims.append(Sim(id = len(sims), name= "Jessica", genes=Genes(80, 80, True, 60), age=180))
sims.append(Sim(id = len(sims), name= "Kelly", genes=Genes(70, 90, True, 50), age=180))
sims.append(Sim(id = len(sims), name= "Larry", genes=Genes(60, 100, False, 40), age=180))

sims = spend_a_year(sims, tundra, date)
date = [0, date[1]+1]
sims = spend_a_year(sims, tundra, date)
date = [0, date[1]+1]
sims = spend_a_year(sims, tundra, date)
date = [0, date[1]+1]
log_status(sims)