/*
You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:
The digit sum of n (the sum of its digits).
The digit product of n (the product of its digits).
Return true if n is divisible by this sum; otherwise, return false.
*/
impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let mut summa: i32 = 0;
        let mut product: i32 = 1;
        for elem in n.to_string().chars() {
            let mut int_elem: i32 = elem.to_digit(10).unwrap() as i32;
            summa += int_elem;
            product *= int_elem;
        }
        n % (summa + product) == 0
    }
}
