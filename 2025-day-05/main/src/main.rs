use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Cannot read file");

    // parse
    let parts: Vec<&str> = contents.split("\n\n").collect();
    
    let mut fresh_ingredient_ranges: Vec<(usize, usize)> = Vec::new();
    for i in parts[0].trim().split('\n') {
        let (x,y) = i.split_once('-').unwrap();
        let xval = x.parse::<usize>().unwrap();
        let yval = y.parse::<usize>().unwrap();
        fresh_ingredient_ranges.push((xval, yval));
    }

    let available_ingredients: Vec<usize> = parts[1].trim()
        .split('\n')
        .map(|x| x.parse::<usize>().unwrap())
        .collect();
   
    let mut total_fresh = 0;
    for i in available_ingredients {
        if is_fresh(&fresh_ingredient_ranges, &i) {
            total_fresh += 1;
        }
    }

    println!("Part 1: Fresh ingredients: {}", total_fresh);

    // part 2
    let mut total_range_fresh = 0;

    merge_ranges(&mut fresh_ingredient_ranges);
    
    for (start, end) in &fresh_ingredient_ranges {
        let count: usize = match *end - *start {
            x => x + 1 as usize,
        };
        total_range_fresh += count;
    }

    println!("Part 2: Range of fresh ingredients: {}", total_range_fresh);
}

fn is_fresh(ranges: &Vec<(usize, usize)>, ingredient: &usize) -> bool {
    for (start, end) in ranges {
        if *ingredient >= *start && *ingredient <= *end {
            return true;
        }
    }
    false
}

fn merge_ranges(ranges: &mut Vec<(usize, usize)>) {
    ranges.sort_by(|a, b| a.0.cmp(&b.0));

    let mut merged_ranges: Vec<(usize, usize)> = Vec::new();
    let mut current_range = ranges[0]; 

    for &next_range in &ranges[1..] {
        if next_range.0 <= current_range.1 {
            current_range.1 = current_range.1.max(next_range.1);
        } else {
            merged_ranges.push(current_range);
            current_range = next_range; 
        }
    }
    
    merged_ranges.push(current_range);
    *ranges = merged_ranges;
}
