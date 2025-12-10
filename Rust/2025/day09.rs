use std::cmp::{max, min};
use std::collections::HashSet;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Tile(i64, i64);

#[derive(Debug, Clone, PartialEq)]
struct VerticalWall {
    x: i64,
    y_min: i64,
    y_max: i64,
}

#[derive(Debug, Clone, PartialEq)]
struct HorizontalWall {
    y: i64,
    x_min: i64,
    x_max: i64,
}

pub fn setup(input: &str) -> Vec<Tile> {
    input
        .lines()
        .map(|s| {
            let split: Vec<_> = s.split(",").collect();
            Tile(split[0].parse().unwrap(), split[1].parse().unwrap())
        })
        .collect()
}

pub fn part1(input: &Vec<Tile>) -> i64 {
    let mut areas: Vec<i64> = Vec::new();
    for tile in input {
        for tile2 in input {
            if tile.0 == tile2.0 && tile.1 == tile2.1 {
                continue;
            }

            let diff_x = 1 + (tile.0 - tile2.0).abs();
            let diff_y = 1 + (tile.1 - tile2.1).abs();
            areas.push(i64::from(diff_x) * i64::from(diff_y));
        }
    }

    *areas.iter().max().unwrap()
}

pub fn part2(input: &Vec<Tile>) -> i64 {
    let mut v_walls = Vec::new();
    let mut h_walls = Vec::new();
    let vertex_set: HashSet<Tile> = input.iter().cloned().collect::<HashSet<Tile>>();
    for i in 0..input.len() {
        let tile = &input[i];
        let tile2 = &input[(i + 1) % input.len()];
        if tile.0 == tile2.0 && tile.1 == tile2.1 {
            continue;
        }
        if tile.0 == tile2.0 {
            v_walls.push(VerticalWall {
                x: tile.0,
                y_min: min(tile.1, tile2.1),
                y_max: max(tile.1, tile2.1),
            });
        } else {
            h_walls.push(HorizontalWall {
                y: tile.1,
                x_min: min(tile.0, tile2.0),
                x_max: max(tile.0, tile2.0),
            });
        }
    }

    let mut max_area = 0;
    for (i, t1) in input.iter().enumerate() {
        for t2 in input.iter().skip(i + 1) {
            if t1.0 == t2.0 || t1.1 == t2.1 {
                continue;
            }

            let min_x = min(t1.0, t2.0);
            let max_x = max(t1.0, t2.0);
            let min_y = min(t1.1, t2.1);
            let max_y = max(t1.1, t2.1);

            let t3 = Tile(t2.0, t1.1);
            let t4 = Tile(t1.0, t2.1);

            // Both edge tiles must be inside the tile polygon
            if !is_inside(t3, &v_walls, &vertex_set) || !is_inside(t4, &v_walls, &vertex_set) {
                continue;
            }

            if walls_intersect_rect(min_x, max_x, min_y, max_y, &v_walls, &h_walls) {
                continue;
            }
            let area = (max_x - min_x) * (max_y - min_y);
            if area > max_area {
                max_area = area;
            }
        }
    }
    max_area
}

fn is_inside(p: Tile, v_walls: &Vec<VerticalWall>, vertices: &HashSet<Tile>) -> bool {
    if vertices.contains(&p) {
        return true;
    }

    let mut intersections = 0;
    for w in v_walls {
        if w.x > p.0 && p.1 >= w.y_min && p.1 < w.y_max {
            intersections += 1;
        }
    }
    intersections % 2 != 0
}

fn walls_intersect_rect(
    min_x: i64, max_x: i64, 
    min_y: i64, max_y: i64, 
    v_walls: &Vec<VerticalWall>, 
    h_walls: &Vec<HorizontalWall>
) -> bool {
    
    for w in v_walls {
        if w.x > min_x && w.x < max_x {
            if !(w.y_max <= min_y || w.y_min >= max_y) {
                return true; // Cut detected
            }
        }
    }

    for w in h_walls {
        if w.y > min_y && w.y < max_y {
            if !(w.x_max <= min_x || w.x_min >= max_x) {
                return true; // Cut detected
            }
        }
    }

    false
}
aoc::main!(2025, 9, part1, part2[a]); // update input day
