/*
Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.
A multiple of k is any positive integer divisible by k.
*/
use std::collections::HashSet;


impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let unique_numbers: HashSet<i32> = nums.into_iter().collect();
        let mut res = k;
        loop {
            if unique_numbers.contains(&res) {
                res += k;
            } else {
                return res;
            }
        }
    }
}
