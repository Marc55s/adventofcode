use itertools::Itertools;
use z3::{ast::Int, Config, Optimize, SatResult};

pub fn setup(input: &str) -> Vec<Vec<String>> {
    input
        .lines()
        .map(|line| line.split_whitespace().map(|s| s.to_string()).collect())
        .collect()
}

#[derive(Debug)]
pub struct Machine {
    pub buttons: Vec<Vec<u32>>,
    pub goal_light_state: Vec<char>,
    pub joltage_max_levels: Option<Vec<u32>>,
}
pub fn part1(input: &Vec<Vec<String>>) -> i64 {
    let mut machine_list: Vec<Machine> = Vec::new();
    for lines in input {
        let buttons = &lines[1..lines.len() - 1].to_vec();
        let char_buttons: Vec<_> = buttons
            .iter()
            .map(|s| {
                s.chars()
                    .filter(|s| s.is_ascii_digit())
                    .map(|s| s.to_digit(10).unwrap())
                    .collect::<Vec<u32>>()
            })
            .collect();

        machine_list.push(Machine {
            buttons: char_buttons,
            goal_light_state: lines[0].chars().skip(1).take(lines[0].len() - 2).collect(),
            joltage_max_levels: None,
        });
    }

    // try every button combination and get the fewest button presses
    let mut sum: i64 = 0;
    for machine in machine_list {
        let mut button_count = usize::MAX;

        // try every combination
        for len in 1..=machine.buttons.len() {
            for comb in machine.buttons.iter().combinations(len) {
                let mut light_state = vec!['.'; machine.goal_light_state.len()];

                for button in &comb {
                    for i in button.iter() {
                        if light_state[*i as usize] == '.' {
                            light_state[*i as usize] = '#'
                        } else {
                            light_state[*i as usize] = '.'
                        }
                    }
                }
                // match the goal light state
                if light_state == machine.goal_light_state && comb.len() < button_count {
                    button_count = comb.len();
                    break;
                }
            }
        }
        if button_count == usize::MAX {
            button_count = 0;
        }
        sum += button_count as i64;
    }

    sum
}

pub fn part2(input: &Vec<Vec<String>>) -> i64 {
    let mut machine_list: Vec<Machine> = Vec::new();
    for lines in input {
        let buttons = &lines[1..lines.len() - 1].to_vec();
        let char_buttons: Vec<_> = buttons
            .iter()
            .map(|s| {
                s.chars()
                    .filter(|s| s.is_ascii_digit())
                    .map(|s| s.to_digit(10).unwrap())
                    .collect::<Vec<u32>>()
            })
            .collect();

        let joltage: Vec<_> = lines[lines.len() - 1]
            .split(",")
            .map(|s| {
                let s = s.replace("{", "");
                s.replace("}", "")
            })
            .map(|s| s.parse::<u32>().unwrap())
            .collect();
        machine_list.push(Machine {
            buttons: char_buttons,
            goal_light_state: lines[0].chars().skip(1).take(lines[0].len() - 2).collect(),
            joltage_max_levels: Some(joltage),
        });
    }

    // solve the linear equation in higher dimensions
    // the issue for "normal solving" is the integer and minmimal solution constraint -> Z3
    let mut sum: i64 = 0;
    for machine in machine_list {
        let targets = machine.joltage_max_levels.unwrap();
        let buttons = machine.buttons;
        if let Some(moves) = solve_with_z3(&buttons, &targets) {
            sum += moves
        } else {
            panic!("No solution found :(");
        }
    }

    sum
}

/*
* Declarative Magic to solve higher dimensional linear equations
* Works by setting assertions and constraints and the throught the rules the solution can be found
*/

fn solve_with_z3(buttons: &[Vec<u32>], targets: &[u32]) -> Option<i64> {
    let opt = Optimize::new();

    // 1. Create variables dynamically
    // "x_0", "x_1", etc. for each button
    let x_vars: Vec<Int> = (0..buttons.len())
        .map(|i| Int::new_const(format!("x_{}", i)))
        .collect();

    // 2. Global Constraints: All presses must be >= 0
    let zero = Int::from_i64(0);
    for x in &x_vars {
        opt.assert(&x.ge(&zero));
    }

    // 3. Dynamic Constraints (The Target Equations)
    for (slot_idx, &target_val) in targets.iter().enumerate() {
        // Start a sum at 0
        let mut sum = Int::from_i64(0);

        // Find which buttons affect this slot index
        for (btn_idx, affected_indices) in buttons.iter().enumerate() {
            if affected_indices.contains(&(slot_idx as u32)) {
                // Add this button's variable to the sum
                sum = &sum + &x_vars[btn_idx];
            }
        }

        // Assertion: sum == target
        opt.assert(&sum.eq(Int::from_i64(target_val as i64)));
    }

    // 4. Objective: Minimize total presses
    // Calculate total sum of all x variables
    let total_presses = x_vars.iter().fold(Int::from_i64(0), |acc, x| acc + x);

    // Minimize Integer solutions aka button presses
    opt.minimize(&total_presses);

    // 5. Solve
    if opt.check(&[]) == SatResult::Sat {
        let model = opt.get_model().unwrap();
        // Evaluate the objective function to get the final answer
        let result = model.eval(&total_presses, true).unwrap();
        Some(result.as_i64().unwrap())
    } else {
        None
    }
}

aoc::main!(2025, 10, part1, part2);
