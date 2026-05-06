/*
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public int CountGoodSubstrings(string s) {
        if (s.Length < 3) {
            return 0;
        } else {
            int numberOfOccurences = 0;
            for (int i = 0; i < s.Length - 2; ++i) {
                string line = s.Substring(i, 3);
                if (new HashSet<char>(line).Count() == 3) {
                    numberOfOccurences += 1;
                }
            }
            return numberOfOccurences;
        }
    }
}
