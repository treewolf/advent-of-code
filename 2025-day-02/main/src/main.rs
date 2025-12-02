use std::fs;

// if id is odd lengthed, it cannot have a valid duplicate
fn acceptable_length(x: u64) -> bool {
    let s: String = x.to_string();
    if s.len() % 2 == 0 {
        return true;
    }
    return false;
}

// return true if id is made up of 2 same halves
fn same_half(x: u64) -> bool {
    let s: String = x.to_string();
    let (a, b) = s.split_at(s.len() / 2);
    a == b
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
            if ! acceptable_length(i) {
                continue;
            }

            if same_half(i) {
               total += i; 
            }
        }
    }

    println!("Total sum of invalid ids: {total}");
}
