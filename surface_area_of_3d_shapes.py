# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
# Return the total surface area of the resulting shapes.
# Note: The bottom face of each shape counts toward its surface area.
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    total_area += 4*grid[i][j] + 2
                    if i > 0:
                        total_area -= 2*min(grid[i][j], grid[i-1][j])
                    if j > 0:
                        total_area -= 2*min(grid[i][j], grid[i][j-1])
        return total_area
