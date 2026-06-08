# There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.
# Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.
# In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).
# Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.
from math import inf
from typing import List


class Solution:
    def minCost(
        self, maxTime: int, edges: List[List[int]], passingFees: List[int]
    ) -> int:
        m = maxTime + 1
        f = [[inf] * len(passingFees) for _ in range(m)]
        f[0][0] = passingFees[0]
        for i in range(1, m):
            for x, y, t in edges:
                if t <= i:
                    f[i][x] = min(f[i][x], f[i - t][y] + passingFees[x])
                    f[i][y] = min(f[i][y], f[i - t][x] + passingFees[y])
        res = min(f[i][-1] for i in range(m))
        if res < inf:
            return res
        else:
            return -1
