fn main() {
    // Structs
    struct Genes {
        fertility: f32,
        food_ability: f32
    }

    struct Human {
        id: usize,
        partner: usize,
        name: String,
        age: u16,
        alive: bool,
        female: bool,
        genes: Genes
    }

    struct Biome {
        id: usize,
        name: String,
        capacity: u8
    }

    // Build functions
    fn build_genes(fertility: f32, food_ability: f32) -> Genes {
        Genes {
            fertility,
            food_ability
        }
    }

    fn build_human(id: usize, name: String, age: u16, female: bool, genes: Genes) -> Human {
        Human {
            id: id + 1,
            partner: 0,
            name,
            age,
            female,
            alive: true,
            genes
        }
    }

    fn build_biome(id: usize, name: String, capacity: u8) -> Biome {
        Biome {
            id,
            name,
            capacity
        }
    }
    // Food
    fn food_consumption(humans: &Vec<Human>) -> f32 {
        let mut consumed: f32 = 0.0;
        for human in humans {
            if human.age < 180 {
                consumed += 0.1 + human.age as f32 * 0.05;
            } else {
                consumed += 1.0;
            }
        }
        return consumed
    }

    fn look_for_food(mut human: Human, difficulty: f32) -> Human {
        if human.genes.food_ability / difficulty < 20.0 {
            human.alive = false
        } else if human.genes.food_ability / difficulty < 40.0 {
            if rand::random() {
                human.alive = false
            }
        }
        return human
    }

    // Passing time
    fn food_stage(humans: Vec<Human>, difficulty: f32) -> Vec<Human>{
        let mut new_humans: Vec<Human> = Vec::new();
        for human in humans {
            let mut new_human = human;
            if new_human.alive {
                new_human = look_for_food(new_human, difficulty);
                if new_human.alive {
                    new_human.age += 1;
                }
            }
            new_humans.push(new_human);
        }
        return new_humans
    }

    fn mating_stage(humans: Vec<Human>) -> Vec<Human> {
        let mut other_humans: Vec<Human> = Vec::new();
        let mut single_men: Vec<Human> = Vec::new();
        let mut single_women: Vec<Human> = Vec::new();
        let mut return_humans: Vec<Human> = Vec::new();
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
            for mut woman in &mut single_women {
                if woman.partner == 0 && rand::random() && man.partner == 0{
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

    // Logging
    fn log_update(humans: &Vec<Human>) {
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
    let tundra = build_biome(0, "Tundra".to_string(), 24);
    let mut humans: Vec<Human> = Vec::new();
    humans.push(build_human(humans.len(), "Alice".to_string(), 200, true, build_genes(50.0, 50.0)));
    humans.push(build_human(humans.len(), "Bob".to_string(), 200, false, build_genes(50.0, 50.0)));
    humans.push(build_human(humans.len(), "Connor".to_string(), 200, false, build_genes(50.0, 50.0)));
    humans.push(build_human(humans.len(), "David".to_string(), 200, false, build_genes(50.0, 50.0)));
    humans.push(build_human(humans.len(), "Emily".to_string(), 200, true, build_genes(50.0, 50.0)));
    humans.push(build_human(humans.len(), "Felicity".to_string(), 200, true, build_genes(50.0, 50.0)));

    // Running the simulation
    let food_difficulty = food_consumption(&humans) / tundra.capacity as f32;
    humans = food_stage(humans, food_difficulty);
    humans = mating_stage(humans);
    log_update(&humans);
}
