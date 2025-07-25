# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
# Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        unique = [""]
        for word in arr:
            for elem in unique:
                tmp = word + elem
                if len(tmp) == len(set(tmp)):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
        return maxlen
