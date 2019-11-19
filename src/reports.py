# Reports module

def life_expectancy(dead_sims):
    months_lived = 0
    for sim in dead_sims:
        months_lived += sim.age
    print("Average life expectancy is %.1f years." % (months_lived / len(dead_sims) / 12))

def causes_of_death(dead_sims):
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

def date_and_population(date, sims, dead_sims):
    live_sims = list(filter(lambda x: x.alive, sims))
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("%d years have passed." %  (date // 12))
    print("There are %d sims still alive." % len(live_sims))
    print("There are %d dead sims." % len(dead_sims))

def average_age(sims):
    total_age = 0
    if len(sims) == 0:
        print("Everyone is dead. No average age.")
    else:
        for sim in sims:
            total_age += sim.age
        print("Average age of living sims: %.1f" % (total_age / len(sims) / 12))


def genetic_analysis(sims):
    female_sims = list(filter(lambda x: x.genes.female, sims))
    male_sims = list(filter(lambda x: not x.genes.female, sims))
    if len(female_sims) == 0 or len(male_sims) == 0:
        print("Everyone is dead. Genetics analysis not performed.")
    else:
        male_food_skill = 0
        male_attractiveness = 0
        male_libido = 0
        female_food_skill = 0
        female_attractiveness = 0
        female_libido = 0
        for sim in female_sims: 
            female_food_skill += sim.genes.food_skill
            female_attractiveness += sim.genes.attractiveness
            female_libido += sim.genes.libido
        for sim in male_sims:
            male_food_skill += sim.genes.food_skill
            male_attractiveness += sim.genes.attractiveness
            male_libido += sim.genes.libido
        print("Average food skill of males: %d/100" % (male_food_skill // len(male_sims)))
        print("Average attractiveness of males: %d/100" % (male_attractiveness // len(male_sims)))
        print("Average libido of males: %d/100" % (male_libido // len(male_sims)))
        print("Average food skill of females: %d/100" % (female_food_skill // len(female_sims)))
        print("Average attractiveness of females: %d/100" % (female_attractiveness // len(female_sims)))
        print("Average libido of females: %d/100" % (female_libido // len(female_sims)))


def list_of_sims(sims):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("End of Simulation Status Log")
    for sim in sims:
        print("------------------------------")
        if sim.alive:
            print("%s is still alive and is %s years old." % (sim.name, sim.age // 12))
            if sim.partner_id > 0:
                print("Their partner is %s" % next(filter(lambda x: x.id == sim.partner_id, sims), None).name)
            else:
                print("So lonely...")
        else:
            print("%s is dead." % sim.name)
