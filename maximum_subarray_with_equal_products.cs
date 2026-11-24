/*
You are given an array of positive integers nums.
An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.
*/
using System;
using System.Numerics;


public class Solution {
    public int MaxLength(int[] nums) {
        int maxLen = 0;
        for (int i = 0; i < nums.Length - 1; ++i) {
            int prod = nums[i];
            int gcd = nums[i];
            int lcm = nums[i];
            for (int j = i + 1; j < nums.Length; ++j) {
                prod *= nums[j];
                gcd = (int)BigInteger.GreatestCommonDivisor(gcd, nums[j]);
                if ((nums[j] == 0) || (lcm == 0)) {
                    lcm = 0;
                } else {
                    lcm = (lcm / (int)BigInteger.GreatestCommonDivisor(lcm, nums[j])) * nums[j];
                }
                if (prod == gcd * lcm) {
                    maxLen = Math.Max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
}
