# You are given a 0-indexed m x n binary matrix grid.
# A 0-indexed m x n difference matrix diff is created with the following procedure:
# Let the number of ones in the ith row be onesRowi.
# Let the number of ones in the jth column be onesColj.
# Let the number of zeros in the ith row be zerosRowi.
# Let the number of zeros in the jth column be zerosColj.
# diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
# Return the difference matrix diff.
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_dict = {}
        col_dict = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i in row_dict:
                        row_dict[i] += 1
                    else:
                        row_dict[i] = 1
                    if j in col_dict:
                        col_dict[j] += 1
                    else:
                        col_dict[j] = 1
        for i in range(len(grid)):
            if i not in row_dict:
                row_dict[i] = 0
        for j in range(len(grid[0])):
            if j not in col_dict:
                col_dict[j] = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = 2*row_dict[i] + 2*col_dict[j] - len(grid[0]) - len(grid)
        return grid
