# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
# You are given two arrays redEdges and blueEdges where:
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
from collections import deque, defaultdict
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [defaultdict(list), defaultdict(list)]
        for start, end in redEdges:
            graph[0][start].append(end)
        for start, end in blueEdges:
            graph[1][start].append(end)
        distances = [-1] * n
        visited = set()
        queue = deque([(0, 0), (0, 1)])
        distance = 0
        while queue:
            for i in range(len(queue)):
                node, color = queue.popleft()
                if distances[node] == -1:
                    distances[node] = distance
                visited.add((node, color))
                if color == 0:
                    color = 1
                else:
                    color = 0
                for neighbor in graph[color][node]:
                    if (neighbor, color) not in visited:
                        queue.append((neighbor, color))
            distance += 1
        return distances
