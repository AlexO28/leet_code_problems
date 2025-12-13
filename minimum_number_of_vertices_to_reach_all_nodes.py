# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.
# Notice that you can return the vertices in any order.
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        bad_nodes = set()
        for start, end in edges:
            bad_nodes.add(end)
        return [j for j in range(n) if j not in bad_nodes]
