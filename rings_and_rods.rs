/*
There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.
You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:
The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
Return the number of rods that have all three colors of rings on them.
*/
impl Solution {
    pub fn count_points(rings: String) -> i32 {
        let mut ringColor = ' ';
        let mut rodeNumber = 0;
        let mut red_values = vec![false; 10];
        let mut green_values = vec![false; 10];
        let mut blue_values = vec![false; 10];
        for (position, elem) in rings.chars().enumerate() {
            if (position % 2) == 0 {
                if (ringColor == ' ') {
                    ringColor = elem;
                } else {
                    if (ringColor == 'R') {
                        red_values[rodeNumber] = true;
                    } else if (ringColor == 'G') {
                        green_values[rodeNumber] = true;
                    } else if (ringColor == 'B') {
                        blue_values[rodeNumber] = true;
                    }
                    ringColor = elem;
                }
            } else {
                rodeNumber = elem.to_digit(10).unwrap() as usize;
            }
        }
        if (ringColor == 'R') {
            red_values[rodeNumber] = true;
        } else if (ringColor == 'G') {
            green_values[rodeNumber] = true;
        } else if (ringColor == 'B') {
            blue_values[rodeNumber] = true;
        }
        let mut number_of_good_rods = 0;
        for i in 0..red_values.len() {
            if (red_values[i]) && (green_values[i]) && (blue_values[i]) {
                number_of_good_rods += 1;
            }
        }
        number_of_good_rods
    }
}
