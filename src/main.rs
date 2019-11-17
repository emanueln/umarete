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

    fn build_human(id: usize, name: String, age: u16, female: bool, genes: Genes) -> Sim {
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
    fn food_consumption(humans: &Vec<Sim>) -> f32 {
        let mut consumed: f32 = 0.0;
        for human in humans {
            if human.alive {
                if human.age < 180 {
                    consumed += 0.1 + human.age as f32 * 0.05;
                } else {
                    consumed += 1.0;
                }
            }
        }
        return consumed
    }

    fn could_not_find_food(human: &Sim, difficulty: f32) -> bool {
        let mut dead = false;
        if human.genes.food_ability / difficulty < 20.0 {
            dead = true;
        } else if human.genes.food_ability / difficulty < 40.0 {
            if random_float_between(0.0, 3.0) >= 2.0 {
                dead = true;
            }
        }
        return dead
    }

    // Death
    fn kill(mut human: Sim) -> Sim{
        human.alive = false;
        human.partner = 0;
        return human;
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
    fn food_stage(humans: Vec<Sim>, difficulty: f32) -> Vec<Sim>{
        let mut new_humans: Vec<Sim> = Vec::new();
        for mut human in humans {
            if human.alive {
                let mut survived = true;
                if human.age >= 180 {
                    if could_not_find_food(&human, difficulty){
                        survived = false;
                    }
                } else {
                    // logic for children's survival here
                    survived = true;
                }
                if !survived {
                    human = kill(human);
                }
            }
            new_humans.push(human);
        }
        return new_humans
    }

    fn mating_stage(humans: Vec<Sim>) -> Vec<Sim> {
        let mut other_humans: Vec<Sim> = Vec::new();
        let mut single_men: Vec<Sim> = Vec::new();
        let mut single_women: Vec<Sim> = Vec::new();
        let mut return_humans: Vec<Sim> = Vec::new();
        for human in humans {
            if human.alive && human.partner == 0 && human.age >= 180 {
                if human.female {
                    single_women.push(human);
                } else {
                    single_men.push(human);
                }
            } else {
                other_humans.push(human);
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
            return_humans.push(man);
        }
        return_humans.extend(single_women);
        return_humans.extend(other_humans);
        return return_humans;
    }

    fn spend_a_month(mut humans: Vec<Sim>, biome: &Biome) -> Vec<Sim> {
        let food_difficulty = food_consumption(&humans) / biome.capacity as f32;
        humans = food_stage(humans, food_difficulty);
        humans = mating_stage(humans);
        return humans
    }

    // Logging
    fn log_update(humans: &Vec<Sim>) {
        for human in humans {
            if human.alive {
                println!("{} is alive!", human.name);
                if let Some(partner) = humans.into_iter().find(|s| s.id == human.partner) {
                   println!("Their partner is {}", partner.name);
               } else {
                   println!("So lonely...");
               }
            } else {
                println!("{} is dead!", human.name)
            }
            println!("-------------------------------");
        }
    }
    // Creating the world
    let tundra = build_biome(24);
    let mut humans: Vec<Sim> = Vec::new();
    humans.push(build_human(humans.len(), "Alice".to_string(), 200, true, build_genes(30.0, 90.0)));
    humans.push(build_human(humans.len(), "Bob".to_string(), 200, false, build_genes(40.0, 50.0)));
    humans.push(build_human(humans.len(), "Connor".to_string(), 200, false, build_genes(30.0, 30.0)));
    humans.push(build_human(humans.len(), "David".to_string(), 200, false, build_genes(60.0, 50.0)));
    humans.push(build_human(humans.len(), "Emily".to_string(), 200, true, build_genes(70.0, 10.0)));
    humans.push(build_human(humans.len(), "Felicity".to_string(), 200, true, build_genes(80.0, 60.0)));
    humans.push(build_human(humans.len(), "George".to_string(), 200, false, build_genes(30.0, 90.0)));
    humans.push(build_human(humans.len(), "Harry".to_string(), 200, false, build_genes(40.0, 50.0)));
    humans.push(build_human(humans.len(), "Isabelle".to_string(), 200, false, build_genes(30.0, 30.0)));
    humans.push(build_human(humans.len(), "Jessica".to_string(), 200, false, build_genes(60.0, 50.0)));
    humans.push(build_human(humans.len(), "Kelly".to_string(), 200, true, build_genes(70.0, 10.0)));
    humans.push(build_human(humans.len(), "Larry".to_string(), 200, false, build_genes(80.0, 60.0)));

    // Running the simulation
    humans = spend_a_month(humans, &tundra);
    humans = spend_a_month(humans, &tundra);
    humans = spend_a_month(humans, &tundra);
    humans = spend_a_month(humans, &tundra);
    humans = spend_a_month(humans, &tundra);
    log_update(&humans);
}
