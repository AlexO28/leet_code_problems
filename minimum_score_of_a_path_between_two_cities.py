# You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.
# The score of a path between two cities is defined as the minimum distance of a road in this path.
# Return the minimum possible score of a path between cities 1 and n.
class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        self.visited = set()
        self.res = inf
        self.g = {}
        for a, b, w in roads:
            if a in self.g:
                self.g[a].append((b, w))
            else:
                self.g[a] = [(b, w)]
            if b in self.g:
                self.g[b].append((a, w))
            else:
                self.g[b] = [(a, w)]
        self.res = inf
        self.search(1)
        return self.res

    def search(self, a):
        self.visited.add(a)
        for b, w in self.g[a]:
            self.res = min(self.res, w)
            if b not in self.visited:
                self.search(b)
