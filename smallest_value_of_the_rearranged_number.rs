/*
You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.
Return the rearranged number with minimal value.
Note that the sign of the number does not change after rearranging the digits.
*/
impl Solution {
    pub fn smallest_number(num: i64) -> i64 {
        let mut num = num;
        if num > 0 {
            let mut chars: Vec<char> = num.to_string().chars().collect();
            let mut number_of_zeros = 0;
            let mut digits: Vec<i32> = Vec::new();
            for elem in chars.iter() {
                if *elem == '0' {
                    number_of_zeros += 1;
                } else {
                    digits.push(elem.to_digit(10).unwrap() as i32);
                }
            }
            digits.sort();
            chars[0] = char::from_digit(digits[0] as u32, 10).unwrap();
            if number_of_zeros > 0 {
                for i in 0..number_of_zeros {
                    chars[i + 1] = '0';
                }
            }
            if digits.len() > 1 {
                for i in 1..digits.len() {
                    chars[number_of_zeros + i] = char::from_digit(digits[i] as u32, 10).unwrap();
                }
            }
            let s: String = chars.into_iter().collect();
            return s.parse::<i64>().unwrap();
        } else if num < 0 {
            num = -num;
            let mut chars: Vec<char> = num.to_string().chars().collect();
            let mut digits: Vec<i32> = Vec::new();
            for elem in chars.iter() {
                digits.push(elem.to_digit(10).unwrap() as i32);
            }
            digits.sort();
            digits.reverse();
            for i in 0..digits.len() {
                chars[i] = char::from_digit(digits[i] as u32, 10).unwrap();
            }
            let s: String = chars.into_iter().collect();
            return -s.parse::<i64>().unwrap();
        } else {
            return 0;
        }
    }
}
