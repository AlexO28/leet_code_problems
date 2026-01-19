# Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.
# For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.
# Return the number of substrings that satisfy the condition above.
# A substring is a contiguous sequence of characters within a string.
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i, a in enumerate(s):
            for j, b in enumerate(t):
                if a != b:
                    l = 0
                    r = 0
                    while i > l and j > l and s[i - l - 1] == t[j - l - 1]:
                        l += 1
                    while (
                        i + r + 1 < len(s)
                        and j + r + 1 < len(t)
                        and s[i + r + 1] == t[j + r + 1]
                    ):
                        r += 1
                    ans += (l + 1) * (r + 1)
        return ans
