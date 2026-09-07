# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
# A node u is an ancestor of another node v if u can reach v via a set of edges.
from typing import List
from collections import deque, defaultdict


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.g = defaultdict(list)
        for u, v in edges:
            self.g[u].append(v)
        self.ans = [[] for _ in range(n)]
        for i in range(n):
            self.bfs(i)
        return self.ans


    def bfs(self, s):
        q = deque([s])
        vis = {s}
        while q:
            i = q.popleft()
            for j in self.g[i]:
                if j not in vis:
                    vis.add(j)
                    q.append(j)
                    self.ans[j].append(s)
