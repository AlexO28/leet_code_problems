# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:
# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.
# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        res = [[-1] * (len(isWater[0])) for j in range(len(isWater))]
        q = deque()
        for i, row in enumerate(isWater):
            for j, x in enumerate(row):
                if x == 1:
                    res[i][j] = 0
                    q.append((i, j))
        dirs = (-1, 0, 1, 0, -1)
        while q:
            i, j = q.popleft()
            for a, b in pairwise(dirs):
                x = i + a
                y = j + b
                if 0 <= x < len(isWater) and 0 <= y < len(isWater[0]) and res[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    q.append((x, y))
        return res
