# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        deltaX = [-1, 0, 1, 0]
        deltaY = [0, 1, 0, -1]
        dis = [
            [[0 for x in range(k + 1)] for y in range(len(grid[0]))]
            for z in range(len(grid))
        ]
        vis = [
            [[False for x in range(k + 1)] for y in range(len(grid[0]))]
            for z in range(len(grid))
        ]
        q = []
        q.append((0, 0, 0))
        vis[0][0][0] = True
        while q:
            (curX, curY, curK) = q.pop(0)
            if (curX == len(grid) - 1) and (curY == len(grid[0]) - 1):
                return dis[curX][curY][curK]
            for i in range(4):
                newX = curX + deltaX[i]
                newY = curY + deltaY[i]
                if (
                    (newX < 0)
                    or (newX >= len(grid))
                    or (newY < 0)
                    or (newY >= len(grid[0]))
                ):
                    continue
                newK = curK
                if grid[newX][newY] == 1:
                    newK += 1
                if newK > k:
                    continue
                if vis[newX][newY][newK]:
                    continue
                dis[newX][newY][newK] = dis[curX][curY][curK] + 1
                vis[newX][newY][newK] = True
                q.append((newX, newY, newK))
        return -1
