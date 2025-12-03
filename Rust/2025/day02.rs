type IdRange = (i64, i64);

pub fn setup(input: &str) -> Vec<IdRange> {
    let ranges: Vec<_> = input.split(",").collect();
    let formatted_ranges = ranges.iter().map(|s| {
        let (a,b) = s.trim().split_once("-").unwrap();
        (a.parse::<i64>().unwrap(),b.parse::<i64>().unwrap())
    }).collect();
    formatted_ranges
}

// part1
pub fn part1(input: &Vec<IdRange>) -> i64 {
    let mut sum = 0;
    for (a,b) in input {
        let valid_ids: i64 = (*a..=*b).into_iter().filter(|e| e.to_string().len() % 2 == 0).filter_map(|e| {
            let num_as_str = e.to_string();
            let (first, second) = num_as_str.split_at(num_as_str.len() / 2);
            if first.eq(second) {
                Some(e)
            } else {
                None
            }
        }).sum();
        sum += valid_ids;
    }
    sum
}

pub fn part2(input: &Vec<IdRange>) -> i64 {
    let mut sum = 0;
    for (a,b) in input {
        for unknown_id in  *a..=*b {
            // validate ids
            let num_as_str = unknown_id.to_string();
            let len = num_as_str.len();
            for i in 1..=len/2 {
                if len % i != 0 {
                    continue;
                }
                let two = &num_as_str[i..];
                let one = &num_as_str[0..num_as_str.len()-i];
                if one.eq(two) {
                    sum += unknown_id;
                    break;
                }
            }
        }
    }
    sum
}

aoc::main!(2025, 2, part1, part2);
