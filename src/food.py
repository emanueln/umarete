# Food module

# How much do all sims want to eat?
def total_food_desired(sims):
    total_food = 0.0
    for sim in sims:
        total_food += individual_food_desired(sim)       
    return total_food

# How much does 1 sim want to eat?
def individual_food_desired(sim):
    if sim.age < 201:
        food_desired = 0.1 + sim.age * 0.0045
    else:
        food_desired = 1.0
    return food_desired

# Adult method for getting food
def adult_get_food(sim, difficulty):
    food = sim.genes.food_skill / difficulty
    if food < 1.0:
        sim.starvation += 1.0 - food 
    else:
        sim.starvation -= food - 1.0
        if sim.starvation <= -3.0:
            sim.starvation = -3.0
    if sim.starvation > 3.0:
        sim.kill("starvation")
    return sim

# One sim looks for food
def get_food(sim, difficulty):
    if sim.age >= 201:
        sim = adult_get_food(sim, difficulty) 
    return sim
    
# Everyone looks for food
def food_stage(sims, difficulty):
    new_sims = []
    for sim in sims:
        sim = get_food(sim, difficulty)
        new_sims.append(sim)
    return new_sims