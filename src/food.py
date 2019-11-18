# Food Functions

# How much do all sims want to eat?
def total_food_desired(sims):
    total_food = 0.0
    for sim in sims:
        if sim.alive: 
            total_food += individual_food_desired(sim)
            
    return total_food

# How much does 1 sim want to eat?
def individual_food_desired(sim):
    if sim.age < 201:
        food_desired = 0.1 + sim.age * 0.05
    else:
        food_desired = 1.0
    return food_desired

# Did the sim die?
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


# One sim looks for food
def get_food(sim, difficulty):
    if sim.age >= 201:
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