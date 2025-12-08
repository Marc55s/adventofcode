use std::collections::{HashMap, HashSet};

pub fn setup(input: &str) -> Vec<Vec<char>> {
    input
        .lines()
        .map(|s| s.chars().collect::<Vec<char>>())
        .collect()
}

#[derive(Eq, Hash, PartialEq, Clone, Copy, Debug)]
pub struct Ray(i32, i32);

impl Ray {
    fn down(&self) -> Self {
        Ray(self.0 + 1, self.1)
    }
    fn left(&self) -> Self {
        Ray(self.0, self.1 - 1)
    }
    fn right(&self) -> Self {
        Ray(self.0, self.1 + 1)
    }

    fn is_splitter(&self, map: &[Vec<char>]) -> bool {
        map[self.0 as usize][self.1 as usize] == '^'
    }
}

pub fn part1(input: &[Vec<char>]) -> i32 {
    let start_idx = input[0].iter().position(|s| *s == 'S').unwrap();

    let mut ray_positions: HashSet<Ray> = HashSet::new();
    ray_positions.insert(Ray(0, start_idx as i32));
    let mut splitted = 0;

    for line in input {
        let str: String = line.iter().collect();
        if !str.contains("^") {
            continue;
        }
        for (k, dot) in line.iter().enumerate() {
            if *dot == '^' {
                let current = Ray(0, k as i32);
                let mut temp: Vec<Ray> = vec![];
                // println!("{:?}", current);
                for ray in ray_positions.clone() {
                    if current.1 == ray.1 {
                        ray_positions.remove(&ray);
                        temp.push(current.left());
                        temp.push(current.right());
                        splitted += 1;
                    }
                }
                ray_positions.extend(&mut temp.iter());
            }
        }
    }

    splitted
}

fn part2(input: &[Vec<char>]) -> u64 {
    let start_idx = input[0].iter().position(|s| *s == 'S').unwrap();
    let mut stack: Vec<(Ray, bool)> = vec![(Ray(0, start_idx as i32), false)];
    let mut cache: HashMap<Ray, u64> = HashMap::new();

    // DFS
    while let Some((current, children_processed)) = stack.pop() {
        if cache.contains_key(&current) {
            continue;
        }

        if current.0 >= input.len() as i32 - 1 {
            cache.insert(current, 1);
            continue;
        }

        if children_processed {
            let mut paths = 0;
            if current.is_splitter(input) {
                let left = current.down().left();
                let right = current.down().right();

                paths += cache.get(&left).unwrap_or(&0);
                paths += cache.get(&right).unwrap_or(&0);
            } else {
                let down = current.down();
                paths += cache.get(&down).unwrap_or(&0);
            }

            cache.insert(current, paths);
        } else {
            stack.push((current, true));

            if current.is_splitter(input) {
                stack.push((current.down().right(), false));
                stack.push((current.down().left(), false));
            } else {
                stack.push((current.down(), false));
            }
        }
    }

    let start_node = Ray(0, start_idx as i32);
    *cache.get(&start_node).unwrap_or(&0)
}

aoc::main!(2025, 7, part1, part2);
