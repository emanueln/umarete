# Reproduction module
import classes
import names
from random import seed
from random import randint
seed(1)

# Baby making
def make_a_baby(mother, father):
    id = randint(1, 100) * randint(1, 1000000000000)
    genes = genes_from_parents(mother, father)
    if genes.female:
        name = names.random_girl_name()
    else:
        name = names.random_boy_name()
    return classes.Sim(id, name = name, genes = genes, age=0)

def average(first, second):
    return (first + second) / 2

def genes_from_parents(mother, father):
    female = randint(1,100) > 51
    food_skill = mutate(average(mother.genes.food_skill, father.genes.food_skill))
    attractiveness = mutate(average(mother.genes.attractiveness, father.genes.attractiveness))
    libido = mutate(average(mother.genes.libido, father.genes.libido))
    return classes.Genes(food_skill, attractiveness, female, libido, mother.id, father.id)

def mutate(gene):
    return gene

def chance_of_getting_pregnant(age):
    if age <= 273:
        return 0.25
    elif age <= 369:
        return 0.25 - 0.0005 * (age - 273)
    else:   
        return 0.20 - 0.001 * (age - 369)

def get_fertile_women(sims):
    return list(filter(lambda x: (
        x.starvation <= 0 and 
        x.partner_id > 0 and 
        x.age < 561 and 
        not x.pregnant and 
        x.genes.female), sims))

def get_pregnant_women(sims):
    return list(filter(lambda x: (x.pregnant), sims))

def reproduction_stage(sims):
    return_sims = []
    new_babies = []
    fertile_women = get_fertile_women(sims)
    pregnant_women = get_pregnant_women(sims)
    for sim in sims:
        if sim in fertile_women:
            if randint(0, 100) <= chance_of_getting_pregnant(sim.age) * 100:
                sim.pregnant = True
                baby = make_a_baby(sim, next(filter(lambda x: x.id == sim.partner_id, sims), None))
                new_babies.append(baby)
        elif sim in pregnant_women:
            babies =  list(filter(lambda x: x.genes.mother_id == sim.id, sims))
            for baby in babies:
                if baby.age == 9:
                    sim.pregnant = False
                    #print("%s gave birth to a beautiful baby named %s." % (sim.name, baby.name))
        return_sims.append(sim)
    return_sims += new_babies
    return return_sims