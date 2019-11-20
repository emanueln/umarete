# Reports module
from modules import classes

def life_expectancy(dead_sims):
    print("--------LIFE EXPECTANCY----------")
    months_lived = 0
    for sim in dead_sims:
        months_lived += sim.age
    print("Average life expectancy is %.1f years." % (months_lived / len(dead_sims) / 12))

def causes_of_death(dead_sims):
    print("--------CAUSE OF DEATH----------")
    starvation = 0
    childhood_starvation = 0
    mother_death = 0
    old_age = 0
    for sim in dead_sims:
        if sim.death_cause == 1:
            starvation += 1
        elif sim.death_cause == 2:
            mother_death += 1
        elif sim.death_cause == 3:
            childhood_starvation += 1
        elif sim.death_cause == 5:
            old_age += 1
    print("Deaths by starvation: %s" % starvation)
    print("Deaths by starvation in childhood: %s" % childhood_starvation)
    print("Deaths caused by death of mother: %s" % mother_death)
    print("Deaths from old age: %s" % old_age)

def date_and_population(date, tribe):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("%d years have passed." %  (date // 12))
    print("There are %d sims still alive." % len(tribe.sims))
    print("There are %d dead sims." % len(tribe.dead_sims))

def average_age(sims):
    print("--------AVERAGE AGE----------")
    total_age = 0
    if len(sims) == 0:
        print("Everyone is dead. No average age.")
    else:
        for sim in sims:
            total_age += sim.age
        print("Average age of living sims: %.1f" % (total_age / len(sims) / 12))


def genetic_analysis(sims):
    male_sims = list(filter(lambda x: not x.genes.female, sims))
    female_sims = list(filter(lambda x: x.genes.female, sims))
    if len(female_sims) == 0 or len(male_sims) == 0:
        print("Everyone is dead. Genetics analysis not performed.")
    else:
        male_genes = dict()
        female_genes = dict()
        for gene in classes.list_of_genes():
            male_genes[gene] = 0
            female_genes[gene] = 0
        for sim in male_sims:
           for gene in classes.list_of_genes():
                male_genes[gene] += getattr(sim.genes, gene)
        for sim in female_sims:
            for gene in classes.list_of_genes():
                female_genes[gene] += getattr(sim.genes, gene)
        print("----------MALES----------")
        for gene, value in male_genes.items():
            print("Average %s: %d" % (gene, (value // len(male_sims))))
        print("--------FEMALES----------")
        for gene, value in female_genes.items():
            print("Average %s: %d" % (gene, (value // len(female_sims))))


def list_of_sims(sims):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("End of Simulation Status Log")
    for sim in sims:
        print("------------------------------")
        print("%s is still alive and is %s years old." % (sim.name, sim.age // 12))
        if sim.partner_id > 0:
            print("Their partner is %s" % next(filter(lambda x: x.id == sim.partner_id, sims), None).name)
        else:
            print("So lonely...")