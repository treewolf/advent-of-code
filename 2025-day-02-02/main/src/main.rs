use std::collections::HashSet;
use std::fs;

// return true if an id is made of repeated patterns
fn repeated(x: u64) -> bool {
    let s: String = x.to_string();
    let len = s.len();

    if len < 2 {
        return false;
    }

    for split_n in 1..=len / 2 {
        if len % split_n == 0 { 
            let part = &s[0..split_n];
            let expected: String = part.repeat(len / split_n);
            if expected == s {
                return true; 
            }
        }
    }

    false
}


fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");
    let entries: Vec<&str> = contents.trim().split(',').collect();

    let mut total = 0;

    for entry in entries {
        println!("start");

        let ids: Vec<&str> = entry.split('-').collect();
        let first_id: u64 = ids[0].parse().expect("Cannot parse first id to uint");
        let last_id: u64 = ids[1].parse().expect("Cannot parse last id to uint");
        dbg!(first_id);
        dbg!(last_id);

        for i in first_id..=last_id {
            if repeated(i) {
                dbg!(i);
                total += i;
            }
        }
    }

    println!("Total sum of invalid ids: {total}");
}
