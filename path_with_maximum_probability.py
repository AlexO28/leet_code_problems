# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
from typing import List
from heapq import heappush, heappop


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for i in range(n)]
        for edge, probability in zip(edges, succProb):
            node_a, node_b = edge
            graph[node_a].append((node_b, probability))
            graph[node_b].append((node_a, probability))
        priority_queue = [(-1.0, start_node)]
        max_probability = [0.0] * n
        max_probability[start_node] = 1.0
        while priority_queue:
            current_prob_neg, current_node = heappop(priority_queue)
            current_prob = -current_prob_neg
            if max_probability[current_node] > current_prob:
                continue
            for neighbor, edge_prob in graph[current_node]:
                new_probability = current_prob * edge_prob
                if new_probability > max_probability[neighbor]:
                    max_probability[neighbor] = new_probability
                    heappush(priority_queue, (-new_probability, neighbor))
        return max_probability[end_node]
 
