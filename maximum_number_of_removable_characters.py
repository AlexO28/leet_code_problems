# You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).
# You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.
# Return the maximum k you can choose such that p is still a subsequence of s after the removals.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        self.s = s
        self.p = p
        l = 0
        self.removable = removable
        r = len(removable)
        while l < r:
            mid = (l + r + 1) >> 1
            if self.check(mid):
                l = mid
            else:
                r = mid - 1
        return l

    def check(self, k):
        rem = [False] * len(self.s)
        for i in self.removable[:k]:
            rem[i] = True
        i = 0
        j = 0
        while (i < len(self.s)) and (j < len(self.p)):
            if (not rem[i]) and (self.p[j] == self.s[i]):
                j += 1
            i += 1
        return j == len(self.p)
