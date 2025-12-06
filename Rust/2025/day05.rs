pub fn setup(input: &str) -> Vec<String> {
    input.lines().map(|s| s.to_string()).collect()
}
pub fn part1(input: &[String]) -> u64 {
    let mut fresh_count = 0;
    let all_ids = input.split(|s| s.is_empty()).collect::<Vec<_>>();
    let fresh_id_ranges = all_ids.first().unwrap();
    let ingredient_ids = all_ids.last().unwrap();
    let ingredient_ids: Vec<u64> = ingredient_ids.iter().map(|s| s.parse::<u64>().unwrap()).collect();

    for ingredient_id in  ingredient_ids {
        for fresh_id in fresh_id_ranges.to_vec().iter() {
            let split: Vec<&str> = fresh_id.split('-').collect();

            if ingredient_id >= split[0].parse::<u64>().unwrap() && ingredient_id <= split[1].parse::<u64>().unwrap() {
                fresh_count += 1;
                break;
            }
        }
    }
    fresh_count
}

type Range = (u64, u64);

pub fn part2(input: &[String]) -> u64 {
    let all_ids = input.split(|s| s.is_empty()).collect::<Vec<_>>();
    let fresh_id_ranges = all_ids.first().unwrap();
    let mut ranges = fresh_id_ranges
        .iter()
        .map(|fresh_id_range| {
            let split: Vec<&str> = fresh_id_range.split('-').collect();
            (
                split[0].parse::<u64>().unwrap(),
                split[1].parse::<u64>().unwrap(),
            )
        })
        .collect::<Vec<Range>>();

    ranges.sort_by(|a, b| a.0.cmp(&b.0)); // sort range by start index

    // 1. flatten ranges
    let mut i = 0;
    loop {
        if i >= ranges.len() - 1 {
            break;
        }
        let start = ranges[i]; 
        let end = ranges[i + 1]; 
        if start.1 >= end.0 {
            if end.1 > start.1 {
                ranges[i].1 = end.1;
            }
            ranges.remove(i + 1);
            i -= 1;
        }  
        i += 1;
    }

    // 2. calc diffs and sum up
    ranges.iter().map(|r| r.1 - r.0 + 1).sum::<u64>() // important + 1 because of inclusive range
}

aoc::main!(2025, 5, part1, part2);
