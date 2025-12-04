use std::fs;

fn main() {
    let contents = fs::read_to_string("test-input.txt").expect("Cannot read file");

    // read into grid format
    let mut grid: Vec<Vec<u8>> = Vec::new();
    for line in contents.lines() {
        let row: Vec<u8> = line
            .trim()
            .chars()
            .map(|c| if c == '@' { 1 } else { 0 })
            .collect();
        grid.push(row);
    }

    let spots = valid_spot(&grid, 4);
    println!("{:?}", spots);

    println!("Valid spots: {}", spots.len());
}

// find valid spots and record location vector
fn valid_spot(grid: &Vec<Vec<u8>>, neighbor_limit: usize) -> Vec<(usize, usize)> {
    let mut spots = Vec::new();
    let rows = grid.len();
    let cols = grid[0].len();

    let directions = vec![
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
    ];

    for i in 0..rows {
        for j in 0..cols {
            let mut neighbors_count: usize = 0;

            // care only about the cells that are occupied
            if grid[i][j] != 1 {
                continue;
            }

            for (dx, dy) in &directions {
                let new_x = i as isize + dx;
                let new_y = j as isize + dy;

                // check if position is occupied
                if new_x >= 0 && new_x < rows as isize && new_y >= 0 && new_y < cols as isize {
                    if grid[new_x as usize][new_y as usize] == 1 {
                        neighbors_count += 1;
                    }
                }
            }
            println!("{:?}: {}", (i, j), neighbors_count);

            if neighbors_count < neighbor_limit {
                spots.push((i, j));
            }
        }
    }
    spots
}
