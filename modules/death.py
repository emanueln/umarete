# Death module

def handle_deaths(tribe):
    new_dead = list(filter(lambda sim: not sim.alive, tribe.live_sims()))
    for dead in new_dead:
        if dead.id == tribe.chief_id:
            tribe.chief_id = 0
    for family in tribe.families:
        handle_family_deaths(family)

def handle_family_deaths(family):
    if family.man is not None and family.woman is not None:
        if not family.man.alive and family.woman.alive:
            family.woman.grieving = True
            family.woman.partner_id = 0
        elif not family.woman.alive and family.man.alive:
            family.man.grieving = True
            family.man.partner_id = 0
    if family.woman is not None and not family.woman.alive:
        children_under_9 = list(filter(lambda x: x.age < 9, family.children))
        for child in children_under_9:
            child.kill(2)