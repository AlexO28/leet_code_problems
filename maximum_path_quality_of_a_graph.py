# There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.
# A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).
# Return the maximum quality of a valid path.
# Note: There are at most four edges connected to each node.
from typing import List


class Solution:
    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:
        self.values = values
        self.g = [[] for _ in range(len(values))]
        for u, v, t in edges:
            self.g[u].append((v, t))
            self.g[v].append((u, t))
        self.vis = [False] * len(values)
        self.vis[0] = True
        self.ans = 0
        self.search(0, 0, values[0], maxTime)
        return self.ans

    def search(self, u, cost, value, maxTime):
        if u == 0:
            self.ans = max(self.ans, value)
        for v, t in self.g[u]:
            if cost + t <= maxTime:
                if self.vis[v]:
                    self.search(v, cost + t, value, maxTime)
                else:
                    self.vis[v] = True
                    self.search(v, cost + t, value + self.values[v], maxTime)
                    self.vis[v] = False
