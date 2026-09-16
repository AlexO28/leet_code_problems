/*
You are building a string s of length n one character at a time, prepending each new character to the front of the string. The strings are labeled from 1 to n, where the string with length i is labeled si.
The score of si is the length of the longest common prefix between si and sn (Note that s == sn).
Given the final string s, return the sum of the score of every si.
*/
class Solution {
    public long sumScores(String s) {
        char[] ss = s.toCharArray();
        int[] z = new int[s.length()];
        int l = 0;
        int r = 0;
        z[0] = s.length();
        for (int i = 1; i < s.length(); ++i) {
            if (i <= r) {
                z[i] = Math.min(z[i - l], r - i + 1);
            }
            while ((i + z[i] < s.length()) && (ss[z[i]] == ss[i + z[i]])) {
                ++z[i];
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }            
        }
        long summa = 0;
        for (int i = 0; i < s.length(); ++i) {
            summa += z[i];
        }
        return summa;
    }
}
