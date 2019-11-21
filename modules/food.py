# Food module

# How much do all sims want to eat?
def total_food_desired(tribe):
    total_food = 0.0
    sims = tribe.live_sims()
    for sim in sims:
        if sim.pregnant or len(list(filter(lambda x: x.genes.mother_id == sim.id and x.age < 35, sims))) > 0:
            child = next(filter(lambda x: x.genes.mother_id == sim.id and x.age < 35, sims), None)
            total_food += sim.mother_hunger(child)
        elif sim.age > 35: 
            total_food += sim.hunger()
    return total_food

# How much extra food do the parents have?
def mother_and_father_food(mother, father, difficulty):
    father_food, mother_food = (0.0, 0.0)
    if father is not None:
        father_food = father.genes.food_skill / difficulty - 1
    if mother is not None:
        mother_food = mother.genes.food_skill / difficulty - 1
    return father_food + mother_food

# One sim looks for food
def sim_get_food(sim, family, difficulty):
    if sim.age < 35:
        return sim
    food = sim.find_food(difficulty)
    if sim.age < 201:
        food += mother_and_father_food(family.mother, family.father, difficulty)
    if food < sim.hunger():
        if family.food_store >= sim.hunger() - food:
            family.food_store -= sim.hunger() - food
        else:
            sim.starvation += sim.hunger() - food
            if sim.starvation > 3.0:
                if sim.age >= 201:
                    sim.kill(1)
                else:
                    sim.kill(3)
    else:
        sim.starvation -= food - sim.hunger()
        if sim.starvation <= 0.0:
            family.food_store += ((sim.starvation * -1) - 1) 
            sim.starvation = 0.0

def family_get_food(family, difficulty):
    new_sims = []
    for sim in family.members():
        sim_get_food(sim, family, difficulty)
        new_sims.append(sim)
    family.set_members(new_sims)

# Everyone looks for food
def food_stage(tribe, difficulty):
    new_families = []
    for family in tribe.families:
        family_get_food(family, difficulty)
        new_families.append(family)
    tribe.families = new_families
    return tribe