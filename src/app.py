# Imports
import food
import mating
import reports 
import aging
import death
import classes
import names
import reproduction
import combat
import internal_politics

# Setting up random number generator
from random import seed
from random import randint
seed(1)

# Create semi-random sims
def random_sim():
    genes = classes.random_genes()
    if genes.female:
        name = names.random_girl_name()
    else:
        name = names.random_boy_name()
    return classes.Sim(name = name, genes = genes, age=201)

# Spend time
def spend_a_month(tribe, biome):
    food_difficulty = food.total_food_desired(tribe.sims) / biome.capacity * 100
    food.food_stage(tribe, food_difficulty)
    death.handle_deaths(tribe)
    reproduction.reproduction_stage(tribe)
    mating.mating_stage(tribe.sims)
    aging.age_sims(tribe.sims)
    death.handle_deaths(tribe)
    internal_politics.politics_stage(tribe)
    
def spend_a_year(tribe, biome, date):
    for _ in range(12):
        spend_a_month(tribe, biome)
        date += 1
    return date
    
# Creating the world from user input
print("What should the carrying capacity be?")
try:
    capacity = int(input())
except ValueError:
    capacity = 20
print("What should the starting population be?")
try:
    starting_population = int(input())
except ValueError:
    starting_population = 12
print("How many years should we simulate?")
try:
    sim_length = int(input())
except ValueError:
    sim_length = 100

date = 0
tundra = classes.Biome(capacity=capacity)

# Generate x sims to seed the world
sims = []
for _ in range(starting_population):
    sims.append(random_sim())
# Assign them to a tribe
tribe = classes.Tribe(name="First Tribe", sims = sims)

# Run simulation for x years
for _ in range(sim_length):
    date = spend_a_year(tribe, tundra, date)

# Give status report at the end
reports.date_and_population(date, tribe)
reports.average_age(tribe.sims)
reports.genetic_analysis(tribe.sims)
if len(tribe.dead_sims) > 0:    
    reports.life_expectancy(tribe.dead_sims)
    reports.causes_of_death(tribe.dead_sims)