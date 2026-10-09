/*
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.
Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array.
*/
using System.Collections.Generic;


public class Solution {
    public bool FindSubarrays(int[] nums) {
        if (nums.Length == 2) {
            return false;
        }
        HashSet<int> info = new HashSet<int>();
        for (int i = 0; i < nums.Length - 1; ++i) {
            int summa = nums[i] + nums[i + 1];
            if (info.Contains(summa)) {
                return true;
            } else {
                info.Add(summa);
            }
        }
        return false;
    }
}
