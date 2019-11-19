# Reports module

def date_and_population(date, sims):
    live_sims = list(filter(lambda x: x.alive, sims))
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("%d years have passed." %  (date // 12))
    print("There are %d sims alive." % len(live_sims))

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
