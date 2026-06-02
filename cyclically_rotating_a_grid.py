# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.
# The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:
# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:
# Return the matrix after applying k cyclic rotations to it.
from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.grid = grid
        for p in range(int(min(len(grid) / 2, len(grid[0]) / 2))):
            self.rotate(p, k)
        return grid

    def rotate(self, p, k):
        nums = []
        row_max = len(self.grid) - p - 1
        col_max = len(self.grid[0]) - p - 1
        for j in range(p, col_max):
            nums.append(self.grid[p][j])
        for j in range(p, row_max):
            nums.append(self.grid[j][col_max])
        for j in range(col_max, p, -1):
            nums.append(self.grid[row_max][j])
        for j in range(row_max, p, -1):
            nums.append(self.grid[j][p])
        k %= len(nums)
        if k > 0:
            nums = nums[k:] + nums[:k]
            i = 0
            for j in range(p, col_max):
                self.grid[p][j] = nums[i]
                i += 1
            for j in range(p, row_max):
                self.grid[j][col_max] = nums[i]
                i += 1
            for j in range(col_max, p, -1):
                self.grid[row_max][j] = nums[i]
                i += 1
            for j in range(row_max, p, -1):
                self.grid[j][p] = nums[i]
                i += 1
