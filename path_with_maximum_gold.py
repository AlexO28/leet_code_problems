# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, self.extractGoldFromCell(grid, i, j, []))
        return max_gold

    def extractGoldFromCell(self, grid, i, j, visited):
        res = grid[i][j]
        visited.append([i, j])
        candidate = 0
        if i > 0:
            if grid[i-1][j] > 0:
                if [i-1, j] not in visited:
                    candidate = max(candidate, self.extractGoldFromCell(grid, i-1, j, visited.copy()))
        if i < len(grid)-1:
            if grid[i+1][j] > 0:
                if [i+1, j] not in visited:
                    candidate = max(candidate, self.extractGoldFromCell(grid, i+1, j, visited.copy()))
        if j > 0:
            if grid[i][j-1] > 0:
                if [i, j-1] not in visited:
                    candidate = max(candidate, self.extractGoldFromCell(grid, i, j-1, visited.copy()))
        if j < len(grid[0])-1:
            if grid[i][j+1] > 0:
                if [i, j+1] not in visited:
                    candidate = max(candidate, self.extractGoldFromCell(grid, i, j+1, visited.copy()))
        return res + candidate
