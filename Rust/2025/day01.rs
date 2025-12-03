use core::f64;

pub fn setup(input: &str) -> Vec<String> {
    input.lines().map(|s| s.to_string()).collect()
}

// part1
pub fn part1(input: &Vec<String>) -> i32 {
    let mut dial_start = 50;
    let mut zeros = 0;
    for line in input {
        let amount = line[1..].parse::<i32>().unwrap();
        let dial_end = {
            if line.starts_with("L") {
                -amount
            } else {
                amount
            }
        };

        let mut a = dial_end % 100;

        if a < 0 {
            a += 100;
        }
        if dial_start + a > 99 {
            dial_start = (dial_start + a) % 100;
        } else {
            dial_start += a;
        }

        if dial_start == 0 {
            zeros += 1;
        }
    }
    zeros
}

// part2
pub fn part2(input: &Vec<String>) -> i32 {
    let mut dial_start = 50;
    let mut zeros = 0;
    for line in input {
        let amount = line[1..].parse::<i32>().unwrap();
        let (dial_end, is_right_turn) = if line.starts_with("L") { 
            (-amount, false) 
        } else { 
            (amount, true) 
        };

        let old_pos = dial_start;
        let new_pos = dial_start + dial_end;

        let crossed_zeros = if is_right_turn {
            let old_zone = f64::floor(old_pos as f64 / 100.0) as i32;
            let new_zone = f64::floor(new_pos as f64 / 100.0) as i32;
            (new_zone - old_zone).abs()
        } else {
            let old_zone = f64::floor((old_pos - 1) as f64 / 100.0) as i32;
            let new_zone = f64::floor((new_pos - 1) as f64 / 100.0) as i32;
            (old_zone - new_zone).abs()
        };

        zeros += crossed_zeros;
        dial_start = new_pos;
    }
    zeros
}

// aoc::main!(2025, 1, part1, part2[a]);
aoc::main!(2025, 1, part1, part2);
