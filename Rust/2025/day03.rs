use std::cmp::Reverse;

pub fn setup(input: &str) -> Vec<String> {
    input.lines().map(|s| s.to_string()).collect()
}
pub fn part1(batteries: &[String]) -> i32 {
    let mut joltage: i32 = 0;

    for battery in batteries {
        let (digits_str, _) = battery.split_at(battery.len() - 1);
        let digits: Vec<u32> = digits_str
            .chars()
            .map(|c| c.to_digit(10).unwrap())
            .collect();

        let (idx, &max) = digits
            .iter()
            .enumerate()
            .max_by_key(|&(idx, val)| (val, Reverse(idx)))
            .unwrap();

        let remaining_slice: Vec<u32> = battery[idx + 1..]
            .chars()
            .map(|c| c.to_digit(10).unwrap())
            .collect();
        let max2 = remaining_slice.iter().max().unwrap_or(&0);

        let z = format!("{}{}", max, max2);
        joltage += z.parse::<i32>().unwrap();
    }

    joltage
}

pub fn part2(batteries: &[String]) -> u64 {
    let mut total_joltage: u64 = 0;

    for battery in batteries {
        let mut start_idx = 0;
        let mut jolt: u64 = 0;
        for i in (0..12).rev() {
            let digits_str = &battery[start_idx..battery.len() - i];
            let digits: Vec<u64> = digits_str
                .chars()
                .map(|c| c.to_digit(10).unwrap() as u64)
                .collect();

            let (idx, &max) = digits
                .iter()
                .enumerate()
                .max_by_key(|&(idx, val)| (val, Reverse(idx)))
                .unwrap();

            start_idx += idx + 1;
            jolt = jolt * 10 + max;
        }
        total_joltage += jolt;
    }
    total_joltage
}

aoc::main!(2025, 3, part1, part2);
