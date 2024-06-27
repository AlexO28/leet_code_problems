# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertices_dict = {}
        for edge in edges:
            if edge[0] in vertices_dict:
                return edge[0]
            else:
                vertices_dict[edge[0]] = 1
            if edge[1] in vertices_dict:
                return edge[1]
            else:
                vertices_dict[edge[1]] = 1
