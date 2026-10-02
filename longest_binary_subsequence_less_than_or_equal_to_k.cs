/*
You are given a binary string s and a positive integer k.
Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
Note:
The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
*/
public class Solution {
    public int LongestSubsequence(string s, int k) {
        int res = 0;
        int v = 0;
        for (int i = s.Length - 1; i >= 0; --i) {
            if (s[i] == '0') {
                ++res;
            } else if ((res < 30) && ((v | 1 << res) <= k)) {
                v |= 1 << res;
                ++res;
            }
        }
        return res;
    }
}
