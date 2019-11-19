# Imports
import food
import mating
import reports 
import aging
import death
import classes
import names
import reproduction

# Setting up random number generator
from random import seed
from random import randint
seed(1)

# Create semi-random sims
def random_genes():
    gene_numbers = []
    for _ in range(4):
        gene_numbers.append(randint(1,100))
    gender = gene_numbers[2] > 51
    return classes.Genes(gender ,0 , 0, gene_numbers[0], gene_numbers[1], gene_numbers[3])

def random_sim(id):
    genes = random_genes()
    if genes.female:
        name = names.random_girl_name()
    else:
        name = names.random_boy_name()
    return classes.Sim(id = id, name = name, genes = genes, age=201)

# Spend time
def spend_a_month(sims, dead_sims, biome):
    food_difficulty = food.total_food_desired(sims) / biome.capacity * 100
    sims = food.food_stage(sims, food_difficulty)
    sims, dead_sims = death.handle_deaths(sims, dead_sims)
    sims = reproduction.reproduction_stage(sims)
    sims = mating.mating_stage(sims)
    sims = aging.age_sims(sims)
    sims, dead_sims = death.handle_deaths(sims, dead_sims)
    return sims, dead_sims
    
def spend_a_year(sims, dead_sims, biome, date):
    for _ in range(12):
        #print("------------------------------")
        #print("Month %s of Year %s" % (date % 12 + 1, date // 12 + 1))
        sims, dead_sims = spend_a_month(sims, dead_sims, biome) 
        date += 1
        #print("------------------------------")
    return sims, dead_sims, date
    
# Creating the world
date = 0
tundra = classes.Biome(capacity=200)
sims = []
dead_sims = []

# Generate x sims to seed the world
for _ in range(12):
    sims.append(random_sim(randint(1,10) * randint(0, 1000000000)))

# Run simulation for x years
for _ in range(150):
    sims, dead_sims, date = spend_a_year(sims, dead_sims, tundra, date)

reports.date_and_population(date, sims, dead_sims)
reports.average_age(sims)
reports.genetic_analysis(sims)
if len(dead_sims) > 0:    
    reports.life_expectancy(dead_sims)
    reports.causes_of_death(dead_sims)