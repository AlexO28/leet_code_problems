# You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.
# The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.
# To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].
# In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.
# Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.
from heapq import heappop, heappush


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {}
        for u, v, count_nodes in edges:
            if u in graph:
                graph[u].append([v, count_nodes + 1])
            else:
                graph[u] = [[v, count_nodes + 1]]
            if v in graph:
                graph[v].append([u, count_nodes + 1])
            else:
                graph[v] = [[u, count_nodes + 1]]
        if 0 not in graph:
            return 1
        queue = [[0, 0]]
        distances = [0] + [maxMoves + 1] * (n - 1)    
        while queue:
            distance, current_node = heappop(queue)
            for neighbor, weight in graph[current_node]:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heappush(queue, [new_distance, neighbor])
        answer = sum((distance <= maxMoves) for distance in distances)
        for u, v, count_nodes_between in edges:
            answer += min(count_nodes_between,  min(count_nodes_between, max(0, maxMoves - distances[u])) + min(count_nodes_between, max(0, maxMoves - distances[v]))) 
        return answer
