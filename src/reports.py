# Reports module

def life_expectancy(dead_sims):
    months_lived = 0
    for sim in dead_sims:
        months_lived += sim.age
    print("Average life expectancy is % years." % (months_lived / len(dead_sims) / 12))

def date_and_population(date, sims, dead_sims):
    live_sims = list(filter(lambda x: x.alive, sims))
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("%d years have passed." %  (date // 12))
    print("There are %d sims still alive." % len(live_sims))
    print("There are %d dead sims." % len(dead_sims))

def genetic_analysis(sims):
    live_sims = list(filter(lambda x: x.alive, sims))
    if len(live_sims) == 0:
        print("Everyone is dead. Genetics analysis not performed.")
    else:
        food_skill = 0
        attractiveness = 0
        libido = 0
        for sim in live_sims: 
            food_skill += sim.genes.food_skill
            attractiveness += sim.genes.attractiveness
            libido += sim.genes.libido
        print("Average food skill of the population: %s/100" % (food_skill // len(live_sims)))
        print("Average attractiveness of the population: %s/100" % (attractiveness // len(live_sims)))
        print("Average libido of the population: %s/100" % (libido // len(live_sims)))


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
