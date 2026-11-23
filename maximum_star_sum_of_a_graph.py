# There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.
# You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
# A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.
# The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.
# The star sum is the sum of the values of all the nodes present in the star graph.
# Given an integer k, return the maximum star sum of a star graph containing at most k edges.
from math import inf


class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
        max_sum = -inf
        for element in range(len(vals)):
            if element not in graph:
                max_sum = max(max_sum, vals[element])
                continue
            cur_sum = vals[element]
            chosen_vals = [vals[next_element] for next_element in graph[element] if vals[next_element] > 0]
            if len(chosen_vals) > 0:
                chosen_vals.sort(reverse=True)
                chosen_vals = chosen_vals[:k]
                cur_sum += sum(chosen_vals)
            max_sum = max(max_sum, cur_sum)
        return max_sum
