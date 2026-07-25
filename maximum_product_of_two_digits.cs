/*
You are given a positive integer n.
Return the maximum product of any two digits in n.
Note: You may use the same digit twice if it appears more than once in n.
*/
using System;


public class Solution {
    public int MaxProduct(int n) {
        char[] digits = n.ToString().ToCharArray();
        Array.Sort(digits);
        Array.Reverse(digits);
        return (int)char.GetNumericValue(digits[0]) * (int)char.GetNumericValue(digits[1]); 
    }
}
