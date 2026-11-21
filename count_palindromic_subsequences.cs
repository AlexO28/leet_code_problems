/*
Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.
Note:
A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
*/
public class Solution {
    public int CountPalindromes(string s) {
        int[,,] pre = new int[s.Length + 2, 10, 10];
        int[,,] suf = new int[s.Length + 2, 10, 10];
        int[] t = new int[s.Length];
        for (int i = 0; i < s.Length; ++i) {
            t[i] = s[i] - '0';
        }
        int[] c = new int[10];
        for (int i = 1; i <= s.Length; ++i) {
            int v = t[i - 1];
            for (int j = 0; j < 10; ++j) {
                for (int k = 0; k < 10; ++k) {
                    pre[i, j, k] = pre[i - 1, j, k];
                }
            }
            for (int j = 0; j < 10; ++j) {
                pre[i, j, v] += c[j];
            }
            ++c[v];
        }
        c = new int[10];
        for (int i = s.Length; i > 0; --i) {
            int v = t[i - 1];
            for (int j = 0; j < 10; ++j) {
                for (int k = 0; k < 10; ++k) {
                    suf[i, j, k] = suf[i + 1, j, k];
                }
            }
            for (int j = 0; j < 10; ++j) {
                suf[i, j, v] += c[j];
            }
            ++c[v];
        }
        long res = 0;
        for (int i = 1; i <= s.Length; ++i) {
            for (int j = 0; j < 10; ++j) {
                for (int k = 0; k < 10; ++k) {
                    res += (long) pre[i - 1, j, k] * suf[i + 1, j, k];
                    res %= 1000000007;
                }
            }
        }
        return (int) res;
    }
}
