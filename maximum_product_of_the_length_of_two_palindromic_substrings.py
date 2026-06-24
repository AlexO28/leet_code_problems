# You are given a 0-indexed string s and are tasked with finding two non-intersecting palindromic substrings of odd length such that the product of their lengths is maximized.
# More formally, you want to choose four integers i, j, k, l such that 0 <= i <= j < k <= l < s.length and both the substrings s[i...j] and s[k...l] are palindromes and have odd lengths. s[i...j] denotes a substring from index i to index j inclusive.
# Return the maximum possible product of the lengths of the two non-intersecting palindromic substrings.
# A palindrome is a string that is the same forward and backward. A substring is a contiguous sequence of characters in a string.
class Solution:
    def maxProduct(self, s: str) -> int:
        zeros = [0] * len(s)
        hlen = zeros.copy()
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                hlen[i] = min(right - i, hlen[2 * center - i])
            while (
                0 <= i - 1 - hlen[i]
                and i + 1 + hlen[i] < len(s)
                and s[i - 1 - hlen[i]] == s[i + 1 + hlen[i]]
            ):
                hlen[i] += 1
            if right < i + hlen[i]:
                center = i
                right = i + hlen[i]
        prefix = zeros.copy()
        suffix = zeros.copy()
        for i in range(len(s)):
            prefix[i + hlen[i]] = max(prefix[i + hlen[i]], 2 * hlen[i] + 1)
            suffix[i - hlen[i]] = max(suffix[i - hlen[i]], 2 * hlen[i] + 1)
        for i in range(1, len(s)):
            prefix[~i] = max(prefix[~i], prefix[~i + 1] - 2)
            suffix[i] = max(suffix[i], suffix[i - 1] - 2)
        for i in range(1, len(s)):
            prefix[i] = max(prefix[i - 1], prefix[i])
            suffix[~i] = max(suffix[~i], suffix[~i + 1])
        return max(prefix[i - 1] * suffix[i] for i in range(1, len(s)))
