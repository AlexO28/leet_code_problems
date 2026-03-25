# You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.
# A connected trio is a set of three nodes where there is an edge between every pair of them.
# The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.
# Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.
from typing import List
from math import inf


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = [[False] * n for i in range(n)]
        deg = [0] * n
        for u, v in edges:
            u -= 1
            v -= 1
            g[u][v] = True
            g[v][u] = True
            deg[u] += 1
            deg[v] += 1
        ans = inf
        for i in range(n):
            for j in range(i + 1, n):
                if g[i][j]:
                    for k in range(j + 1, n):
                        if g[i][k] and g[j][k]:
                            ans = min(ans, deg[i] + deg[j] + deg[k] - 6)
        if ans == inf:
            return -1
        else:
            return ans
