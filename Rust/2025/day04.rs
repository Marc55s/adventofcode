pub fn setup(input: &str) -> Vec<Vec<char>> {
    input
        .lines()
        .map(|s| s.chars().collect::<Vec<char>>())
        .collect()
}

pub fn count_accessible_by_forklift(x: i32, y: i32, input: &[Vec<char>]) -> i32 {
    let mut count_neighbours: i32 = 0;
    for i in -1..2 {
        for j in -1..2 {
            if i == 0 && j == 0
                || (x + i) as usize >= input.len()
                || (y + j) as usize >= input[0].len()
            {
                continue;
            }
            if input[(x + i) as usize][(y + j) as usize] == '@' {
                count_neighbours += 1;
            }
        }
    }
    count_neighbours
}

pub fn part1(input: &[Vec<char>]) -> i32 {
    // println!("{:?}", input);
    let mut count = 0;
    for i in 0..input.len() {
        for j in 0..input[i].len() {
            if count_accessible_by_forklift(i as i32, j as i32, input) < 4 && input[i][j] == '@' {
                count += 1;
            }
        }
    }
    count
}

pub fn part2(input: &[Vec<char>]) -> i32 {
    let mut input = input.to_owned();
    let mut rolls_of_paper_total = 0;
    loop {
        let mut removable: Vec<(usize, usize)> = Vec::new();
        for i in 0..input.len() {
            for j in 0..input[i].len() {
                if count_accessible_by_forklift(i as i32, j as i32, &input) < 4
                    && input[i][j] == '@'
                {
                    rolls_of_paper_total += 1;
                    removable.push((i, j));
                }
            }
        }

        for (x, y) in &removable {
            input[*x][*y] = '.';
        }

        if removable.is_empty() {
            break;
        }
    }

    rolls_of_paper_total
}

aoc::main!(2025, 4, part1, part2);
