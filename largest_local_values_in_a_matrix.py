# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        arr = []
        for i in range(1, len(grid)-1):
            temp = []
            for j in range(1, len(grid)-1):
                temp.append(max(grid[i][j], grid[i][j-1], grid[i][j+1], grid[i+1][j], grid[i+1][j-1], grid[i+1][j+1], grid[i-1][j], grid[i-1][j-1], grid[i-1][j+1]))
            arr.append(temp)
        return arr
