/*
You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on an infinite number line. With one step, you can move either one position to the left, or one position to the right.
Given a positive integer k, return the number of different ways to reach the position endPos starting from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.
Two ways are considered different if the order of the steps made is not exactly the same.
Note that the number line includes negative integers.
*/
using System;


public class Solution {
    private int[,] f;
    private const int MOD = 1000000007;

    public int NumberOfWays(int startPos, int endPos, int k) {
        ++k;
        f = new int[k, k];
        for (int i = 0; i < k; ++i) {
            for (int j = 0; j < k; ++j) {
                f[i, j] = -1;
            }
        }
        return Search(Math.Abs(startPos - endPos), k - 1);
    }

    private int Search(int i, int j) {
        if ((i > j) || (j < 0)) {
            return 0;
        } else if (j == 0) {
            return i == 0 ? 1 : 0;
        } else if (f[i, j] != -1) {
            return f[i, j];
        } else {
            int res = (Search(i + 1, j - 1) + Search(Math.Abs(i - 1), j - 1)) % MOD;
            f[i, j] = res;
            return res;
        }
    }
}
