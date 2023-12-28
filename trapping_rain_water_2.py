# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
from heapq import heappop, heappush 

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        visited = [[False] * len(heightMap[0]) for j in range(len(heightMap))]
        min_heap = []
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if (i == 0) or (i == len(heightMap) - 1)\
                    or (j == 0) or (j == len(heightMap[0]) - 1):
                    heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True     
        trapped_water = 0
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))      
        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < len(heightMap)) and (0 <= ny < len(heightMap[0]))\
                    and not visited[nx][ny]:
                    trapped_water += max(0, height - heightMap[nx][ny])                  
                    visited[nx][ny] = True
                    heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))      
        return trapped_water
