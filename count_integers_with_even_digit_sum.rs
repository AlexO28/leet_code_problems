/*
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
The digit sum of a positive integer is the sum of all its digits.
*/
impl Solution {
    pub fn count_even(num: i32) -> i32 {
        let mut res = 0;
        for i in 1..(num + 1) {
            if i.to_string().chars().map(|c| c.to_digit(10).unwrap()).sum::<u32>() % 2 == 0 {
                res += 1
            }
        }
        res
    }
}
