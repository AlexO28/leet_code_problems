# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island.
# Return the smallest number of 0's you must flip to connect the two islands.
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if len(grid) == 2:
            return 1
        self.grid = grid
        self.directions = [0, 1, 0, -1, 0]
        self.queue = deque()
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 1:
                    start_i = i
                    start_j = j
        self.search(start_i, start_j)
        steps = 0
        while True:
            for z in range(len(self.queue)):
                i, j = self.queue.popleft()
                for k in range(4):
                    x = i + self.directions[k]
                    y = j + self.directions[k + 1]
                    if (x >= 0) and (x < len(self.grid)) and (y >= 0) and (y < len(self.grid)):
                        if self.grid[x][y] == 1:
                            return steps
                        elif self.grid[x][y] == 0:
                            self.grid[x][y] = 2
                            self.queue.append((x, y))
            steps += 1


    def search(self, i, j):
        self.queue.append((i, j))
        self.grid[i][j] = 2
        for k in range(4):
            x = i + self.directions[k]
            y = j + self.directions[k+1]
            if (x >= 0) and (x < len(self.grid)) and (y >= 0) and (y < len(self.grid)) and (self.grid[x][y] == 1):
                self.search(x, y)
