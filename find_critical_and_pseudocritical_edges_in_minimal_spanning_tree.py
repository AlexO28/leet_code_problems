# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.
# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.
# Note that you can return the indices of the edges in any order.
from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        for edge_idx, edge in enumerate(edges):
            edge.append(edge_idx)
        edges.sort(key=lambda edge: edge[2])
        uf_mst = UnionFind(n)
        mst_weight = 0
        for from_node, to_node, weight, _ in edges:
            if uf_mst.union(from_node, to_node):
                mst_weight += weight
        critical_edges = []
        pseudo_critical_edges = []

        for from_node, to_node, weight, original_idx in edges:
            uf_without = UnionFind(n)
            weight_without = 0

            for curr_from, curr_to, curr_weight, curr_idx in edges:
                if curr_idx != original_idx:
                    if uf_without.union(curr_from, curr_to):
                        weight_without += curr_weight
            if uf_without.num_components > 1 or weight_without > mst_weight:
                critical_edges.append(original_idx)
                continue
            uf_with = UnionFind(n)
            uf_with.union(from_node, to_node)
            weight_with = weight

            for curr_from, curr_to, curr_weight, curr_idx in edges:
                if curr_idx != original_idx:
                    if uf_with.union(curr_from, curr_to):
                        weight_with += curr_weight
            if weight_with == mst_weight:
                pseudo_critical_edges.append(original_idx)
        return [critical_edges, pseudo_critical_edges]


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.num_components = n

    def union(self, node_a: int, node_b: int) -> bool:
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a == root_b:
            return False
        self.parent[root_a] = root_b
        self.num_components -= 1
        return True

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
