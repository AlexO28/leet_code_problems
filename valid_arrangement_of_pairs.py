# You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.
# Return any valid arrangement of pairs.
# Note: The inputs will be generated such that there exists a valid arrangement of pairs.
from typing import List
from collections import defaultdict, deque


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        start = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start = node
                break
        path = []
        stack = [start]
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            path.append(stack.pop())
        path.reverse()
        result = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        return result
