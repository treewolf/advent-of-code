use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");

    // parse
    let mut columns: HashMap<usize, Vec<String>> = HashMap::new();
    let rows: Vec<&str> = contents.trim().split("\n").collect();

    let spaces = Regex::new(r"\s+").unwrap();

    for (_, &value) in rows.iter().enumerate() {
        let modified_value = spaces.replace_all(value, " ").to_string();

        let parts: Vec<String> = modified_value
            .trim()
            .split_whitespace()
            .map(|s| s.to_string())
            .collect();

        for (i, part) in parts.iter().enumerate() {
            columns.entry(i).or_insert_with(Vec::new).push(part.clone());
        }
    }

    // do math
    let mut total: i64 = 0;
    for (_, v) in &columns {
        let mut equation = v.clone();
        let operator = equation.pop();

        let numbers: Vec<i64> = equation
            .into_iter()
            .map(|x| x.parse::<i64>().expect("Cannot parse to number"))
            .collect();

        let subtotal: i64 = match operator.expect("Sign").as_str() {
            "+" => numbers.iter().sum(),
            "*" => numbers.iter().product(),
            _ => continue,
        };

        total += subtotal;
    }

    println!("Total: {}", &total);
}
