# Death module

def handle_deaths(sims):
    return_sims = []
    for sim in sims:
        if sim.alive and sim.partner_id > 0 and not next(filter(lambda x: x.id == sim.partner_id, sims), None).alive:
            print("%s's partner died. They are grieving." % sim.name)
            sim.grieving = True
            sim.partner_id = 0
        elif sim.grieving:
            print("%s is no longer grieving. They will start looking for a partner." % sim.name)
            sim.grieving = False
        return_sims.append(sim)
    return return_sims   