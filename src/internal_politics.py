# Internal Tribal Politics module

import combat

def politics_stage(tribe):
    if tribe.chief_id == 0:
        election_process(tribe)

# Election process
def election_process(tribe): 
    candidates = list(filter(lambda x: (x.age >= 201 and not x.genes.female and x.genes.ambition > 50), tribe.sims))
    winner = tournament(candidates)
    tribe.chief_id = winner.id

# Tournament
def tournament(candidates):
    winner = candidates[0]
    rounds = number_of_rounds(candidates)
    for _ in range(rounds):
        candidates = tournament_round(candidates)
    winner = candidates[0]
    return winner

def number_of_rounds(candidates):
    rounds = 1
    for _ in range(len(candidates)):
        if rounds * 2 >= len(candidates):
            return rounds
        else:
            rounds = rounds * 2

def tournament_round(candidates):
    new_candidates = candidates
    if len(new_candidates) > 1:
        odd_number = len(new_candidates) % 2 == 1
        fights = len(new_candidates) // 2
        for x in range(fights):
            winner = combat.duel(candidates[x], candidates[x*2])
            new_candidates.append(winner)
        if odd_number:
            new_candidates.append(candidates[len(candidates) - 1])
    return new_candidates