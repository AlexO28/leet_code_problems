/*
Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.
One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.
Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.
Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.
*/
impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        let MOD = 1000000007;
        let mut ans: i64 = 1;
        let mut count = 0;
        let mut last = 0;
        for (i, c) in corridor.chars().enumerate() {
            if (c == 'S') {
                count += 1;
                if (count > 2) && (count % 2 > 0) {
                    ans = (ans * ((i - last) as i64)) % MOD;
                }
                last = i;
            }
        }
        if (count == 0) || (count % 2 > 0) {
            ans = 0;
        }
        ans as i32
    }
}
