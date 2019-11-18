# Imports
import food
import mating
import reports 
import aging
import death
import classes
import names

# Setting up random number generator
from random import seed
from random import randint
seed(1)

# Create semi-random sims

def random_boy_name():
    index = randint(0, 39)
    return names.boy_names[index]

def random_girl_name():
    index = randint(0, 39)
    return names.girl_names[index]

def random_genes():
    gene_numbers = []
    for _ in range(4):
        gene_numbers.append(randint(1,100))
    gender = gene_numbers[2] > 51
    return classes.Genes(gene_numbers[0], gene_numbers[1], gender, gene_numbers[3], 0, 0)

def random_sim(id):
    genes = random_genes()
    if genes.female:
        name = random_girl_name()
    else:
        name = random_boy_name()
    return classes.Sim(id = id, name = name, genes = genes, age=201)

# Spend time

def spend_a_month(sims, biome):
    food_difficulty = food.total_food_desired(sims) / biome.capacity * 100
    sims = food.food_stage(sims, food_difficulty)
    sims = mating.mating_stage(sims)
    sims = death.handle_deaths(sims)
    sims = aging.age_sims(sims)
    return sims
    
def spend_a_year(sims, biome, date):
    for _ in range(12):
        print("------------------------------")
        print("Month %s of Year %s" % (date % 12 + 1, date // 12 + 1))
        sims = spend_a_month(sims, biome) 
        date += 1
        print("------------------------------")
    return sims, date
    
# Creating the world
date = 0
tundra = classes.Biome(capacity=12)
sims = []

# Generate 12 sims
for _ in range(12):
    sims.append(random_sim(len(sims) + 1))

# Run 5 years of simulation
for _ in range(5):
    sims, date = spend_a_year(sims, tundra, date)

reports.universal_status(sims)