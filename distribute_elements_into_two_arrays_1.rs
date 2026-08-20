/*
You are given a 1-indexed array of distinct integers nums of length n.
You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:
If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.
Return the array result.
*/
impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut arr1: Vec<i32> = Vec::new();
        let mut arr2: Vec<i32> = Vec::new();
        arr1.push(nums[0]);
        arr2.push(nums[1]);
        for i in 2..nums.len() {
            if arr1[arr1.len() - 1] >= arr2[arr2.len() - 1] {
                arr1.push(nums[i]);
            } else {
                arr2.push(nums[i]);
            }
        }
        arr1.extend(arr2);
        return arr1;
    }
}
