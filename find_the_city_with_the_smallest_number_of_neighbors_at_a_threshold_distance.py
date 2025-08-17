# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        self.graph = [[float("inf")] * n for _ in range(n)]
        for start, end, weight in edges:
            self.graph[end][start] = weight
            self.graph[start][end] = weight
        res_city = n
        min_reachable_cities = float("inf")
        for i in range(n - 1, -1, -1):
            reachable_cities = self.dijkstra(i, n, distanceThreshold)
            if reachable_cities < min_reachable_cities:
                min_reachable_cities = reachable_cities
                res_city = i
        return res_city

    def dijkstra(self, u, n, distance_threshold):
        distances = [float("inf")] * n
        distances[u] = 0
        visited = [False] * n
        for i in range(n):
            k = -1
            for j in range(n):
                if not visited[j] and (k == -1 or distances[k] > distances[j]):
                    k = j
            visited[k] = True
            for j in range(n):
                distances[j] = min(distances[j], distances[k] + self.graph[k][j])
        return sum(d <= distance_threshold for d in distances)
