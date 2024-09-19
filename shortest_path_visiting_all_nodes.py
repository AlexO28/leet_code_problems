# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        for node in range(len(graph)):
            state = 1 << node
            queue.append((node, state))
            visited.add((node, state))
        steps = 0
        check = (1 << len(graph))-1
        while True:
            for i in range(len(queue)):
                current_node, state = queue.popleft()
                if state == check:
                    return steps
                for neighbor in graph[current_node]:
                    new_state = state | (1 << neighbor)
                    if (neighbor, new_state) not in visited:
                        visited.add((neighbor, new_state))
                        queue.append((neighbor, new_state))
            steps += 1
