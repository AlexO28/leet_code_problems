# Alice and Bob have an undirected graph of n nodes and three types of edges:
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)
        cnt = 0
        for type, src, dst in edges:
            if type == 3:
                cnt += alice.union(src, dst) | bob.union(src, dst)
        for type, src, dst in edges:
            if type == 1:
                cnt += alice.union(src, dst)
            elif type == 2:
                cnt += bob.union(src, dst)
        if alice.isConnected() and bob.isConnected():
            return len(edges) - cnt
        return -1


class DSU:
    def __init__(self, n):
        self.n = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return 0
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        self.n -= 1
        return 1

    def isConnected(self):
        return self.n == 1
