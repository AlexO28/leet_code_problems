# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.
# Return the minimum possible area of the rectangle.
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        xmin = len(grid)
        xmax = -1
        ymin = len(grid[0])
        ymax = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    xmin = min(xmin, i)
                    xmax = max(xmax, i)
                    ymin = min(ymin, j)
                    ymax = max(ymax, j)
        if xmax < xmin:
            return 0
        else:
            return (xmax - xmin + 1) * (ymax - ymin + 1)
