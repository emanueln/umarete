# Reports module

def universal_status(sims):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("End of Simulation Status Log")
    for sim in sims:
        print("------------------------------")
        if sim.alive:
            print("%s still alive and is %s years old." % (sim.name, sim.age // 12))
            if sim.partner_id > 0:
                print("Their partner is %s" % next(filter(lambda x: x.id == sim.partner_id, sims), None).name)
            else:
                print("So lonely...")
        else:
            print("%s is dead." % sim.name)
