/*
You are given an integer array nums and an integer threshold.
Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.
Return the size of any such subarray. If there is no such subarray, return -1.
A subarray is a contiguous non-empty sequence of elements within an array.
*/
using System.Collections.Generic;


public class Solution {
    public int ValidSubarraySize(int[] nums, int threshold) {
        int[] left = new int[nums.Length];
        int[] right = new int[nums.Length];
        for (int i = 0; i < nums.Length; ++i) {
            left[i] = -1;
            right[i] = nums.Length;
        }
        Stack<int> stack = new Stack<int>();
        for (int i = 0; i < nums.Length; ++i) {
            while ((stack.Count > 0) && (nums[stack.Peek()] >= nums[i])) {
                stack.Pop();
            }
            if (stack.Count > 0) {
                left[i] = stack.Peek();
            }
            stack.Push(i);
        }
        stack.Clear();
        for (int i = nums.Length - 1; i >= 0; --i) {
            while ((stack.Count > 0) && (nums[stack.Peek()] >= nums[i])) {
                stack.Pop();
            }
            if (stack.Count > 0) {
                right[i] = stack.Peek();
            }
            stack.Push(i);
        }
        for (int i = 0; i < nums.Length; ++i) {
            int k = right[i] - left[i] - 1;
            if (nums[i] > threshold / k) {
                return k;
            }
        }
        return -1;
    }
}
