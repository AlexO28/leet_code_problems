/*
You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
Sort the values at odd indices of nums in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
Return the array formed after rearranging the values of nums.
*/
impl Solution {
    pub fn sort_even_odd(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        let mut nums_even: Vec<i32> = Vec::new();
        let mut nums_odd: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            if i % 2 == 0 {
                nums_even.push(nums[i]);
            } else {
                nums_odd.push(nums[i]);
            }
        }
        nums_even.sort();
        nums_odd.sort();
        nums_odd.reverse();
        let mut i = 0;
        let mut j = 0;
        for k in 0..nums.len() {
            if k % 2 == 0 {
                nums[k] = nums_even[i];
                i += 1;
            } else {
                nums[k] = nums_odd[j];
                j += 1;
            }
        }
        nums
    }
}
