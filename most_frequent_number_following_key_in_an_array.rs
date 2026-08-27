/*
You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.
For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:
0 <= i <= nums.length - 2,
nums[i] == key and,
nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.
*/
use std::collections::HashMap;


impl Solution {
    pub fn most_frequent(nums: Vec<i32>, key: i32) -> i32 {
        let mut freqs: HashMap<i32, i32> = HashMap::new();
        let mut saw_before = false;
        for num in nums {
            if saw_before {
                *freqs.entry(num).or_insert(0) += 1;
            }
            saw_before = (num == key);
        }
        return *freqs.iter().max_by_key(|&(_, &val)| val).map(|(k, _)| k).unwrap();
    }
}
