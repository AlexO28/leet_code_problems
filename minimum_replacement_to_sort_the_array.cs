/*
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.
Return the minimum number of operations to make an array that is sorted in non-decreasing order.
*/
public class Solution {
    public long MinimumReplacement(int[] nums) {
        long res = 0;
        int mx = nums[nums.Length - 1];
        for (int i = nums.Length - 2; i >= 0; --i) {
            if (nums[i] <= mx) {
                mx = nums[i];
                continue;
            }
            int k = (nums[i] + mx - 1) / mx;
            res += k - 1;
            mx = nums[i] / k;
        }
        return res;
    }
}
