use std::fs;

fn main() {
    let mut contents = fs::read_to_string("input.txt")
        .expect("Cannot read file");
    contents.truncate(contents.trim().len());

    let mut marker = 50;
    let mut zero_count = 0;

    let entries = contents.split("\n");
    for entry in entries 
    {
        // split entry by L or R, and then number
        let (direction, rotation_string) = entry.split_at(1);
        let rotations: i32 = rotation_string.parse().expect("Not a valid number");
        if direction == "L" {
            marker -= rotations;
        }
        else {
            marker += rotations;
        }

        // 100 is modulus since combo is circulor 0-99
        if marker % 100 == 0 {
            zero_count += 1;
        }
    }
    dbg!(zero_count);
}
