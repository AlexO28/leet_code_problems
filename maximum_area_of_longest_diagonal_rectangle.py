# You are given a 2D 0-indexed integer array dimensions.
# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.
# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res_area = 0
        max_diagonal = 0
        for x, y in dimensions:
            cur_diagonal = x**2 + y**2
            if cur_diagonal > max_diagonal:
                max_diagonal = cur_diagonal
                res_area = x * y
            elif cur_diagonal == max_diagonal:
                res_area = max(res_area, x * y)
        return res_area
