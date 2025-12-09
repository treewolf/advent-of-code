use std::collections::HashSet;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");
    let grid: Vec<String> = contents.trim().split('\n').map(|s| s.to_string()).collect();

    let split_count = simulate_tachyon_beams(&grid);
    println!("Part 1 splits: {}", split_count);

    let timeline_count = count_timelines(&grid);
    println!("Part 2 timelines: {}", timeline_count);
}

fn simulate_tachyon_beams(grid: &[String]) -> usize {
    let (start_row, start_col) = find_starting_position(grid);

    let mut beams = vec![start_col];
    let mut total_splits = 0;
    let mut current_row = start_row + 1;

    while current_row < grid.len() && !beams.is_empty() {
        let mut new_beams = Vec::new();
        let mut seen_columns = HashSet::new();

        for &col in &beams {
            let cell = grid[current_row].chars().nth(col).unwrap();

            match cell {
                '^' => {
                    total_splits += 1;

                    //left
                    if col > 0 && !seen_columns.contains(&(col - 1)) {
                        new_beams.push(col - 1);
                        seen_columns.insert(col - 1);
                    }

                    //right
                    if col + 1 < grid[current_row].len() && !seen_columns.contains(&(col + 1)) {
                        new_beams.push(col + 1);
                        seen_columns.insert(col + 1);
                    }
                }
                '.' | 'S' => {
                    if !seen_columns.contains(&col) {
                        new_beams.push(col);
                        seen_columns.insert(col);
                    }
                }
                _ => {}
            }
        }

        beams = new_beams;
        current_row += 1;
    }

    total_splits
}

fn find_starting_position(grid: &[String]) -> (usize, usize) {
    for (i, row) in grid.iter().enumerate() {
        if let Some(j) = row.chars().position(|c| c == 'S') {
            return (i, j);
        }
    }
    (0, 0)
}

fn count_timelines(grid: &[String]) -> usize {
    let (start_row, start_col) = find_starting_position(grid);
    let last_row = grid.len() - 1;

    let mut dp = vec![vec![0u64; grid[0].len()]; grid.len()];

    dp[start_row][start_col] = 1;

    for row in start_row..last_row {
        for col in 0..grid[row].len() {
            if dp[row][col] == 0 {
                continue;
            }

            let cell = grid[row].chars().nth(col).unwrap();

            if cell == '^' {
                //left
                if col > 0 {
                    dp[row + 1][col - 1] += dp[row][col];
                }
                //right
                if col + 1 < grid[row].len() {
                    dp[row + 1][col + 1] += dp[row][col];
                }
            } else {
                dp[row + 1][col] += dp[row][col];
            }
        }
    }

    dp[last_row].iter().sum::<u64>() as usize
}
