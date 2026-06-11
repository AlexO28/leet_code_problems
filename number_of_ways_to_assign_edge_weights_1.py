# There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.
# Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.
# The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.
# Select any one node x at the maximum depth. Return the number of ways to assign edge weights in the path from node 1 to x such that its total cost is odd.
# Since the answer may be large, return it modulo 109 + 7.
# Note: Ignore all edges not in the path from node 1 to x.
from typing import List
from functools import cache


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        self.graph = {}
        for u, v in edges:
            if u in self.graph:
                self.graph[u].append(v)
            else:
                self.graph[u] = [v]
            if v in self.graph:
                self.graph[v].append(u)
            else:
                self.graph[v] = [u]
        self.visited = []
        return pow(2, self.calculate_depth(1, 0) - 1, 1000000007)

    @cache
    def calculate_depth(self, node, parent):
        max_depth = 0
        for kid in self.graph[node]:
            if kid != parent:
                max_depth = max(max_depth, self.calculate_depth(kid, node) + 1)
        return max_depth
