# You are given an integer array of unique positive integers nums. Consider the following graph:
# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.
from typing import List
from collections import Counter


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for value in nums:
            factor = 2
            while (factor <= value // factor):
                if value % factor == 0:
                    uf.union(value, factor)
                    uf.union(value, value // factor)
                factor += 1
        component_sizes = Counter(uf.find(v) for v in nums)
        return max(component_sizes.values())


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            self.parent[parent_a] = parent_b

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
