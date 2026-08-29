# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.
# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.
# Note that node 0 will not be a restricted node.
from typing import List
from collections import deque


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = {}
        for edge in edges:
            if (edge[0] not in restricted) and (edge[1] not in restricted):
                if edge[0] in graph:
                    graph[edge[0]].append(edge[1])
                else:
                    graph[edge[0]] = [edge[1]]
                if edge[1] in graph:
                    graph[edge[1]].append(edge[0])
                else:
                    graph[edge[1]] = [edge[0]]
        q = deque([0])
        visited = set()
        while q:
            elem = q.pop()
            visited.add(elem)
            if elem in graph:
                for neighbor in graph[elem]:
                    if neighbor not in visited:
                        q.append(neighbor)
        return len(visited)
