/*
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
A substring is a contiguous sequence of characters within a string.
*/
public class Solution {
    public int LargestVariance(string s) {
        int res = 0;
        for (char elem1 = 'a'; elem1 <= 'z'; ++elem1) {
            for (char elem2 = 'a'; elem2 <= 'z'; ++elem2) {
                if (elem1 == elem2) {
                    continue;
                }
                int[] f = new int[] {0, -s.Length};
                for (int i = 0; i < s.Length; ++i) {
                    if (s[i] == elem1) {
                        ++f[0];
                        ++f[1];
                    } else if (s[i] == elem2) {
                        f[1] = Math.Max(f[0] - 1, f[1] - 1);
                        f[0] = 0;
                    }
                    res = Math.Max(res, f[1]);
                }
            }
        }
        return res;
    }
}
