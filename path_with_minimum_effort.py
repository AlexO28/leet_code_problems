# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
from collections import deque
from typing import List
from bisect import bisect_left
from itertools import pairwise


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.heights = heights
        return bisect_left(range(10**6), True, key=self.check)

    def check(self, h):
        q = deque([(0, 0)])
        vis = {(0, 0)}
        dirs = (-1, 0, 1, 0, -1)
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == len(self.heights) - 1 and j == len(self.heights[0]) - 1:
                    return True
                for a, b in pairwise(dirs):
                    x = i + a
                    y = j + b
                    if (
                        0 <= x < len(self.heights)
                        and 0 <= y < len(self.heights[0])
                        and (x, y) not in vis
                        and abs(self.heights[i][j] - self.heights[x][y]) <= h
                    ):
                        q.append((x, y))
                        vis.add((x, y))
        return False
