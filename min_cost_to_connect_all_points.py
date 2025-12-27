# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
from typing import List
from math import inf


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        g = [[0] * len(points) for _ in range(len(points))]
        dist = [inf] * len(points)
        vis = [False] * len(points)
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                t = abs(x1 - x2) + abs(y1 - y2)
                g[i][j] = t
                g[j][i] = t
        dist[0] = 0
        ans = 0
        for _ in range(len(points)):
            i = -1
            for j in range(len(points)):
                if not vis[j] and (i == -1 or dist[j] < dist[i]):
                    i = j
            vis[i] = True
            ans += dist[i]
            for j in range(len(points)):
                if not vis[j]:
                    dist[j] = min(dist[j], g[i][j])
        return ans
