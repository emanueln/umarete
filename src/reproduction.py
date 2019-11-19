# Reproduction module
import classes
import names
from random import seed
from random import randint
seed(1)

def reproduction_stage(tribe):
    return_sims = []
    new_babies = []
    fertile_women = get_fertile_women(tribe.sims)
    pregnant_women = get_pregnant_women(tribe.sims)
    for sim in tribe.sims:
        if sim in fertile_women and woman_wants_baby(sim, tribe.sims):
            if got_pregnant(sim):
                sim.pregnant = True
                baby = make_a_baby(sim, next(filter(lambda x: x.id == sim.partner_id, tribe.sims), None))
                new_babies.append(baby)
        elif sim in pregnant_women:
            babies =  list(filter(lambda x: x.genes.mother_id == sim.id, tribe.sims))
            for baby in babies:
                if baby.age == 9:
                    sim.pregnant = False
                    #print("%s gave birth to a beautiful baby named %s." % (sim.name, baby.name))
        return_sims.append(sim)
    return_sims += new_babies
    tribe.sims = return_sims

def got_pregnant(sim):
    random_number = randint(1, 100)
    chance = chance_of_getting_pregnant(sim.age) * 100
    if random_number < chance:
        return True
    else:
        return False

# Don't try for a baby if one of your existing children is starving
def woman_wants_baby(woman, sims):
    wants_baby = True
    children = list(filter(lambda x: x.genes.mother_id == woman.id and x.age < 201, sims))
    for child in children:
        if child.starvation > 0:
            wants_baby = False
    return wants_baby

# Baby making
def make_a_baby(mother, father):
    genes = genes_from_parents(mother, father)
    if genes.female:
        name = names.random_girl_name()
    else:
        name = names.random_boy_name()
    return classes.Sim(name = name, genes = genes, age=0)

def average(first, second):
    return (first + second) / 2

def genes_from_parents(mother, father):
    female = randint(1,100) > 51
    genes = dict()
    for attr, value in mother.genes.__dict__.items():
        genes[attr] = value
    for attr, value in father.genes.__dict__.items():
        genes[attr] = mutate(average(genes[attr], value))
    return classes.Genes(female, mother.id, father.id, genes)

def mutate(gene):
    if randint(1, 100) == 100:
        gene += randint(-25, 25)
        if gene < 0:
            gene = 0
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