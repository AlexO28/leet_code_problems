# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.
# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.component_count = size

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False      
        self.parent[root1] = root2
        self.component_count -= 1
        return True

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        num_vertices = len(edges)
        parents = list(range(num_vertices + 1))
        union_find = UnionFind(num_vertices + 1)
        conflict = None
        cycle = None
        for index, (from_vertex, to_vertex) in enumerate(edges):
            if parents[to_vertex] != to_vertex:
                conflict = index
            else:
                parents[to_vertex] = from_vertex
                if not union_find.union(from_vertex, to_vertex):
                    cycle = index                  
        if conflict is None:
            return edges[cycle]
        redundant_edge_target = edges[conflict][1]
        if cycle is not None:
            return [parents[redundant_edge_target], redundant_edge_target]
        return edges[conflict]
