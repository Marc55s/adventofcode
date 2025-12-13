pub fn setup(input: &str) -> Vec<String> {
    input.lines().map(|s| s.to_string()).collect()
}
pub fn part1(input: &Vec<String>) -> i32 {
    let regions: Vec<_> = input.iter().filter(|s| s.contains('x')).collect();
    let is_fitting: i32 = regions
        .iter()
        .map(|s| {
            if let Some((area, patterns)) = s.split_once(": "){
                let area: i32 = area.split("x").map(|s| s.parse::<i32>().unwrap()).product();

                let all_patterns = patterns.split_whitespace()
                    .map(|s| s.parse::<i32>().unwrap())
                    .collect::<Vec<i32>>()
                    .iter()
                    .sum::<i32>();
                
                if area >= 9 * all_patterns {
                    1
                } else {
                    0
                }
            } else {
                0
            }
        })
        .sum();
    
    is_fitting
}
pub fn part2(_input: &Vec<String>) -> i32 {
    0
}

aoc::main!(2025, 12, part1, part2); // update input day
