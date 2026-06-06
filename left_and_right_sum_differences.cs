/*
You are given a 0-indexed integer array nums of size n.
Define two arrays leftSum and rightSum where:
leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
*/
using System;
using System.Linq;


public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        if (nums.Length == 1) {
            return new[] { 0 };
        } else {
            int sum = nums.Sum();
            int leftSum = 0;
            int rightSum = sum;
            int[] res = new int[nums.Length]; 
            for (int i = 0; i < nums.Length; ++i) {
                rightSum -= nums[i];
                res[i] = Math.Abs(leftSum - rightSum);
                leftSum += nums[i];
            }
            return res;
        }

    }
}
