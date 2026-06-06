# There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.
# There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.
# Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.
# A subpath of a path is a contiguous sequence of cities within that path.
from typing import List
from collections import Counter


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        self.m = len(paths)
        max_val = max(len(path) for path in paths)
        BASE = 133331
        self.MOD = 18446744073709551617
        self.p = [0] * (max_val + 1)
        self.p[0] = 1
        for i in range(1, len(self.p)):
            self.p[i] = self.p[i - 1] * BASE % self.MOD
        self.hh = []
        for path in paths:
            k = len(path)
            h = [0] * (k + 1)
            for i, x in enumerate(path, 1):
                h[i] = h[i - 1] * BASE % self.MOD + x
            self.hh.append(h)
        l = 0
        r = min(len(path) for path in paths)
        while l < r:
            mid = (l + r + 1) >> 1
            if self.check(mid):
                l = mid
            else:
                r = mid - 1
        return l

    def check(self, k):
        cnt = Counter()
        for h in self.hh:
            vis = set()
            for i in range(1, len(h) - k + 1):
                j = i + k - 1
                x = (h[j] - h[i - 1] * self.p[j - i + 1]) % self.MOD
                if x not in vis:
                    vis.add(x)
                    cnt[x] += 1
        return max(cnt.values()) == self.m
