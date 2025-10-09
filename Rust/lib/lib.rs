#[macro_export]
macro_rules! main {
    // Both parts with examples
    ($year:literal, $day:literal, part1[$ex1:ident], part2[$ex2:ident]) => {
        $crate::main!(@impl $year, $day,
            Some(::std::concat!(::std::stringify!($year), "/examples/", ::std::stringify!($year), "/", ::std::stringify!($day), "/", ::std::stringify!($day), ".", ::std::stringify!($ex1))),
            Some(::std::concat!(::std::stringify!($year), "/examples/", ::std::stringify!($year), "/", ::std::stringify!($day), "/", ::std::stringify!($day), ".", ::std::stringify!($ex2)))
        );
    };

    // Part1 with example, part2 on main input
    ($year:literal, $day:literal, part1[$ex1:ident], part2) => {
        $crate::main!(@impl $year, $day,
            Some(::std::concat!(::std::stringify!($year), "/examples/", ::std::stringify!($year), "/", ::std::stringify!($day), "/", ::std::stringify!($day), ".", ::std::stringify!($ex1))),
           None::<&str> 
        );
    };

    // Part1 on main input, part2 with example
    ($year:literal, $day:literal, part1, part2[$ex2:ident]) => {
        $crate::main!(@impl $year, $day,
            None::<&str>,
            Some(::std::concat!(::std::stringify!($year), "/examples/", ::std::stringify!($year), "/", ::std::stringify!($day), "/", ::std::stringify!($day), ".", ::std::stringify!($ex2)))
        );
    };

    // Both on main input
    ($year:literal, $day:literal, part1, part2) => {
        $crate::main!(@impl $year, $day, None::<&str>, None::<&str>);
    };

    // Only part1 with example
    ($year:literal, $day:literal, part1[$ex1:ident]) => {
        $crate::main!(@impl_part1 $year, $day,
            Some(::std::concat!(::std::stringify!($year), "/examples/", ::std::stringify!($year), "/", ::std::stringify!($day), "/", ::std::stringify!($day), ".", ::std::stringify!($ex1)))
        );
    };

    // Only part1 on main input
    ($year:literal, $day:literal, part1) => {
        $crate::main!(@impl_part1 $year, $day, None::<&str>);
    };

    // Only part2 with example
    ($year:literal, $day:literal, part2[$ex2:ident]) => {
        $crate::main!(@impl_part2 $year, $day,
            Some(::std::concat!(::std::stringify!($year), "/examples/", ::std::stringify!($year), "/", ::std::stringify!($day), "/", ::std::stringify!($day), ".", ::std::stringify!($ex2)))
        );
    };

    // Only part2 on main input
    ($year:literal, $day:literal, part2) => {
        $crate::main!(@impl_part2 $year, $day, None::<&str>);
    };

    // Default: both parts on main input
    ($year:literal, $day:literal) => {
        $crate::main!(@impl $year, $day, None::<&str>, None::<&str>);
    };

    // === BOTH PARTS IMPLEMENTATION ===
    (@impl $year:literal, $day:literal, $p1_path:expr, $p2_path:expr) => {
        fn main() {
            let main_path = ::std::env::args()
                .nth(1)
                .unwrap_or_else(|| ::std::concat!($year, "/puzzles/", $day).into());
            let main_input = setup(&::std::fs::read_to_string(&main_path).expect("Main input missing"));

            let p1_input = if let Some(path) = $p1_path {
                setup(&::std::fs::read_to_string(path).expect("Part1 example missing"))
            } else {
                main_input.clone()
            };
            println!("{}", part1(&p1_input));

            if $day != 25 {
                let p2_input = if let Some(path) = $p2_path {
                    setup(&::std::fs::read_to_string(path).expect("Part2 example missing"))
                } else {
                    main_input
                };
                println!("{}", part2(&p2_input));
            }
        }

        pub fn _main() {
            let main_path = ::std::concat!($year, "/puzzles/", $day);
            let main_input = setup(&::std::fs::read_to_string(main_path).expect("Main input missing"));

            let p1_input = if let Some(path) = $p1_path {
                setup(&::std::fs::read_to_string(path).expect("Part1 example missing"))
            } else {
                main_input.clone()
            };
            print!("[{}/{:02}/1] {:<20}", $year, $day, part1(&p1_input));

            if $day != 25 {
                let p2_input = if let Some(path) = $p2_path {
                    setup(&::std::fs::read_to_string(path).expect("Part2 example missing"))
                } else {
                    main_input
                };
                print!(" [{}/{:02}/2] {}", $year, $day, part2(&p2_input));
            }
            println!();
        }
    };

    // Only Part1
    (@impl_part1 $year:literal, $day:literal, $p1_path:expr) => {
        fn main() {
            let main_path = ::std::env::args()
                .nth(1)
                .unwrap_or_else(|| ::std::concat!($year, "/puzzles/", $day).into());
            let input = if let Some(path) = $p1_path {
                setup(&::std::fs::read_to_string(path).expect("Part1 example missing"))
            } else {
                setup(&::std::fs::read_to_string(&main_path).expect("Main input missing"))
            };
            println!("{}", part1(&input));
        }

        pub fn _main() {
            let main_path = ::std::concat!($year, "/puzzles/", $day);
            let input = if let Some(path) = $p1_path {
                setup(&::std::fs::read_to_string(path).expect("Part1 example missing"))
            } else {
                setup(&::std::fs::read_to_string(main_path).expect("Main input missing"))
            };
            println!("[{}/{:02}/1] {}", $year, $day, part1(&input));
        }
    };

    // Only Part2 
    (@impl_part2 $year:literal, $day:literal, $p2_path:expr) => {
        fn main() {
            let main_path = ::std::env::args()
                .nth(1)
                .unwrap_or_else(|| ::std::concat!($year, "/puzzles/", $day).into());
            let input = if let Some(path) = $p2_path {
                setup(&::std::fs::read_to_string(path).expect("Part2 example missing"))
            } else {
                setup(&::std::fs::read_to_string(&main_path).expect("Main input missing"))
            };
            println!("{}", part2(&input));
        }

        pub fn _main() {
            let main_path = ::std::concat!($year, "/puzzles/", $day);
            let input = if let Some(path) = $p2_path {
                setup(&::std::fs::read_to_string(path).expect("Part2 example missing"))
            } else {
                setup(&::std::fs::read_to_string(main_path).expect("Main input missing"))
            };
            println!("[{}/{:02}/2] {}", $year, $day, part2(&input));
        }
    };
}
