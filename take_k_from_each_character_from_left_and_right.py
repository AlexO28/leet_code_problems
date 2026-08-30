# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq_dict = Counter(s)
        for key in "abc":
            if freq_dict[key] < k:
                return -1
        if len(s) == k:
            return k
        max_val = 0
        j = 0
        for i, c in enumerate(s):
            freq_dict[c] -= 1
            while freq_dict[c] < k:
                freq_dict[s[j]] += 1
                j += 1
            max_val = max(max_val, i - j + 1)
        return len(s) - max_val
