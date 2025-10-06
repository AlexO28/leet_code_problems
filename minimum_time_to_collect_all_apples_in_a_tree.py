# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.
# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.
from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.hasApple = hasApple
        self.visited = [False] * n
        return self.search(0, 0)

    def search(self, node, cost):
        if self.visited[node]:
            return 0
        else:
            self.visited[node] = True
            children_cost = 0
            for neighbor in self.graph[node]:
                children_cost += self.search(neighbor, 2)
            if (not self.hasApple[node]) and (children_cost == 0):
                return 0
            else:
                return cost + children_cost
