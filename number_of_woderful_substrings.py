# A wonderful string is a string where at most one letter appears an odd number of times.
# For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.
# A substring is a contiguous sequence of characters in a string.
from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        if len(word) == 1:
            return 1
        counts = defaultdict(int)
        counts[0] = 1
        res = 0
        state = 0
        for c in word:
            state ^= 1 << (ord(c) - ord("a"))
            res += counts[state]
            res += sum(counts[state ^ (1 << i)] for i in range(10))
            counts[state] += 1
        return res
