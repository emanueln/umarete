# Mating module

# All single men look for mates
def mating_stage(sims):
    new_sims = []
    singles = list(filter(lambda x: (x.partner_id == 0 and x.age >= 201 and not x.grieving), sims))
    single_women = list(filter(lambda x: x.genes.female, singles))
    if len(single_women) == 0:
        return sims
    single_men = list(filter(lambda x: not x.genes.female, singles))
    for man in single_men:
        man, single_women = man_looks_for_mate(man, single_women)
        new_sims.append(man)
    new_sims += single_women
    for sim in sims:
        if sim not in singles:
            new_sims.append(sim)
    return new_sims

# Consider all women
def man_looks_for_mate(man, single_women):
    tried = False
    for woman in single_women:
        if not tried and consider_for_approach(man, woman):
            tried = True
            if seduce(man, woman):
                woman.partner_id = man.id
                man.partner_id = woman.id
    #if tried == False:
        #print("He doesn't find any women desirable enough.")
    return man, single_women

# Should I approach this woman?
def consider_for_approach(man, woman):
    if man.genes.libido - woman.genes.attractiveness > 0:
        return True
    else:
        return False

# Is this woman interested in me?    
def seduce(man, woman):
    #print("%s attempts to seduce %s." % (man.name, woman.name))
    if woman.genes.libido - man.genes.attractiveness > 0:
        #print("She accepts! They are now a couple.")
        return True
    else:
        #print("She turns him away. Better luck next time.")
        return False
