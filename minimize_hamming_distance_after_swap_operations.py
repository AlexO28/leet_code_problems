# You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.
# The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).
# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.
from typing import List
from collections import defaultdict, Counter


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        self.p = list(range(len(source)))
        for a, b in allowedSwaps:
            self.p[self.find(a)] = self.find(b)
        cnt = defaultdict(Counter)
        for i, x in enumerate(source):
            j = self.find(i)
            cnt[j][x] += 1
        ans = 0
        for i, x in enumerate(target):
            j = self.find(i)
            cnt[j][x] -= 1
            ans += cnt[j][x] < 0
        return ans

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
