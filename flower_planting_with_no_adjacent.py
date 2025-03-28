# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.
# All gardens have at most 3 paths coming into or leaving it.
# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        if len(paths) == 0:
            return [1]*n
        graph = {}
        for path in paths:
            if path[0] not in graph:
                graph[path[0]] = [path[1]]
            else:
                graph[path[0]].append(path[1])
            if path[1] not in graph:
                graph[path[1]] = [path[0]]
            else:
                graph[path[1]].append(path[0])
        res = [0] * n
        for j in range(n):
            if j+1 in graph:
                used_flowers = list(set([res[i-1] for i in graph[j+1]]))
            else:
                used_flowers = []
            for i in range(1, 5):
                if i not in used_flowers:
                    res[j] = i
                    break
        return res
