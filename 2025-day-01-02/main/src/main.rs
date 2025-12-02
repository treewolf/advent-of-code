use std::fs;

fn main() {
    let contents = fs::read_to_string("test1-input.txt").expect("Cannot read file");
    let entries: Vec<&str> = contents.trim().split('\n').collect();

    let mut marker: i32 = 50;
    let mut zero_count: i32 = 0;

    for entry in entries {
        println!("start");
        dbg!(zero_count);
        dbg!(entry);
        // Split the entry into the direction and rotation amount
        let (direction, rotation_string) = entry.split_at(1);
        let rotations: i32 = rotation_string.trim().parse().expect("Not a valid number");

        // Calculate the final marker based on direction
        let final_mark = if direction == "L" {
            marker - rotations
        } else {
            marker + rotations
        };
        dbg!(final_mark);

        // Check for full rotations
        let full_rotations = final_mark.abs() / 100;
        dbg!(full_rotations);

        zero_count += full_rotations;
        dbg!(zero_count);

        if final_mark < 0 && marker != 0 {
            zero_count += 1;
            dbg!(zero_count);
        }
        if final_mark == 0 {
            zero_count += 1;
            dbg!(zero_count);
        }

        // reset dial
        if final_mark >= 100 {
            marker = final_mark % 100;
        } else if final_mark < 0 {
            marker = (final_mark % 100) + 100;
        } else {
            marker = final_mark;
        }
        dbg!(marker);
        println!("end")
    }

    println!("Total zero crossings: {}", zero_count);
}
