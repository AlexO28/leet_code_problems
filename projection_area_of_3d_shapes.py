# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
# We view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
# Return the total area of all three projections.
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            cur_max = 0
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res += 1
                    cur_max = max(cur_max, grid[i][j])
            res += cur_max
        for j in range(len(grid[0])):
            cur_max = 0
            for i in range(len(grid)):
                if grid[i][j] > 0:
                    cur_max = max(cur_max, grid[i][j])
            res += cur_max
        return res
