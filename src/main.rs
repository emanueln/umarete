use rand::Rng;

fn main() {
    // RNG
    fn random_float_between(a: f32, b: f32) -> f32 {
        return rand::thread_rng().gen_range(a, b)
    }
    // Structs
    struct Genes {
        food_ability: f32,
        attractiveness: f32
    }

    struct Sim {
        id: usize,
        partner: usize,
        name: String,
        age: u16,
        alive: bool,
        female: bool,
        genes: Genes
    }

    struct Biome {
        capacity: u8
    }

    // Build functions
    fn build_genes(food_ability: f32, attractiveness: f32) -> Genes {
        Genes {
            food_ability,
            attractiveness
        }
    }

    fn build_sim(id: usize, name: String, age: u16, female: bool, genes: Genes) -> Sim {
        Sim {
            id: id + 1,
            partner: 0,
            name,
            age,
            female,
            alive: true,
            genes
        }
    }

    fn build_biome(capacity: u8) -> Biome {
        Biome {
            capacity
        }
    }

    // Food
    fn food_consumption(sim: &Vec<Sim>) -> f32 {
        let mut consumed: f32 = 0.0;
        for sim in sim {
            if sim.alive {
                if sim.age < 180 {
                    consumed += 0.1 + sim.age as f32 * 0.05;
                } else {
                    consumed += 1.0;
                }
            }
        }
        return consumed
    }

    fn could_not_find_food(sim: &Sim, difficulty: f32) -> bool {
        let mut dead = false;
        if sim.genes.food_ability / difficulty < 20.0 {
            dead = true;
        } else if sim.genes.food_ability / difficulty < 40.0 {
            if random_float_between(0.0, 3.0) >= 2.0 {
                dead = true;
            }
        }
        return dead
    }

    // Death
    fn kill(mut sim: Sim) -> Sim{
        sim.alive = false;
        sim.partner = 0;
        return sim;
    }

    // Mating
    fn consider_for_mating(man: &Sim, woman: &Sim) -> bool {
        let desire = random_float_between(1.0, 5.0);
        if woman.partner == 0 &&
        woman.genes.attractiveness >= man.genes.attractiveness / desire &&
        man.partner == 0 &&
        rand::random(){
            return true
        } else {
            return false
        }
    }

    // Passing time
    fn food_stage(sims: Vec<Sim>, difficulty: f32) -> Vec<Sim>{
        let mut new_sims: Vec<Sim> = Vec::new();
        for mut sim in sims {
            if sim.alive {
                let mut survived = true;
                if sim.age >= 180 {
                    if could_not_find_food(&sim, difficulty){
                        survived = false;
                    }
                } else {
                    // logic for children's survival here
                    survived = true;
                }
                if !survived {
                    sim = kill(sim);
                }
            }
            new_sims.push(sim);
        }
        return new_sims
    }

    fn mating_stage(sims: Vec<Sim>) -> Vec<Sim> {
        let mut other_sims: Vec<Sim> = Vec::new();
        let mut single_men: Vec<Sim> = Vec::new();
        let mut single_women: Vec<Sim> = Vec::new();
        let mut return_sims: Vec<Sim> = Vec::new();
        for sim in sims {
            if sim.alive && sim.partner == 0 && sim.age >= 180 {
                if sim.female {
                    single_women.push(sim);
                } else {
                    single_men.push(sim);
                }
            } else {
                other_sims.push(sim);
            }
        }
        for mut man in single_men {
            let mut tried = false;
            for mut woman in &mut single_women {
                if !tried && consider_for_mating(&man, woman){
                    tried = true;
                    woman.partner = man.id;
                    man.partner = woman.id;
                }
            }
            return_sims.push(man);
        }
        return_sims.extend(single_women);
        return_sims.extend(other_sims);
        return return_sims;
    }

    fn spend_a_month(mut sims: Vec<Sim>, biome: &Biome) -> Vec<Sim> {
        let food_difficulty = food_consumption(&sims) / biome.capacity as f32;
        sims = food_stage(sims, food_difficulty);
        sims = mating_stage(sims);
        return sims
    }

    // Logging
    fn log_update(sims: &Vec<Sim>) {
        for sim in sims {
            if sim.alive {
                println!("{} is alive!", sim.name);
                if let Some(partner) = sims.into_iter().find(|s| s.id == sim.partner) {
                   println!("Their partner is {}", partner.name);
               } else {
                   println!("So lonely...");
               }
            } else {
                println!("{} is dead!", sim.name)
            }
            println!("-------------------------------");
        }
    }
    // Creating the world
    let tundra = build_biome(12);
    let mut sims: Vec<Sim> = Vec::new();
    sims.push(build_sim(sims.len(), "Alice".to_string(), 200, true, build_genes(30.0, 90.0)));
    sims.push(build_sim(sims.len(), "Bobby".to_string(), 200, false, build_genes(100.0, 5.0)));
    sims.push(build_sim(sims.len(), "Connor".to_string(), 200, false, build_genes(30.0, 30.0)));
    sims.push(build_sim(sims.len(), "David".to_string(), 200, false, build_genes(60.0, 50.0)));
    sims.push(build_sim(sims.len(), "Emily".to_string(), 200, true, build_genes(70.0, 10.0)));
    sims.push(build_sim(sims.len(), "Felicity".to_string(), 200, true, build_genes(80.0, 60.0)));
    sims.push(build_sim(sims.len(), "George".to_string(), 200, false, build_genes(30.0, 90.0)));
    sims.push(build_sim(sims.len(), "Harry".to_string(), 200, false, build_genes(40.0, 50.0)));
    sims.push(build_sim(sims.len(), "Isabelle".to_string(), 200, false, build_genes(30.0, 30.0)));
    sims.push(build_sim(sims.len(), "Jessica".to_string(), 200, false, build_genes(60.0, 50.0)));
    sims.push(build_sim(sims.len(), "Kelly".to_string(), 200, true, build_genes(70.0, 10.0)));
    sims.push(build_sim(sims.len(), "Larry".to_string(), 200, false, build_genes(80.0, 60.0)));

    // Running the simulation
    sims = spend_a_month(sims, &tundra);
    sims = spend_a_month(sims, &tundra);
    sims = spend_a_month(sims, &tundra);
    sims = spend_a_month(sims, &tundra);
    sims = spend_a_month(sims, &tundra);
    log_update(&sims);
}
