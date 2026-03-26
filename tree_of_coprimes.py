# There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a value associated with it, and the root of the tree is node 0.
# To represent this tree, you are given an integer array nums and a 2D array edges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree.
# Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.
# An ancestor of a node i is any other node on the shortest path from node i to the root. A node is not considered an ancestor of itself.
# Return an array ans of size n, where ans[i] is the closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ancestor.
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        self.nums = nums
        self.g = defaultdict(list)
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        self.f = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    self.f[i].append(j)
        self.stks = defaultdict(list)
        self.ans = [-1] * len(nums)
        self.search(0, -1, 0)
        return self.ans

    def search(self, i, fa, depth):
        t = -1
        k = -1
        for v in self.f[self.nums[i]]:
            stk = self.stks[v]
            if stk and stk[-1][1] > k:
                t, k = stk[-1]
        self.ans[i] = t
        for j in self.g[i]:
            if j != fa:
                self.stks[self.nums[i]].append((i, depth))
                self.search(j, i, depth + 1)
                self.stks[self.nums[i]].pop()
