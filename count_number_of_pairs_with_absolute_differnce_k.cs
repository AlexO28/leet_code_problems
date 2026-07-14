/*
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
*/
using System;


public class Solution {
    public int CountKDifference(int[] nums, int k) {
        if (nums.Length < 2) {
            return 0;
        }
        int numberOfPairs = 0;
        for (int i = 0; i < nums.Length - 1; ++i) {
            for (int j = i + 1; j < nums.Length; ++j) {
                if (Math.Abs(nums[j] - nums[i]) == k) {
                    ++numberOfPairs;
                }
            }
        }
        return numberOfPairs;
    }
}
