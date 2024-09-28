# You are given an m x n binary matrix grid.
# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
# Return the highest possible score after making any number of moves (including zero moves).
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    grid[i][j] ^= 1
        result = 0
        for j in range(len(grid[0])):
            num_ones = sum(grid[i][j] for i in range(len(grid)))
            result += max(num_ones, len(grid)-num_ones)*(1 << (len(grid[0]) - j - 1))
        return result
