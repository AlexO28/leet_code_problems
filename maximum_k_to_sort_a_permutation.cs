/*
You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].
You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.
Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.
*/
using System;


public class Solution {
    public int SortPermutation(int[] nums) {
        int res = -1;
        for (int i = 0; i < nums.Length; ++i) {
            if (i != nums[i]) {
                res &= nums[i];
            }
        }
        return Math.Max(res, 0);
    }
}
