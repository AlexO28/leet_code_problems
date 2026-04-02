# There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.
# A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.
# The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.
# Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.
from math import inf
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        dist = [inf] * (n + 1)
        dist[n] = 0
        q = [(0, n)]
        MOD = 1000000007
        while q:
            _, u = heappop(q)
            for v, w in g[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(q, (dist[v], v))
        arr = list(range(1, n + 1))
        arr.sort(key=lambda i: dist[i])
        f = [0] * (n + 1)
        f[n] = 1
        for i in arr:
            for j, _ in g[i]:
                if dist[i] > dist[j]:
                    f[i] = (f[i] + f[j]) % MOD
        return f[1]
