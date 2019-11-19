# Mating module

# Should I approach this woman?
def consider_for_approach(man, woman):
    if woman.partner_id == 0 and (woman.genes.attractiveness >= man.genes.attractiveness - man.genes.libido):
        return True
    else:
        return False

# Is this woman interested in me?    
def seduce(man, woman):
    #print("%s attempts to seduce %s." % (man.name, woman.name))
    if man.genes.attractiveness >= woman.genes.attractiveness - woman.genes.libido:
        #print("She accepts! They are now a couple.")
        return True
    else:
        #print("She turns him away. Better luck next time.")
        return False

# Consider all women
def man_looks_for_mate(man, women):
    tried = False
    for woman in women:
        if not tried and consider_for_approach(man, woman):
            tried = True
            if seduce(man, woman):
                woman.partner_id = man.id
                man.partner_id = woman.id
    #if tried == False:
        #print("He doesn't find any women desirable enough.")
    return man, women

# All men look for mates
def mating_stage(sims):
    new_sims = []
    singles = list(filter(lambda x: (x.alive and x.partner_id == 0 and x.age >= 201 and not x.grieving), sims))
    single_women = list(filter(lambda x: x.genes.female, singles))
    if len(single_women) == 0:
        return sims
    single_men = list(filter(lambda x: not x.genes.female, singles))
    for sim in sims:
        if sim not in singles:
            new_sims.append(sim)
    for man in single_men:
        man, single_women = man_looks_for_mate(man, single_women)
        new_sims.append(man)
    new_sims = new_sims + single_women
    return new_sims
