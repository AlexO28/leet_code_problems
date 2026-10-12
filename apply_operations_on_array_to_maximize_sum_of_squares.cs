/*
You are given a 0-indexed integer array nums and a positive integer k.
You can do the following operation on the array any number of times:
Choose any two distinct indices i and j and simultaneously update the values of nums[i] to (nums[i] AND nums[j]) and nums[j] to (nums[i] OR nums[j]). Here, OR denotes the bitwise OR operation, and AND denotes the bitwise AND operation.
You have to choose k elements from the final array and calculate the sum of their squares.
Return the maximum sum of squares you can achieve.
Since the answer can be very large, return it modulo 109 + 7.
*/
using System.Collections.Generic;


public class Solution {
    public int MaxSum(IList<int> nums, int k) {
        const int MOD = 1000000007;
        int[] cnt = new int[31];
        foreach (int x in nums) {
            for (int i = 0; i < 31; ++i) {
                if ((x >> i & 1) == 1) {
                    ++cnt[i];
                }
            }
        }
        long res = 0;
        while (k-- > 0) {
            int x = 0;
            for (int i = 0; i < 31; ++i) {
                if (cnt[i] > 0) {
                    x |= 1 << i;
                    --cnt[i];
                }
            }
            res = (res + 1L * x * x) % MOD;
        }
        return (int) res;
    }
}
