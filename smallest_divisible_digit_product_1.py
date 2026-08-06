/*
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.  
*/
using System;


public class Solution {
    public int SmallestNumber(int n, int t) {
        while (true) {
            int prod = 1;
            foreach (char digit in n.ToString()) {
                prod *= (int)char.GetNumericValue(digit);
            }
            if (prod % t == 0) {
                return n;
            }
            ++n;
        }
    }
}
