/*
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.
In one move, you can either:
Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.
Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.
*/
impl Solution {
    pub fn min_moves(target: i32, max_doubles: i32) -> i32 {
        let mut target = target;
        let mut res = 0;
        for i in 0..max_doubles {
            if target < 2 {
                break;
            } else {
                let new_target = target / 2;
                res += target % 2 + 1;
                target = new_target;
            }
        }
        res + target - 1
    }
}
