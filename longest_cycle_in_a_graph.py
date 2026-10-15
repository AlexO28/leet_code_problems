# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.
# Return the length of the longest cycle in the graph. If no cycle exists, return -1.
# A cycle is a path that starts and ends at the same node.
from math import inf


class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        vis = [False] * len(edges)
        res = -1
        for i in range(len(edges)):
            if vis[i]:
                continue
            j = i
            cycle = []
            while j != -1 and not vis[j]:
                vis[j] = True
                cycle.append(j)
                j = edges[j]
            if j == -1:
                continue
            k = next((k for k in range(len(cycle)) if cycle[k] == j), inf)
            res = max(res, len(cycle) - k)
        return res
