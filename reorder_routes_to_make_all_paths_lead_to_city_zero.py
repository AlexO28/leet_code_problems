# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
# It's guaranteed that each city can reach city 0 after reorder.
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.tree = {}
        for b, a in connections:
            if a in self.tree:
                self.tree[a].append([b, 1])
            else:
                self.tree[a] = [[b, 1]]
        for b, a in connections:
            if b in self.tree:
                if [a, 1] not in self.tree[b]:
                    self.tree[b].append([a, 0])
            else:
                self.tree[b] = [[a, 0]]
        self.count = 0
        self.visited = set()
        self.visited.add(0)
        self.countPaths(0)
        return self.count

    def countPaths(self, node):
        for child, mark in self.tree[node]:
            if child not in self.visited:
                self.visited.add(child)
                if mark == 0:
                    self.count += 1
                self.countPaths(child)
