/*
The appeal of a string is the number of distinct characters found in the string.
For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.
A substring is a contiguous sequence of characters within a string.
*/
public class Solution {
    public long AppealSum(string s) {
        long res = 0;
        long t = 0;
        int[] pos = new int[26];
        for (int i = 0; i < 26; ++i) {
            pos[i] = -1;
        }
        for (int i = 0; i < s.Length; ++i) {
            int c = s[i] - 'a';
            t += i - pos[c];
            res += t;
            pos[c] = i;
        }
        return res;
    }
}
