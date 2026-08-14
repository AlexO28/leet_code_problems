/*
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public int MaximumLengthSubstring(string s) {
        int maxLen = 2;
        for (int i = 0; i < s.Length - 1; ++i) {
            Dictionary<char, int> freqs = new Dictionary<char, int>();
            int ind = -1;
            for (int j = i; j < s.Length; ++j) {
                if (!freqs.ContainsKey(s[j])) {
                    freqs[s[j]] = 1;
                } else {
                    freqs[s[j]] += 1;
                    if (freqs[s[j]] == 3) {
                        ind = j - 1;
                        break;
                    }
                }
            }
            if (ind >= 0) {
                maxLen = Math.Max(maxLen, ind - i + 1);
            } else {
                maxLen = Math.Max(maxLen, s.Length - i);
            }
        }
        return maxLen;
    }
}
