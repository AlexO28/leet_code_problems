/*
You are given a 0-indexed string num of length n consisting of digits.
Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.
*/
using System.Collections.Generic;


public class Solution {
    public bool DigitCount(string num) {
        Dictionary<char, int> mapping = new Dictionary<char, int>();
        foreach (char digit in num) {
            if (mapping.ContainsKey(digit)) {
                mapping[digit] += 1;
            } else {
                mapping.Add(digit, 1);
            }
        }
        for (int i = 0; i < num.Length; ++i) {
            char iChar = i.ToString()[0];
            if (mapping.ContainsKey(iChar)) {
                if (mapping[iChar] != (int)char.GetNumericValue(num[i])) {
                    return false;
                }
            } else {
                if ((int)char.GetNumericValue(num[i]) > 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
