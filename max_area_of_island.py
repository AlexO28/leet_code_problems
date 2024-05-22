# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    max_area = max(max_area, self.find_area(i, j))
        return max_area
    
    def find_area(self, i, j):
        if self.grid[i][j] == 0:
            return 0
        area = 1
        self.grid[i][j] = 0
        if i < len(self.grid)-1:
            area += self.find_area(i+1, j)
        if i > 0:
            area += self.find_area(i-1, j)
        if j > 0:
            area += self.find_area(i, j-1)
        if j < len(self.grid[0])-1:
            area += self.find_area(i, j+1)
        return area
 
