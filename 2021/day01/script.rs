use itertools::Itertools;

fn main() {
    let string = "
line one
line two
".trim();
    println!("{}", string);
    println!("{:?}", string);
    
    let string = "
199
200
208
210
200
207
240
269
260
263
".trim();
    let vec: Vec<i32> = string.split("\n").map(|x| x.parse::<i32>().unwrap()).collect();
    println!("{:?}", vec);
    // Part 1
    let mut acc = 0;
    for (prev, next) in vec.iter().copied().tuple_windows() {
        println!("{}--{}", prev, next);
        if next > prev {
            acc += 1;
        }
    }
    println!("{}", acc);
    // Part 2

    let mut vec2: Vec<i32> = Vec::new();
    for (item1, item2, item3) in vec.iter().copied().tuple_windows() {
        vec2.push(item1 + item2 + item3);
    };
    println!("{:?}", vec2);
    let mut acc = 0;
    for (prev, next) in vec2.into_iter().tuple_windows() {
        println!("{}--{}", prev, next);
        if next > prev {
            acc += 1;
        }
    }
    println!("{}", acc);
}


