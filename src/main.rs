use std::convert::TryInto;

fn main() {
    // Structs
    struct Genes {
        fertility: f32,
        food_ability: f32
    }

    struct Human {
        id: usize,
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

    fn build_human(id: usize, name: String, female: bool, genes: Genes) -> Human {
        Human {
            id,
            name,
            age: 0,
            female,
            alive: true,
            genes
        }
    }

    // Food acquisition
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

    // Seeking a partner
    fn seek_partner() {}

    // Creating the world
    let tundra = Biome {
        name: "Tundray".to_string(),
        capacity: 30,
        id: 0
    };
    let mut humans: Vec<Human> = Vec::new();
    humans.push(build_human(humans.len(), "Alice".to_string(), true, build_genes(50.0, 50.0)));
    humans.push(build_human(humans.len(), "Bob".to_string(), true, build_genes(50.0, 50.0)));

    // Passing time
    fn pass_time(humans: Vec<Human>, difficulty: f32) -> Vec<Human>{
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

    // Logging
    fn log_update(humans: Vec<Human>) {
        for human in humans {
            if human.alive {
                println!("{} is alive!", human.name)
            } else {
                println!("{} is dead!", human.name)
            }
        }
    }

    // Running the simulation
    let difficulty: f32 = humans.len() as f32 / tundra.capacity as f32;
    humans = pass_time(humans, difficulty);
    log_update(humans);

}
