use std::collections::{HashMap, HashSet};

pub fn setup(input: &str) -> Vec<JunctionBox> {
    input
        .lines()
        .map(|s| {
            let result: Vec<&str> = s.split(",").collect();
            let result: Vec<i64> = result.iter().map(|s| s.parse::<i64>().unwrap()).collect();
            JunctionBox {
                x: result[0],
                y: result[1],
                z: result[2],
            }
        })
        .collect()
}

#[derive(Debug, Clone, Copy, Hash, Eq, PartialEq)]
pub struct JunctionBox {
    x: i64,
    y: i64,
    z: i64,
}

impl JunctionBox {
    fn distance(&self, other: &JunctionBox) -> i64 {
        // distance without sqrt to skip float errors
        let dx = self.x - other.x;
        let dy = self.y - other.y;
        let dz = self.z - other.z;

        dx * dx + dy * dy + dz * dz
    }
}

pub fn part1(input: &Vec<JunctionBox>) -> i64 {
    let mut distances: Vec<(i64, JunctionBox, JunctionBox)> = Vec::new(); // Sorted Map by key
    for i in 0..input.len() - 1 {
        for k in (i + 1)..input.len() {
            if i == k {
                continue;
            }
            distances.push((input[i].distance(&input[k]), input[i], input[k]));
        }
    }
    distances.sort_by_key(|(d, _, _)| *d);

    // connect together
    let mut circuits: Vec<HashSet<JunctionBox>> = Vec::new();
    const PAIRS: usize = 1000;
    for (_key, a, b) in distances.iter().take(PAIRS) {
        let matches: Vec<usize> = circuits
            .iter()
            .enumerate()
            .filter(|(_, c)| c.contains(a) || c.contains(b))
            .map(|(i, _)| i)
            .collect();
        match matches.as_slice() {
            // No intersection -> make a new circuit
            [] => {
                circuits.push(HashSet::from([*a, *b]));
            }

            // Intersects with exactly one circuit -> expand
            [i] => {
                circuits[*i].insert(*a);
                circuits[*i].insert(*b);
            }

            // Intersects with multiple circuits -> merge
            multi_indices => {
                // merge everything into the first matching circuit found.
                let primary_idx = multi_indices[0];

                // Iterate through the other indices in reverse order -> so the indices dont change
                for &idx in multi_indices[1..].iter().rev() {
                    let removed_set = circuits.remove(idx);
                    circuits[primary_idx].extend(removed_set);
                }

                circuits[primary_idx].insert(*a);
                circuits[primary_idx].insert(*b);
            }
        }
    }

    let mut circuit_lengths: Vec<i64> = circuits.iter().map(|c| c.len() as i64).collect();
    circuit_lengths.sort_unstable();
    circuit_lengths.reverse();

    circuit_lengths.iter().take(3).product::<i64>()
}
pub fn part2(input: &Vec<JunctionBox>) -> i64 {
    let mut distances: Vec<(i64, JunctionBox, JunctionBox)> = Vec::new(); // Sorted Map by key
    for i in 0..input.len() - 1 {
        for k in (i + 1)..input.len() {
            if i == k {
                continue;
            }
            distances.push((input[i].distance(&input[k]), input[i], input[k]));
        }
    }
    distances.sort_by_key(|(d, _, _)| *d);

    // connect together
    let mut pairs = 0;
    let mut circuits: Vec<HashSet<JunctionBox>> = Vec::new();
    loop {
        if let Some(entry) = distances.get(pairs) {
            let (_key, a, b) = entry;
            let matches: Vec<usize> = circuits
                .iter()
                .enumerate()
                .filter(|(_, c)| c.contains(a) || c.contains(b))
                .map(|(i, _)| i)
                .collect();
            match matches.as_slice() {
                // No intersection -> make a new circuit
                [] => {
                    circuits.push(HashSet::from([*a, *b]));
                }

                // Intersects with exactly one circuit -> expand
                [i] => {
                    circuits[*i].insert(*a);
                    circuits[*i].insert(*b);
                }

                // Intersects with multiple circuits -> merge
                multi_indices => {
                    // merge everything into the first matching circuit found.
                    let primary_idx = multi_indices[0];

                    // Iterate through the other indices in reverse order -> so the indices dont change
                    for &idx in multi_indices[1..].iter().rev() {
                        let removed_set = circuits.remove(idx);
                        circuits[primary_idx].extend(removed_set);
                    }

                    circuits[primary_idx].insert(*a);
                    circuits[primary_idx].insert(*b);
                }
            }
        }
        if circuits.len() == 1 {
            
        println!("circuits: {:?}", circuits);
        }
        pairs += 1;
        if pairs % 10 == 0 {
            println!("pairs: {}", pairs);
        }
        if pairs ==  distances.len() {
            break;
        }
    }
    0
}

aoc::main!(2025, 8, part1, part2[a]);
