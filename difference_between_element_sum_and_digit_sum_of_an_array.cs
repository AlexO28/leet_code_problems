/*
You are given a positive integer array nums.
The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.
Note that the absolute difference between two integers x and y is defined as |x - y|.
*/
using System;


public class Solution {
    public int DifferenceOfSum(int[] nums) {
        int elementSum = 0;
        int digitSum = 0;
        foreach (int num in nums) {
            elementSum += num;
            string numStr = num.ToString();
            for (int j = 0; j < numStr.Length; ++j) {
                digitSum += numStr[j] - '0';
            }
        }
        return Math.Abs(elementSum - digitSum);
    }
}
