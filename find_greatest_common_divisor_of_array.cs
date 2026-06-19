/*
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
*/
using System.Numerics;


public class Solution {
    public int FindGCD(int[] nums) {
        int minVal = 1001;
        int maxVal = 0;
        foreach (int num in nums) {
            if (num < minVal) {
                minVal = num;
            }
            if (num > maxVal) {
                maxVal = num;
            }
        }
        return (int)BigInteger.GreatestCommonDivisor(minVal, maxVal);       
    }
}
