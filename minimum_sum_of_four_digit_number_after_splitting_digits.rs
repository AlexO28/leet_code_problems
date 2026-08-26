/*
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
*/
impl Solution {
    pub fn minimum_sum(num: i32) -> i32 {
        let mut chars_list: Vec<i32> = num.to_string().chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
        chars_list.sort();
        return chars_list[0] * 10 + chars_list[1] * 10 + chars_list[2] + chars_list[3];
    }
}
