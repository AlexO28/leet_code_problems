/*
Alice had a 0-indexed array arr consisting of n positive integers. She chose an arbitrary positive integer k and created two new 0-indexed integer arrays lower and higher in the following manner:
lower[i] = arr[i] - k, for every index i where 0 <= i < n
higher[i] = arr[i] + k, for every index i where 0 <= i < n
Unfortunately, Alice lost all three arrays. However, she remembers the integers that were present in the arrays lower and higher, but not the array each integer belonged to. Help Alice and recover the original array.
Given an array nums consisting of 2n integers, where exactly n of the integers were present in lower and the remaining in higher, return the original array arr. In case the answer is not unique, return any valid array.
Note: The test cases are generated such that there exists at least one valid array arr.
*/
impl Solution {
    pub fn recover_array(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums; 
        nums.sort();
        for i in 1..nums.len() {
            let mut d = nums[i] - nums[0];
            if (d > 0) && (d % 2 == 0) {
                let mut vis = vec![false; nums.len()];
                vis[i] = true;
                let mut ans = vec![(nums[0] + nums[i]) / 2];
                let mut l = 1;
                let mut r = i + 1;
                while r < nums.len() {
                    while (l < nums.len()) && vis[l] {
                        l += 1;
                    }
                    while (r < nums.len()) && (nums[r] - nums[l] < d) {
                        r += 1;
                    }
                    if (r == nums.len()) || (nums[r] - nums[l] > d) {
                        break;
                    }
                    vis[r] = true;
                    ans.push((nums[l] + nums[r]) / 2);
                    l += 1;
                    r += 1;
                }
                if (ans.len() == nums.len() / 2) {
                    return ans;
                }
            }
        }
        return Vec::new()
    }
}
