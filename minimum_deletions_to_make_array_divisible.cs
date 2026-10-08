/*
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.
Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.
Note that an integer x divides y if y % x == 0.
*/
using System;


public class Solution {
    public int MinOperations(int[] nums, int[] numsDivide) {
        int x = 0;
        foreach (int num in numsDivide) {
            x = gcd(x, num);
        }
        const int y0 = 1 << 30;
        int y = y0;
        foreach (int num in nums) {
            if (x % num == 0) {
                y = Math.Min(y, num);
            }
        }
        if (y == y0) {
            return -1;
        }
        int res = 0;
        foreach (int num in nums) {
            if (num < y) {
                ++res;
            }
        }
        return res;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
