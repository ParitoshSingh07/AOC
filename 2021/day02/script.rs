fn main() {
    let string = "
forward 5
down 5
forward 8
up 3
down 8
forward 2
".trim();
    let res: Vec<&str> = string.split("\n").collect();
    let mut x = 0;
    let mut y = 0;
    // Part 1
    for line in res.iter() {
        let (command, value) = line.split_once(" ").unwrap();
        let int_val = value.parse::<i32>().unwrap();
        println!("{}", command);
        println!("{}", int_val);
        if command == "forward" {
            x += int_val;
        }
        else if command == "up" {
            y -= int_val;
        }
        else if command == "down" {
            y += int_val;
        }
        else {
            println!("bad command");
        }
    }
    println!("{} {} - {}", x, y, x*y);
    
    
    // Part 2
    let mut x = 0;
    let mut y = 0;
    let mut aim = 0;
    for line in res.iter() {
        let (command, value) = line.split_once(" ").unwrap();
        let int_val = value.parse::<i32>().unwrap();
        println!("{}", command);
        println!("{}", int_val);
        if command == "forward" {
            x += int_val;
            y += aim * int_val;
        }
        else if command == "up" {
            aim -= int_val;
        }
        else if command == "down" {
            aim += int_val;
        }
        else {
            println!("bad command");
        }
    }
    println!("{} {} - {}", x, y, x*y);
}


