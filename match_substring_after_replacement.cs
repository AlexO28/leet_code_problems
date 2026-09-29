/*You are given two strings s and sub. You are also given a 2D character array mappings where mappings[i] = [oldi, newi] indicates that you may perform the following operation any number of times:
Replace a character oldi of sub with newi.
Each character in sub cannot be replaced more than once.
Return true if it is possible to make sub a substring of s by replacing zero or more characters according to mappings. Otherwise, return false.
A substring is a contiguous non-empty sequence of characters within a string.*/
using System.Collections.Generic;


public class Solution {
    public bool MatchReplacement(string s, string sub, char[][] mappings) {
        Dictionary<char, HashSet<char>> info = new Dictionary<char, HashSet<char>>();
        foreach (char[] map in mappings) {
            if (!info.TryGetValue(map[0], out HashSet<char> set)) {
                set = info[map[0]] = new HashSet<char>();
            }
            set.Add(map[1]);
        }
        for (int i = 0; i < s.Length - sub.Length + 1; ++i) {
            bool ok = true;
            for (int j = 0; (j < sub.Length) && ok; ++j) {
                char a = s[i + j];
                char b = sub[j];
                if ((a != b) && (!(info.TryGetValue(b, out HashSet<char> set) && (set.Contains(a))))) {
                    ok = false;
                }
            }
            if (ok) {
                return true;
            }
        }
        return false;
    }
}
