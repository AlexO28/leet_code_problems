/*
You are given an integer array nums of length n.
An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:
Partition nums into consecutive subarrays of length k.
Cyclically rotate each subarray independently any number of times to the left or to the right.
Return an integer denoting the sum of all possible sortable integers k.
*/
using System;


public class Solution {
    public int SortableIntegers(int[] nums) {
        int[] prefMax = new int[nums.Length + 1];
        for (int i = 0; i < nums.Length; ++i) {
            prefMax[i + 1] = Math.Max(prefMax[i], nums[i]);
        }
        int[] suffMin = new int[nums.Length + 1];
        suffMin[nums.Length] = 1000000000;
        for (int i = nums.Length - 1; i >= 0; --i) {
            suffMin[i] = Math.Min(nums[i], suffMin[i + 1]);
        }
        int[] prefDrop = new int[nums.Length];
        for (int i = 1; i < nums.Length; ++i) {
            prefDrop[i] = prefDrop[i - 1] + (nums[i - 1] > nums[i] ? 1 : 0);
        }
        int res = 0;
        int ii = 0;
        for (int i = 1; i <= (ii = nums.Length / i); ++i) {
            if (nums.Length % i == 0) {
                if (Check(nums, prefMax, suffMin, prefDrop, i)) {
                    res += i;
                }
                if ((i != ii) && Check(nums, prefMax, suffMin, prefDrop, ii)) {
                    res += ii;
                }
            }
        }
        return res;
    }

    private bool Check(int[] nums, int[] prefMax, int[] suffMin, int[] prefDrop, int k) {
        for (int start = 0; start < nums.Length; start += k) {
            int end = start + k - 1;
            int drops = prefDrop[end] - prefDrop[start];
            if (nums[end] > nums[start]) {
                ++drops;
            }
            if ((drops > 1) || (prefMax[start] > suffMin[start])) {
                return false;
            }
        }
        return true;
    }
}
