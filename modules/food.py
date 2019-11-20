# Food module

# How much do all sims want to eat?
def total_food_desired(sims):
    total_food = 0.0
    for sim in sims:
        if sim.pregnant or len(list(filter(lambda x: x.genes.mother_id == sim.id and x.age < 35, sims))) > 0:
            child = next(filter(lambda x: x.genes.mother_id == sim.id and x.age < 35, sims), None)
            total_food += sim.mother_hunger(child)
        elif sim.age > 35: 
            total_food += sim.hunger()
    return total_food

# How much extra food do the parents have?
def mother_and_father_food(sim, sims, difficulty):
    father_food, mother_food = (0.0, 0.0)
    father = sim.father(sims)
    mother = sim.mother(sims)
    if father is not None:
        father_food = father.genes.food_skill / difficulty - 1
    if mother is not None:
        mother_food = mother.genes.food_skill / difficulty - 1
    return father_food + mother_food

# One sim looks for food
def get_food(sim, tribe, difficulty):
    if sim.age < 35:
        return sim
    food = sim.find_food(difficulty)
    if sim.age < 201:
        food += mother_and_father_food(sim, tribe.sims, difficulty)
    if food < sim.hunger():
        if tribe.food_store >= sim.hunger() - food:
            tribe.food_store -= sim.hunger() - food
        else:
            sim.starvation += sim.hunger() - food
            if sim.starvation > 3.0:
                if sim.age >= 201:
                    sim.kill(1)
                else:
                    sim.kill(3)
    else:
        sim.starvation -= food - sim.hunger()
        if sim.starvation <= -1.0:
            tribe.food_store += ((sim.starvation * -1) - 1) 
            sim.starvation = -1.0
    
# Everyone looks for food
def food_stage(tribe, difficulty):
    new_sims = []
    for sim in tribe.sims:
        get_food(sim, tribe, difficulty)
        new_sims.append(sim)
    tribe.sims = new_sims
    return tribe