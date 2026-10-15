/*
You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:
Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
*/
using System.Collections.Generic;


public class Solution {
    public int SumCounts(IList<int> nums) {
        HashSet<int> set;
        int res = 0;
        for (int i = 0; i < nums.Count; ++i) {
            set = new HashSet<int>();
            for (int j = i; j < nums.Count; ++j) {
                set.Add(nums[j]);
                res += set.Count * set.Count;
            }
        }
        return res;
    }
}
