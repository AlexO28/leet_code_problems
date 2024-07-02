# You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left = [[0]*n for i in range(n)]
        right = [[0]*n for i in range(n)]
        up = [[0]*n for i in range(n)]
        down = [[0]*n for i in range(n)]
        mines_dict = {}
        for i, j in mines:
            mines_dict[str(i) + "_" + str(j)] = 1
        for i in range(n):
            number_of_ones = 0
            for j in range(n):
                if str(i) + "_" + str(j) in mines_dict:
                    number_of_ones = 0
                else:
                    number_of_ones += 1
                left[i][j] = number_of_ones
        for i in range(n):
            number_of_ones = 0
            for j in range(n-1, -1, -1):
                if str(i) + "_" + str(j) in mines_dict:
                    number_of_ones = 0
                else:
                    number_of_ones += 1
                right[i][j] = number_of_ones
        for j in range(n):
            number_of_ones = 0
            for i in range(n):
                if str(i) + "_" + str(j) in mines_dict:
                    number_of_ones = 0
                else:
                    number_of_ones += 1
                down[i][j] = number_of_ones
        for j in range(n):
            number_of_ones = 0
            for i in range(n-1, -1, -1):
                if str(i) + "_" + str(j) in mines_dict:
                    number_of_ones = 0
                else:
                    number_of_ones += 1
                up[i][j] = number_of_ones
        minval = 0
        for i in range(n):
            for j in range(n):
                minval = max(minval, min(left[i][j], right[i][j], up[i][j], down[i][j]))
        return minval
