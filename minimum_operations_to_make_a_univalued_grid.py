# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
# A uni-value grid is a grid where all the elements of it are equal.
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        data = []
        prevRemainder = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                main_part, remainder = divmod(grid[i][j], x)
                if prevRemainder == -1:
                    prevRemainder = remainder
                elif prevRemainder != remainder:
                    return -1
                data.append(main_part)
        if len(data) == 1:
            return 0
        data.sort()
        res = 0
        for j in range(len(data) // 2):
            res += data[len(data) - 1 - j] - data[j]
        return res
