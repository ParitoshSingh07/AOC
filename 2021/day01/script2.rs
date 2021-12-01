fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

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
    for slice in vec.iter().copied().collect::<Vec<i32>>().windows(2) {
    if let [prev, next] = slice {
        println!("{}--{}", prev, next);
            if next > prev {
                acc += 1;
            }
        }
    }

    println!("{}", acc);
    // Part 2

    let mut vec2: Vec<i32> = Vec::new();
    for slice in vec.iter().copied().collect::<Vec<i32>>().windows(3) {
        println!("{:?}", slice);
        vec2.push(slice.iter().sum());
    }

    println!("{:?}", vec2);
    let mut acc = 0;
    for slice in vec2.iter().copied().collect::<Vec<i32>>().windows(2) {
    if let [prev, next] = slice {
        println!("{}--{}", prev, next);
            if next > prev {
                acc += 1;
            }
        }
    }
    println!("{}", acc);
}


