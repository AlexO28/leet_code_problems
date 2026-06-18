/*
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m.
*/
using System;


public class Solution {
    public bool IsThree(int n) {
        if (n < 4) {
            return false;
        } else {
            for (int i = 2; i <= n / 2; ++i) {
                (int quotient, int remainder) = Math.DivRem(n, i);
                if (remainder == 0) {
                    return (i == quotient);
                }
            }
            return false;
        }
    }
}
