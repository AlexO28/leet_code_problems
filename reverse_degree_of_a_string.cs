/*
Given a string s, calculate its reverse degree.
The reverse degree is calculated as follows:
For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
Sum these products for all characters in the string.
Return the reverse degree of s.
*/
public class Solution {
    public int ReverseDegree(string s) {
        int reverseDegree = 0;
        for (int i = 0; i < s.Length; ++i) {
            reverseDegree += (26 - (s[i] - 'a')) * (i + 1);
        }
        return reverseDegree;
    }
}
