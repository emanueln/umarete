# Aging module

def age_sims(sims):
    return_sims = []
    for sim in sims:
        if sim.alive:
            sim.age += 1
        if sim.age > 720:
            sim.kill("old age")
        return_sims.append(sim)
    return return_sims
