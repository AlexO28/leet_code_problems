# You are given an m x n binary matrix matrix.
# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
# Return the maximum number of rows that have all values equal after some number of flips.
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_counter = {}
        for row in matrix:
            if row[0] == 0:
                standardized_row = tuple(row)
            else:
                standardized_row = tuple(1 - x for x in row)
            if standardized_row in row_counter:
                row_counter[standardized_row] += 1
            else:
                row_counter[standardized_row] = 1
        return max(row_counter.values())
