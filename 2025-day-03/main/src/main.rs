use std::cmp;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");
    let entries: Vec<&str> = contents.trim().split('\n').collect();

    // only 2 batteries can be turned on. so first number must be largest
    // unless it is on the end. then second largest number must be found.

    let mut total_joltage: u64 = 0;

    for bank in entries.iter() {
        dbg!(bank);
        let batteries: Vec<u64> = bank
            .chars()
            .filter_map(|c| c.to_digit(10).map(|d| d as u64))
            .collect();

        // get largest number, sliding window
        let mut biggest = 0;
        let mut first_num: u64;

        for (index, &first_num) in batteries.iter().enumerate() {
            for last_index in (index + 1)..batteries.len() {
                let last_num = batteries[last_index];

                let combined = first_num * 10 + last_num;
                biggest = cmp::max(biggest, combined);
            }
        }
        dbg!(biggest);
        total_joltage += biggest;
    }

    println!("Total output: {}", total_joltage);
}
