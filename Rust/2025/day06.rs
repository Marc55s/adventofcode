pub fn setup(input: &str) -> Vec<String> {
    input.lines().map(|s| s.to_string()).collect()
}

pub fn part1(input: &Vec<String>) -> i64 {
    let input: Vec<_> = input
        .iter()
        .map(|s| s.split_whitespace().collect::<Vec<&str>>())
        .collect();

    let operators = input.last().expect("no operators");
    let nums = &input[0..input.len() - 1];
    let transposed_nums: Vec<Vec<i64>> = (0..nums[0].len())
        .map(|i| {
            nums.iter()
                .map(|inner| inner[i].parse::<i64>().unwrap())
                .collect::<Vec<i64>>()
        })
        .collect();

    (0..operators.len())
        .map(|i| {
            if operators[i] == "+" {
                transposed_nums[i].iter().sum::<i64>()
            } else if operators[i] == "*" {
                transposed_nums[i].iter().product::<i64>()
            } else {
                0
            }
        })
        .sum::<i64>()
}

pub fn part2(input: &Vec<String>) -> i64 {
    let mut grand_total: i64 = 0;

    let op_list: Vec<_> = input
        .iter()
        .map(|s| {
            s.split(" ")
                .filter(|s| !s.is_empty())
                .collect::<Vec<&str>>()
        })
        .collect();

    let operators = op_list.last().expect("no operators");
    let number_lines = &input[0..input.len() - 1];

    let mut problem_collecter: Vec<i64> = vec![];
    let mut op_idx = operators.len() - 1;

    for k in (0..number_lines[0].len()).rev() {
        let mut problem_part_num: String = String::new();

        for line in number_lines {
            if let Some(candidate) = line.chars().nth(k) {
                if candidate.is_ascii_digit() {
                    problem_part_num.push(candidate);
                }
            }
        }

        if !problem_part_num.is_empty() {
            problem_collecter.push(problem_part_num.parse::<i64>().unwrap());
        }

        let last_column = k == 0;
        if problem_part_num.is_empty() || last_column {

            let problem_result = match operators[op_idx] {
                "+" => problem_collecter.iter().sum::<i64>(),
                "*" => problem_collecter.iter().product::<i64>(),
                _ => 0,
            };
            grand_total += problem_result;
            op_idx = op_idx.saturating_sub(1);
            problem_collecter.clear();
        }
    }

    grand_total
}

aoc::main!(2025, 6, part1, part2);
