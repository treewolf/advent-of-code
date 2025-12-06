use std::collections::VecDeque;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");
    let lines: Vec<&str> = contents.lines().collect();

    let max_columns = lines[0].len();
    let mut columns: Vec<VecDeque<String>> = vec![VecDeque::new(); max_columns];

    for line in lines {
        let chars: Vec<char> = line.chars().collect();

        for (i, char) in chars.iter().enumerate() {
            columns[i].push_back(char.to_string());
        }
    }

    // make values
    // each number can be max(len-1) because of the operator
    let mut subtotals: Vec<i64> = Vec::new();
    let mut operators: Vec<String> = Vec::new();
    for num_set in &columns {
        let mut tens = 10_i64.pow(num_set.len() as u32 - 2);

        let mut subtotal = 0;

        for i in 0..(num_set.len()) {
            let c = num_set.get(i).unwrap();

            // get operator and break
            if i == &num_set.len() - 1 {
                operators.push((*c).to_string());
                continue;
            }

            if *c == " " {
                subtotal = subtotal / 10;
            } else {
                subtotal += c.parse::<i64>().unwrap() * tens;
            }
            tens = tens / 10;
        }
        subtotals.push(subtotal);
    }

    let mut total = 0;
    let mut semitotal = 0;

    let mut op: String = operators.get(0).unwrap().to_string();

    for (i, num) in subtotals.iter().enumerate() {
        dbg!(&i, &num);
        if let Some(x) = operators.get(i){
            if x.as_str() != " " {
                op = x.to_string();
            }
        }

        if *num == 0 {
            total += semitotal;
            semitotal = 0;
            continue;
        }

        match op.as_str() {
            "*" => {
                if semitotal == 0 {
                    semitotal = 1;
                }
                semitotal *= num;
            },
            _ => semitotal += num,
        }

        if i == subtotals.len() -1 {
            total += semitotal;
        }

        dbg!(&semitotal, &total);
    }

    println!("Grand total: {}", total);
}
