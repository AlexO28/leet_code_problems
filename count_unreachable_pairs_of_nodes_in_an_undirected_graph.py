# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
# Return the number of pairs of different nodes that are unreachable from each other.
from collections import deque


class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        edges_dict = {}
        for a, b in edges:
            if a in edges_dict:
                edges_dict[a].append(b)
            else:
                edges_dict[a] = [b]
            if b in edges_dict:
                edges_dict[b].append(a)
            else:
                edges_dict[b] = [a]
        visited = set()
        components = []
        for v in range(n):
            if v not in visited:
                component = 0
                queue = deque([v])
                cur_visit = set([v])
                while queue:
                    elem = queue.pop()
                    if elem not in visited:
                        visited.add(elem)
                        component += 1
                    if elem in edges_dict:
                        for neighbor in edges_dict[elem]:
                            if (neighbor not in visited) and (neighbor not in cur_visit):
                                cur_visit.add(neighbor)
                                queue.append(neighbor)
                components.append(component)
        if len(components) == 1:
            return 0
        else:
            res = 0
            for i in range(len(components)):
                res += components[i] * (n - components[i])
            return res // 2
