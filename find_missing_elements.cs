/*
You are given an integer array nums consisting of unique integers.
Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.
The smallest and largest integers of the original range are still present in nums.
Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public IList<int> FindMissingElements(int[] nums) {
        Array.Sort(nums);
        int minVal = nums[0];
        int maxval = nums[nums.Length - 1];
        IList<int> res = new List<int>();
        for (int i = 1; i < nums.Length; ++i) {
            if (nums[i] > nums[i - 1] + 1) {
                for (int j = nums[i - 1] + 1; j < nums[i]; ++j) {
                    res.Add(j);
                }
            }
        }
        return res;
    }
}
