# A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.
# Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.
# Two sequences are considered different if at least one element differs from each other.
from typing import List
from functools import cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.MOD = 10 ** 9 + 7
        self.n = n
        self.rollMax = rollMax
        return self.search(0, 0, 0)

    @cache
    def search(self, i, j, x):
        if i >= self.n:
            return 1
        ans = 0
        for k in range(1, 7):
            if k != j:
                ans += self.search(i + 1, k, 1)
            elif x < self.rollMax[j - 1]:
                ans += self.search(i + 1, j, x + 1)
        return ans % self.MOD
