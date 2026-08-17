/*
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
*/
impl Solution {
    pub fn count_elements(nums: Vec<i32>) -> i32 {
        let mut min_val = nums[0];
        let mut max_val = nums[0];
        for &num in &nums {
            if (num < min_val) {
                min_val = num;
            } else if (num > max_val) {
                max_val = num;
            }
        }
        if (max_val == min_val) {
            return 0;
        }
        let mut res = 0;
        for &num in &nums {
            if (num > min_val) && (num < max_val) {
                res += 1;
            }
        }
        res
    }
}
