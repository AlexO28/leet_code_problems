# Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.
# Return the maximum possible product of the lengths of the two palindromic subsequences.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.
class Solution:
    def maxProduct(self, s: str) -> int:
        temp = 1 << len(s)
        p = [True] * (temp)
        for k in range(1, temp):
            i = 0
            j = len(s) - 1
            while i < j:
                while i < j and (k >> i & 1) == 0:
                    i += 1
                while i < j and (k >> j & 1) == 0:
                    j -= 1
                if i < j and s[i] != s[j]:
                    p[k] = False
                    break
                i += 1
                j -= 1
        ans = 0
        for i in range(1, temp):
            if p[i]:
                mx = (temp - 1) ^ i
                j = mx
                a = i.bit_count()
                while j:
                    if p[j]:
                        b = j.bit_count()
                        ans = max(ans, a * b)
                    j = (j - 1) & mx
        return ans
