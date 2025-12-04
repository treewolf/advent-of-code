use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");
    let entries: Vec<&str> = contents.trim().split('\n').collect();

    let mut total_joltage: u64 = 0;

    for bank in entries.iter() {
        dbg!(bank);
        let batteries: Vec<u64> = bank
            .chars()
            .filter_map(|c| c.to_digit(10).map(|d| d as u64))
            .collect();

        let biggest = find_largest_combination(&batteries);
        total_joltage += biggest;
    }

    println!("Total output: {}", total_joltage);
}

fn find_largest_combination(batteries: &[u64]) -> u64 {
    let mut result = Vec::new();

    // len of num
    let mut remaining = 12;
    let mut start_index = 0;

    for _ in 0..batteries.len() {
        if remaining == 0 {
            break;
        }

        let end_index = batteries.len() - remaining + 1;
        let max_digit = batteries[start_index..end_index]
            .iter()
            .cloned()
            .max()
            .unwrap();

        result.push(max_digit);
        remaining -= 1;

        start_index += batteries[start_index..end_index]
            .iter()
            .position(|&x| x == max_digit)
            .unwrap() + 1;
    }

    let combined: String = result.iter().map(|&num| num.to_string()).collect();
    combined.parse::<u64>().unwrap()
}
