use std::collections::HashMap;

pub fn setup(input: &str) -> Vec<Vec<String>> {
    input
        .lines()
        .map(|s| {
            s.split(&[':', ' '][..])
                .filter(|s| !s.is_empty())
                .map(|s| s.to_string())
                .collect::<Vec<String>>()
        })
        .collect::<Vec<Vec<String>>>()
}

pub fn dfs(graph: &HashMap<String, Vec<String>>, current: &str, end: &str, memoization: &mut HashMap<String, u64>) -> u64 {
    if current == end {
        return 1;
    }

    if memoization.contains_key(current) {
        return memoization[current];
    }

    let mut count_paths = 0;
    if let Some(edges) = graph.get(current) {
        for edge in edges {
            count_paths += dfs(graph, edge, end, memoization);
        }
    } else {
        return 0;
    }
    memoization.insert(current.to_string(), count_paths);
    count_paths
}

pub fn part1(input: &Vec<Vec<String>>) -> u64 {
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();

    for line in input {
        graph.insert(line[0].to_string(), line[1..].to_vec());
    }

    let mut memoization: HashMap<String, u64> = HashMap::new();
    dfs(&graph, "you", "out", &mut memoization)
}


pub fn part2(input: &Vec<Vec<String>>) -> u64 {
    let mut all_paths: u64 = 0;
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();

    for line in input {
        graph.insert(line[0].to_string(), line[1..].to_vec());
    }

    let start = "svr";
    let mid1 = "fft";
    let mid2 = "dac";
    let end = "out";


    let mut memoization: HashMap<String, u64> = HashMap::new();
    let count_paths1 = dfs(&graph, start, mid1, &mut memoization);
    let mut memoization: HashMap<String, u64> = HashMap::new();
    let count_paths2 = dfs(&graph, mid1, mid2, &mut memoization);
    let mut memoization: HashMap<String, u64> = HashMap::new();
    let count_paths3 = dfs(&graph, mid2, end, &mut memoization);

    all_paths += count_paths1 * count_paths2  * count_paths3 ;

    let mut memoization: HashMap<String, u64> = HashMap::new();
    let count_paths4 = dfs(&graph, start, mid2, &mut memoization);
    let mut memoization: HashMap<String, u64> = HashMap::new();
    let count_paths5 = dfs(&graph, mid2, mid1, &mut memoization);
    let mut memoization: HashMap<String, u64> = HashMap::new();
    let count_paths6 = dfs(&graph, mid1, end, &mut memoization);

    all_paths += count_paths4 * count_paths5 * count_paths6;

    all_paths
}

aoc::main!(2025, 11, part1, part2); // update input day
