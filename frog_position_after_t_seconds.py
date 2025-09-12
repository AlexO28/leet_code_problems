# Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.
# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
# Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.
from collections import defaultdict, deque
from typing import List


class Solution:
    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        graph = defaultdict(list)
        for node_u, node_v in edges:
            graph[node_u].append(node_v)
            graph[node_v].append(node_u)
        queue = deque([(1, 1.0)])
        visited = [False] * (n + 1)
        visited[1] = True
        while queue and t >= 0:
            level_size = len(queue)
            for _ in range(level_size):
                current_node, probability = queue.popleft()
                unvisited_children_count = len(graph[current_node]) - int(
                    current_node != 1
                )
                if current_node == target:
                    if (unvisited_children_count == 0) or (t == 0):
                        return probability
                    else:
                        return 0
                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, probability / unvisited_children_count))
            t -= 1
        return 0
