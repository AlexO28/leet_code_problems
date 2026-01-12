# There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.
# A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.
# For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.
# Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.
# Notice that the distance between the two cities is the number of edges in the path between them.
from collections import defaultdict
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        self.g = defaultdict(list)
        for u, v in edges:
            u -= 1
            v -= 1
            self.g[u].append(v)
            self.g[v].append(u)
        ans = [0] * (n - 1)
        self.nxt = 0
        self.mx = 0
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            self.msk = mask
            self.mx = 0
            cur = self.msk.bit_length() - 1
            self.search(cur)
            if self.msk == 0:
                self.msk = mask
                self.mx = 0
                self.search(self.nxt)
                ans[self.mx - 1] += 1
        return ans

    def search(self, u, d=0):
        if self.mx < d:
            self.mx = d
            self.nxt = u
        self.msk ^= 1 << u
        for v in self.g[u]:
            if self.msk >> v & 1:
                self.search(v, d + 1)
