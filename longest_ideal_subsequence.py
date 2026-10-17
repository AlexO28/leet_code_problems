# You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:
# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
from string import ascii_lowercase


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [1] * len(s)
        d = {s[0]: 0}
        for i in range(1, len(s)):
            a = ord(s[i])
            for b in ascii_lowercase:
                if abs(a - ord(b)) <= k:
                    if b in d:
                        dp[i] = max(dp[i], dp[d[b]] + 1)
            d[s[i]] = i
        return max(dp)
