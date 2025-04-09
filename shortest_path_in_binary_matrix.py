# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        grid[0][0] = 1
        queue = deque([[0, 0]])
        path_length = 1
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if (temp[0] == len(grid) - 1) and (temp[1] == len(grid) - 1):
                    return path_length
                for x in range(temp[0] - 1, temp[0] + 2):
                    for y in range(temp[1] - 1, temp[1] + 2):
                        if (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid)):
                            if grid[x][y] == 0:
                                grid[x][y] = 1
                                queue.append([x, y])
            path_length += 1
        return -1
