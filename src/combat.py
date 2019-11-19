# Combat module

from random import seed
from random import randint
seed(1)

def roll_d20(mod):
    dice = randint(1, 20)
    return dice + mod

# 1v1
def duel(sim_1, sim_2):
    winner = 1
    sim_1_health = sim_1.genes.constitution // 5
    sim_2_health = sim_2.genes.constitution // 5
    sim_1_fatigue = 0
    sim_2_fatigue = 0
    for _ in range(0, 10):
        if roll_d20(sim_1.genes.dexterity // 20) - sim_1_fatigue > roll_d20(sim_2.genes.dexterity // 20) - sim_2_fatigue:
            sim_2_health -= sim_1.genes.strength
        else:
            sim_1_health -= sim_2.genes.strength
        sim_1_fatigue += (100 - sim_1.genes.constitution) / 100
        sim_2_fatigue += (100 - sim_2.genes.constitution) / 100
    if sim_2_health > sim_1_health:
        winner = 2
    return winner