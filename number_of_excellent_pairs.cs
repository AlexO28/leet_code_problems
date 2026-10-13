/*
You are given a 0-indexed positive integer array nums and a positive integer k.
A pair of numbers (num1, num2) is called excellent if the following conditions are satisfied:
Both the numbers num1 and num2 exist in the array nums.
The sum of the number of set bits in num1 OR num2 and num1 AND num2 is greater than or equal to k, where OR is the bitwise OR operation and AND is the bitwise AND operation.
Return the number of distinct excellent pairs.
Two pairs (a, b) and (c, d) are considered distinct if either a != c or b != d. For example, (1, 2) and (2, 1) are distinct.
Note that a pair (num1, num2) such that num1 == num2 can also be excellent if you have at least one occurrence of num1 in the array.
*/
using System.Collections.Generic;
using System.Numerics;


public class Solution {
    public long CountExcellentPairs(int[] nums, int k) {
        HashSet<int> s = new HashSet<int>();
        foreach (int v in nums) {
            s.Add(v);
        }
        long res = 0;
        int[] cnt = new int[32];
        foreach (int v in s) {
            int t = BitOperations.PopCount((uint) v);
            ++cnt[t];
        }
        foreach (int v in s) {
            int t = BitOperations.PopCount((uint) v);
            for (int i = 0; i < 32; ++i) {
                if (t + i >= k) {
                    res += cnt[i];
                }
            }
        }
        return res;
    }
}
