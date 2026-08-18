/*
You are given an integer array nums and an integer k.
An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
Return the largest almost missing integer from nums. If no such integer exists, return -1.
A subarray is a contiguous sequence of elements within an array.
*/
use std::collections::HashMap;
use std::cmp::max;
use std::collections::HashSet;


impl Solution {
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        if (k == nums.len() as i32) {
            return *nums.iter().max().unwrap() as i32;
        } else if (k == 1) {
            let mut freqs = HashMap::new();
            for num in &nums {
                if freqs.contains_key(&num) {
                    freqs.insert(num, 2);
                } else {
                    freqs.insert(num, 1);
                }
            }
            let mut res = -1;
            for (key, value) in &freqs {
                if *value == 1 {
                    res = max(res, **key);
                }
            }
            return res;
        } else {
            if nums.len() == 2 {
                return max(nums[0], nums[1]);
            } else {
                if (nums[0] == nums[nums.len() - 1]) {
                    return -1;
                }
                let mut data = HashSet::new();
                for i in 1..(nums.len() - 1) {
                    data.insert(nums[i]);
                }
                let has_first = data.contains(&nums[0]);
                let has_last = data.contains(&nums[nums.len() - 1]);
                if !has_first && !has_last {
                    return max(nums[0], nums[nums.len() - 1]);
                } else if has_first && !has_last {
                    return nums[nums.len() - 1];
                } else if !has_first && has_last {
                    return nums[0];
                } else {
                    return -1;
                }
            }
        }       
    }
}
